import time
import unittest

def simple_prng(seed, length):
    """Genera un keystream pseudoaleatorio usando un PRNG propio."""
    state = seed
    keystream = []
    for _ in range(length):
        state = (state * 1103515245 + 12345) & 0x7FFFFFFF  # LCG
        keystream.append(state % 256)
    return keystream

def generate_keystream(length, seed=None):
    """Genera un keystream pseudoaleatorio de la misma longitud que el mensaje."""
    if seed is None:
        seed = int(time.time())  # Usar el tiempo actual como semilla por defecto
    return simple_prng(seed, length)

def encrypt(plaintext, seed=None):
    """Cifra el texto plano usando XOR con el keystream generado."""
    plaintext_bytes = plaintext.encode()
    keystream = generate_keystream(len(plaintext_bytes), seed)
    ciphertext = bytes([p ^ k for p, k in zip(plaintext_bytes, keystream)])
    return ciphertext

def decrypt(ciphertext, seed):
    """Descifra el texto cifrado usando XOR con el mismo keystream."""
    keystream = generate_keystream(len(ciphertext), seed)
    plaintext_bytes = bytes([c ^ k for c, k in zip(ciphertext, keystream)])
    return plaintext_bytes.decode()

# Ejemplo de uso
if __name__ == "__main__":
    seed = 1234  # Se puede modificar para pruebas
    mensaje = "Hola, mundo!"

    # Cifrado
    cifrado = encrypt(mensaje, seed)
    print("Texto Cifrado:", cifrado)

    # Descifrado
    descifrado = decrypt(cifrado, seed)
    print("Texto Descifrado:", descifrado)

    # Pruebas unitarias
    class TestXOREncryption(unittest.TestCase):
        def test_encryption_decryption(self):
            message = "Prueba de cifrado"
            seed = 5678
            ciphertext = encrypt(message, seed)
            decrypted_message = decrypt(ciphertext, seed)
            self.assertEqual(decrypted_message, message)
    
    unittest.main()
