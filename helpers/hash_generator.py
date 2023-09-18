import hashlib


class HashGenerator:
    def generate_hash(self, long_url: str) -> str:
        sha256_hash = hashlib.sha256(long_url.encode()).hexdigest()[:8]
        return sha256_hash
