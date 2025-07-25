import hashlib
from Crypto.Hash import RIPEMD

def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()

def double_sha256(data: bytes) -> bytes:
    return sha256(sha256(data))

def ripemd160(data: bytes) -> bytes:
    h = RIPEMD.new()
    h.update(data)
    return h.digest()
