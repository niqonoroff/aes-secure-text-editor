import os
from argon2.low_level import hash_secret_raw, Type
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Размеры служебных данных
ARGON_TIME = 8
ARGON_MEMORY = 512 * 1024
ARGON_PARALLELISM = 4
SALT_SIZE = 32
NONCE_SIZE = 12
KEY_LENGTH = 32

# Превращение пароля в криптографический ключ
def derive_key(password: str, salt: bytes,
               time_cost: int,
               memory_cost: int,
               parallelism: int) -> bytes:
    return hash_secret_raw(
        secret=password.encode("utf-8"),
        salt=salt,
        time_cost=time_cost,
        memory_cost=memory_cost,
        parallelism=parallelism,
        hash_len=KEY_LENGTH,
        type=Type.ID
    )

# Шифрование текста
def encrypt_text(plaintext: str, password: str,
                 argon_time: int,
                 argon_memory: int,
                 argon_parallel: int,
                 salt_size: int,
                 nonce_size: int) -> bytes:

    salt = os.urandom(salt_size)
    nonce = os.urandom(nonce_size)
    key = derive_key(
        password,
        salt,
        argon_time,
        argon_memory,
        argon_parallel
    )
    aes = AESGCM(key)
    ciphertext = aes.encrypt(nonce, plaintext.encode("utf-8"), None)
    return b"NQ01" + salt + nonce + ciphertext

# Расшифровка текста
def dectypt_text(blob: bytes, password: str,
                 argon_time: int,
                 argon_memory: int,
                 argon_parallel: int,
                 salt_size: int,
                 nonce_size: int) -> str:
    if blob[:4] != b"NQ01":
        raise ValueError("Неверный формат файла")
    salt = blob[4:4 + salt_size]
    nonce = blob[4 + salt_size:4 + salt_size + nonce_size]
    ciphertext = blob[4 + salt_size + nonce_size:]
    key = derive_key(
        password,
        salt,
        argon_time,
        argon_memory,
        argon_parallel
    )
    aes = AESGCM(key)
    plaintext = aes.decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")