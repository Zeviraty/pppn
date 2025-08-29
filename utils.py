import hashlib
import random

def hash(value: str) -> int:
    return int(hashlib.sha1(value.encode()).hexdigest(), 16)

def distance(a: int, b: int) -> int:
    return a ^ b
