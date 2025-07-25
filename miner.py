import time

TARGET_BLOCK_TIME = 10  # seconds (giả lập)

def mine_block(block):
    prefix = "0" * block.difficulty
    start = time.time()
    while True:
        hash_result = block.compute_hash()
        if hash_result.startswith(prefix):
            block.hash = hash_result
            break
        block.nonce += 1
    end = time.time()
    elapsed = round(end - start, 2)
    print(f"⛏️ Mining time: {elapsed}s")
    return elapsed

def adjust_difficulty(previous_time, block_time, current_difficulty):
    if block_time < previous_time * 0.5:
        return current_difficulty + 1
    elif block_time > previous_time * 1.5:
        return max(1, current_difficulty - 1)
    return current_difficulty
