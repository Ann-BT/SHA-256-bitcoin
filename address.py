import base58
from hash_utils import sha256, double_sha256, ripemd160

def create_address(public_key_hex: str) -> str:
    public_key_bytes = bytes.fromhex(public_key_hex)
    pubkey_sha = sha256(public_key_bytes)
    pubkey_ripe = ripemd160(pubkey_sha)

    payload = b'\x00' + pubkey_ripe  # 0x00 for mainnet
    checksum = double_sha256(payload)[:4]
    address = base58.b58encode(payload + checksum).decode()
    return address
