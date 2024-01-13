import os 
import redis 

client = redis.Redis.from_url(
    os.environ["REDIS_URI"],
    decode_responses=True, # automatically converts the responses from bytes to strings
)