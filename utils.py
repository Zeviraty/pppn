import hashlib
import random

def hash(value: str) -> int:
    return int(hashlib.sha1(value.encode()).hexdigest(), 16)

def distance(a: int, b: int) -> int:
    return a ^ b

class Address():
    def __init__(self, ip: str, port:int):
        self.ip = ip
        self.port = port

    def __repr__(self):
        return f"{self.ip}:{self.port}"
