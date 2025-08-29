from utils import Address
import socket

class Peer():
    def __init__(self, starters: list[Address], ) -> None:
        pass

    def put(self, key, value) -> bool:
        return True

    def get(self, key) -> any:
        return ""

    def connect(self,address: Address,port) -> bool:
        return True

    def get_peers(self) -> list:
        return []
