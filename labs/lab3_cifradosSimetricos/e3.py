"""
Crypto Benchmark: ChaCha20 vs AES-GCM

Este script compara el rendimiento de los algoritmos de cifrado ChaCha20 y AES-GCM.
Utiliza la biblioteca PyCryptodome para realizar cifrado y descifrado con cada algoritmo
midiendo el tiempo de ejecución.

@version: 1.0
"""

from Crypto.Cipher import ChaCha20, AES
from Crypto.Random import get_random_bytes
import time
import tracemalloc

# Configuración de claves
CHACHA_KEY = b'0123456789abcdef0123456789abcdef'  # Clave de 32 bytes para ChaCha20
AES_KEY = get_random_bytes(32)  # Clave de 256 bits para AES-GCM

def chacha20_encrypt(data: bytes, key: bytes) -> tuple[bytes, bytes]:
    """
    Cifra los datos utilizando el algoritmo ChaCha20.

    @param data: Datos a cifrar en formato bytes.
    @param key: Clave de 32 bytes para ChaCha20.
    @return: Tupla que contiene los datos cifrados y el nonce utilizado para el cifrado.
    """
    cipher = ChaCha20.new(key=key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data, cipher.nonce

def chacha20_decrypt(encrypted_data: bytes, key: bytes, nonce: bytes) -> bytes:
    """
    Descifra los datos cifrados con ChaCha20.

    @param encrypted_data: Datos cifrados en formato bytes.
    @param key: Clave de 32 bytes utilizada para el cifrado.
    @param nonce: Nonce utilizado durante el cifrado.
    @return: Datos descifrados en formato bytes.
    """
    cipher = ChaCha20.new(key=key, nonce=nonce)
    return cipher.decrypt(encrypted_data)

def aes_gcm_encrypt(data: bytes, key: bytes) -> tuple[bytes, bytes, bytes]:
    """
    Cifra los datos utilizando el algoritmo AES en modo GCM.

    @param data: Datos a cifrar en formato bytes.
    @param key: Clave de 32 bytes para AES-GCM.
    @return: Tupla que contiene los datos cifrados, el nonce y el tag de autenticación.
    """
    cipher = AES.new(key, AES.MODE_GCM)
    encrypted_data, tag = cipher.encrypt_and_digest(data)
    return encrypted_data, cipher.nonce, tag

def aes_gcm_decrypt(encrypted_data: bytes, key: bytes, nonce: bytes, tag: bytes) -> bytes:
    """
    Descifra los datos cifrados con AES-GCM.

    @param encrypted_data: Datos cifrados en formato bytes.
    @param key: Clave de 32 bytes utilizada para el cifrado.
    @param nonce: Nonce utilizado durante el cifrado.
    @param tag: Tag de autenticación generado durante el cifrado.
    @return: Datos descifrados en formato bytes.
    @raises ValueError: Si la verificación del tag de autenticación falla.
    """
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(encrypted_data, tag)

# Mensaje de prueba
message = b"Mensaje de prueba para comparar ChaCha20 y AES-GCM" * 1000

# Prueba de ChaCha20
tracemalloc.start()
start_time = time.time()
encrypted_message, nonce = chacha20_encrypt(message, CHACHA_KEY)
chacha_enc_time = time.time() - start_time
current, peak = tracemalloc.get_traced_memory()
chacha_enc_memory = peak - current
tracemalloc.stop()

tracemalloc.start()
start_time = time.time()
decrypted_message = chacha20_decrypt(encrypted_message, CHACHA_KEY, nonce)
chacha_dec_time = time.time() - start_time
current, peak = tracemalloc.get_traced_memory()
chacha_dec_memory = peak - current
tracemalloc.stop()

assert message == decrypted_message, "Error: ChaCha20 no descifró correctamente"

# Prueba de AES-GCM
tracemalloc.start()
start_time = time.time()
aes_encrypted, aes_nonce, aes_tag = aes_gcm_encrypt(message, AES_KEY)
aes_enc_time = time.time() - start_time
current, peak = tracemalloc.get_traced_memory()
aes_enc_memory = peak - current
tracemalloc.stop()

tracemalloc.start()
start_time = time.time()
aes_decrypted = aes_gcm_decrypt(aes_encrypted, AES_KEY, aes_nonce, aes_tag)
aes_dec_time = time.time() - start_time
current, peak = tracemalloc.get_traced_memory()
aes_dec_memory = peak - current
tracemalloc.stop()

assert message == aes_decrypted, "Error: AES-GCM no descifró correctamente"

# Comparación de Resultados
print("ChaCha20:")
print(f"Cifrado - Tiempo: {chacha_enc_time:.6f} s | Memoria: {chacha_enc_memory / 1024:.2f} KB")
print(f"Descifrado - Tiempo: {chacha_dec_time:.6f} s | Memoria: {chacha_dec_memory / 1024:.2f} KB")

print("\nAES-GCM:")
print(f"Cifrado - Tiempo: {aes_enc_time:.6f} s | Memoria: {aes_enc_memory / 1024:.2f} KB")
print(f"Descifrado - Tiempo: {aes_dec_time:.6f} s | Memoria: {aes_dec_memory / 1024:.2f} KB")
