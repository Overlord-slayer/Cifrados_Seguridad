import unittest
from xor_cipher_prng import decrypt, encrypt

class TestXOREncryption(unittest.TestCase):
    def test_encryption_decryption(self):
        """Prueba que el mensaje cifrado y luego descifrado sea igual al original."""
        message = "Prueba de cifrado"
        seed = 5678
        ciphertext = encrypt(message, seed)
        decrypted_message = decrypt(ciphertext, seed)
        self.assertEqual(decrypted_message, message)
    
    def test_different_keys_produce_different_ciphertext(self):
        """Prueba que cambiar la clave genera un texto cifrado diferente."""
        message = "Texto de prueba"
        seed1 = 1234
        seed2 = 5678
        ciphertext1 = encrypt(message, seed1)
        ciphertext2 = encrypt(message, seed2)
        self.assertNotEqual(ciphertext1, ciphertext2)
    
    def test_keystream_reuse_vulnerability(self):
        """Prueba la vulnerabilidad de reutilización del keystream."""
        message1 = "Mensaje uno"
        message2 = "Mensaje dos"
        seed = 9999
        ciphertext1 = encrypt(message1, seed)
        ciphertext2 = encrypt(message2, seed)
        xor_result = bytes(a ^ b for a, b in zip(ciphertext1, ciphertext2))
        self.assertNotEqual(ciphertext1, ciphertext2)  # Mensajes cifrados deben ser diferentes
        self.assertNotEqual(xor_result, b"\x00" * len(xor_result))  # Evita que se anulen
    
    def test_keystream_length_matches_message(self):
        """Prueba que el keystream tenga al menos la longitud del mensaje."""
        message = "Longitud segura"
        seed = 4321
        ciphertext = encrypt(message, seed)
        self.assertEqual(len(ciphertext), len(message))
    
    def test_secure_keystream_generation(self):
        """Prueba que el keystream generado sea diferente en ejecuciones distintas si la semilla cambia."""
        message = "Seguridad"
        seed1 = 1111
        seed2 = 2222
        ciphertext1 = encrypt(message, seed1)
        ciphertext2 = encrypt(message, seed2)
        self.assertNotEqual(ciphertext1, ciphertext2)

if __name__ == "__main__":
    unittest.main()
