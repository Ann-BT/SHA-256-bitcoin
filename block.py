import time
import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __str__(self):
        return f"{self.sender} → {self.receiver}: {self.amount} BTC"

def calculate_merkle_root(transactions) -> str:
    def hash_pair(a, b):
        return hashlib.sha256((a + b).encode()).hexdigest()

    hashes = [hashlib.sha256(str(tx).encode()).hexdigest() for tx in transactions]

    while len(hashes) > 1:
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])
        hashes = [hash_pair(hashes[i], hashes[i + 1]) for i in range(0, len(hashes), 2)]

    return hashes[0] if hashes else ""

class Block:
    def __init__(self, index, data, prev_hash, difficulty, timestamp=None):
        self.index = index
        self.data = data  # list of Transaction objects
        self.prev_hash = prev_hash
        self.difficulty = difficulty
        self.timestamp = timestamp if timestamp else time.time()
        self.merkle_root = calculate_merkle_root(data)
        self.nonce = 0
        self.hash = None

    def compute_hash(self):
        content = f"{self.index}{self.prev_hash}{self.timestamp}{self.merkle_root}{self.nonce}"
        return hashlib.sha256(hashlib.sha256(content.encode()).digest()).hexdigest()
