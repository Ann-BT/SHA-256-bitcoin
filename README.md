## 1. Introduction

### 1.1 What is SHA-256

SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function from the SHA-2 family, designed by the U.S. National Security Agency in 2001. It produces a fixed 256-bit (32-byte) hash from arbitrary-length input data, represented as 64 hexadecimal characters.

### 1.2 Why SHA-256 is Used in Bitcoin

**Core Security Properties**

- **One-Way Function:** Computationally irreversible — impossible to determine input from hash output
- **Avalanche Effect:** Minor input changes produce dramatically different outputs
- **Collision Resistance:** Finding two inputs with identical outputs is computationally infeasible (2^128 operations required)
- **Preimage Resistance:** Cannot find input that produces a specific hash

**Practical Advantages**

- Proven security track record since 2001
- Hardware optimization potential for ASIC mining
- NIST standardization and institutional trust
- No practical attacks exist against full 64-round SHA-256 as of 2025

---

## 2. SHA-256 Algorithm Architecture

### 2.1 Merkle-Damgaard Construction

SHA-256 processes variable-length inputs through systematic preprocessing:

1. **Message Padding:** Input padded to 448 mod 512 bits
2. **Length Appending:** 64-bit length field added, creating 512-bit multiples
3. **Block Processing:** Each 512-bit block undergoes 64 compression rounds

### 2.2 Compression Function

- Uses eight 32-bit working variables (A–H) initialized with constants from square roots of the first 8 primes.
- Boolean functions:
    - `Ch(x,y,z) = (x ∧ y) ⊕ (¬x ∧ z)`
    - `Maj(x,y,z) = (x ∧ y) ⊕ (x ∧ z) ⊕ (y ∧ z)`
- Bit manipulation: XOR, AND, shifts
- Round constants: Derived from cube roots of the first 64 primes

---

## 3. Bitcoin Implementation of SHA-256

### 3.1 Computing SHA-256 Hashes in Python

- `text.encode()`: Converts text to bytes
- `hashlib.sha256()`: Computes SHA-256 hash
- `.digest()`: Returns raw binary
- `.hexdigest()`: Returns human-readable 64-character hex string

### 3.2 Proof-of-Work Mining

**Process:**

1. Create block headers (80 bytes) with version, previous hash, Merkle root, timestamp, difficulty, nonce
2. Compute: `Hash = SHA-256(SHA-256(block_header))`
3. Check if hash meets difficulty (leading zeros)
4. If not, increment nonce and retry

**Security:**

- Difficulty: ~75–80 leading zero bits
- Network: 10¹⁸+ SHA-256 ops/sec
- Difficulty adjusts every 2,016 blocks

### 3.3 Block Hashing and Chain Integrity

- **Double Hashing**: `SHA-256(SHA-256(80-byte header))`
- **Immutable Chain**: Previous block’s hash in header ensures cryptographic linkage
- **Tamper Evidence**: Changes break hash chain

### 3.4 Bitcoin Address Generation

**Steps:**

1. Generate ECDSA public key
2. SHA-256 on public key
3. RIPEMD-160 on SHA-256 result
4. Add version byte (0x00)
5. Double SHA-256 for checksum (first 4 bytes)
6. Encode with Base58Check

**Security:**

- Dual hashing = algorithm diversification
- Checksum = error detection
- Address = privacy + quantum resistance

---

## 4. Design and Implementation

### 4.1 System Architecture

**Modules:**

- `hash_utils.py`: Cryptographic functions
- `address.py`: Address generation
- `block.py`: Block structure & Merkle trees
- `miner.py`: Mining
- `main.py`: Blockchain simulation

### 4.2 Implementation Details

### `hash_utils.py`

- `sha256()`: Single hash
- `double_sha256()`: Bitcoin-style hash
- `ripemd160()`: For address generation

### `address.py`

- `create_address()` uses:
    - SHA-256 → RIPEMD-160 → Add version → Double SHA-256 → Base58Check
- Example Output: `1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH`

### `block.py`

- `Transaction` class: sender, receiver, amount
- `calculate_merkle_root()` builds hash tree
- `Block` class: Contains metadata and hash

### `miner.py`

- `mine_block()`: Brute-force nonce
- `adjust_difficulty()`: Adapts based on block time

### `main.py`

- Creates Genesis block
- Processes transactions
- Adjusts difficulty
- Simulates mining performance

**SHA-256 Use Cases:**

- Block mining
- Address hashing
- Error detection
- Merkle tree
- Chain linkage

---

## 5. Experiment, Data Collection

| Block # | Mining Time (s) | Difficulty | Nonce | BTC Transferred |
| --- | --- | --- | --- | --- |
| 0 | 0.02 | 3 | 1688 | 0.0 (Init) |
| 1 | 0.08 | 4 | 34020 | 3.5 |
| 2 | 1.73 | 5 | 685295 | 0.6 |
| 3 | 17.22 | 6 | 7130437 | 0.9 |
| 4 | 2.14 | 5 | 874268 | 1.2 |
| 5 | 29.51 | 6 | 12132856 | 1.5 |
| 6 | 3.48 | 5 | 1423319 | 1.8 |
| 7 | 3.22 | 6 | 1320274 | 1.4 |
| 8 | 171.89 | 7 | 67919703 | 1.6 |
| 9 | 39.43 | 6 | 16061181 | 2.7 |
| 10 | 2.32 | 5 | 960320 | 3.0 |
| 11 | 31.85 | 6 | 13047767 | 3.3 |

---

## 6. Analyze Numerical Result

- Mining difficulty causes exponential growth in computation:
    - Difficulty 3 → nonce ~10³
    - Difficulty 7 → nonce >10⁷
- Real-world Bitcoin difficulty ≈ 2⁶⁴ attempts/block.
- Simulation matches theoretical behavior.
- Proof-of-Work security relies on exponential cost of hash generation.

---

## 7. References

1. Narayanan, A., Bonneau, J., Felten, E., Miller, A., & Goldfeder, S. *Bitcoin and Cryptocurrency Technologies*, 2016
2. Nakamoto, S. *Bitcoin: A Peer-to-Peer Electronic Cash System*, 2008
3. [Bitcoin-Wiki – Difficulty](https://en.bitcoin.it/wiki/Difficulty)
4. [Bitcoin.org – How Bitcoin Works](https://bitcoin.org/en/how-bitcoin-works)
5. SHA-256 Algorithm: Characteristics, Steps, and Applications
6. [Simplilearn Tutorial on SHA-256](https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm)
