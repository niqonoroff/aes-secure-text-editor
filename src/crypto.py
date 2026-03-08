import os
from argon2.low_level import hash_secret_raw, Type
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Размеры служебных данных
SALT_SIZE = 32
NONCE_SIZE = 12
ARGON_TIME = 8
ARGON_MEMORY = 512 * 1024
ARGON_PARALLELISM = 4
KEY_LENGTH = 32

# Превращение пароля в криптографический ключ
def derive_key(password: str, salt: bytes) -> bytes:
    return hash_secret_raw(
        secret=password.encode("utf-8"),
        salt=salt,
        time_cost=ARGON_TIME,
        memory_cost=ARGON_MEMORY,
        parallelism=ARGON_PARALLELISM,
        hash_len=KEY_LENGTH,
        type=Type.ID
    )

# Шифрование текста
def encrypt_text(plaintext: str, password: str) -> bytes:
    salt = os.urandom(SALT_SIZE) # Уникальный ключ для каждого файла
    nonce = os.urandom(NONCE_SIZE) # Уникальное шифрование для каждого вызова
    key = derive_key(password, salt) # пароль -> ключ
    aes = AESGCM(key)
    ciphertext = aes.encrypt(nonce, plaintext.encode("utf-8"), None)
    return b"NQ01" + salt + nonce + ciphertext

# Расшифровка текста
def dectypt_text(blob: bytes, password: str) -> str:
    if blob[:4] != b"NQ01":
        raise ValueError("Неверный формат файла")
    salt = blob[4:4+SALT_SIZE]
    nonce = blob[4+SALT_SIZE:4+SALT_SIZE+NONCE_SIZE]
    ciphertext = blob[4+SALT_SIZE+NONCE_SIZE:]
    key = derive_key(password, salt)
    aes = AESGCM(key)
    plaintext = aes.decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")