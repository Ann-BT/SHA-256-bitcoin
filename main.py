from block import Block, Transaction
from miner import mine_block, adjust_difficulty
from address import create_address
from datetime import datetime

TARGET_BLOCK_TIME = 10  # seconds

def fmt(ts):
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# 🧱 Genesis block
genesis = Block(
    index=0,
    data=["System initialized"],
    prev_hash="0" * 64,
    difficulty=3
)
print(f"\n📦 [Genesis Block]")
elapsed = mine_block(genesis)
print(f"Index       : {genesis.index}")
print(f"Timestamp   : {fmt(genesis.timestamp)}")
print(f"Data        : {genesis.data}")
print(f"Prev Hash   : {genesis.prev_hash}")
print(f"Merkle Root : {genesis.merkle_root}")
print(f"Nonce       : {genesis.nonce}")
print(f"Hash        : {genesis.hash}")
print(f"Difficulty  : {genesis.difficulty}")

# 🔁 Block #1 with transactions
difficulty = adjust_difficulty(TARGET_BLOCK_TIME, elapsed, genesis.difficulty)
tx1 = Transaction("Alice", "Bob", 2)
tx2 = Transaction("Charlie", "Dave", 1.5)

block1 = Block(
    index=1,
    data=[tx1, tx2],
    prev_hash=genesis.hash,
    difficulty=difficulty
)
print(f"\n📦 [Block #1]")
elapsed = mine_block(block1)
print(f"Index       : {block1.index}")
print(f"Timestamp   : {fmt(block1.timestamp)}")
print(f"Data        : {[str(tx) for tx in block1.data]}")
print(f"Prev Hash   : {block1.prev_hash}")
print(f"Merkle Root : {block1.merkle_root}")
print(f"Nonce       : {block1.nonce}")
print(f"Hash        : {block1.hash}")
print(f"Difficulty  : {block1.difficulty}")

# 🏷 Bitcoin address
print(f"\n🏷️ [Bitcoin Address]")
public_key = "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
btc_address = create_address(public_key)
print(f"Public Key  : {public_key}")
print(f"Address     : {btc_address}")
block = block1
for i in range(2, 12):  # Tạo block #2 đến #11 (10 block)
    difficulty = adjust_difficulty(TARGET_BLOCK_TIME, elapsed, block.difficulty)

    tx1 = Transaction("UserA", "UserB", i * 0.1)
    tx2 = Transaction("UserC", "UserD", i * 0.2)
    new_block = Block(index=i, data=[tx1, tx2], prev_hash=block.hash, difficulty=difficulty)

    print(f"\n📦 [Block #{i}]")
    elapsed = mine_block(new_block)
    print(f"Index       : {new_block.index}")
    print(f"Timestamp   : {fmt(new_block.timestamp)}")
    print(f"Data        : {[str(tx) for tx in new_block.data]}")
    print(f"Prev Hash   : {new_block.prev_hash}")
    print(f"Merkle Root : {new_block.merkle_root}")
    print(f"Nonce       : {new_block.nonce}")
    print(f"Hash        : {new_block.hash}")
    print(f"Difficulty  : {new_block.difficulty}")

    block = new_block