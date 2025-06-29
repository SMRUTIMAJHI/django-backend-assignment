import redis

try:
    r = redis.Redis(host='localhost', port=6379)
    print("Connected:", r.ping())  # Should print True
except Exception as e:
    print("Redis not running:", e)
