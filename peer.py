import utils
import socket

class Peer():
    def __init__(self) -> None:
        pass

    def put(self, key, value) -> bool:
        return True

    def get(self, key) -> any:
        return ""

    def connect(self,adress,port) -> bool:
        return True

    def get_peers(self) -> list:
        return []
