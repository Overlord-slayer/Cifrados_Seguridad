"""_summary_

@see https://chatgpt.com/share/67bd28ab-4fd4-800b-9152-78195d693a1d

Returns:
    _type_: _description_
"""

import time

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


    # Pruebas manuales con impresión de resultados

    print("\n1. ¿Qué sucede cuando cambias la clave utilizada para generar el keystream?")
    message = "Texto de prueba"
    seed1 = 1234
    seed2 = 5678
    ciphertext1 = encrypt(message, seed1)
    ciphertext2 = encrypt(message, seed2)
    print("   - Cifrado con seed1:", ciphertext1)
    print("   - Cifrado con seed2:", ciphertext2)
    print("   - Son diferentes:", ciphertext1 != ciphertext2)

    print("\n2. ¿Qué riesgos de seguridad existen si reutilizas el mismo keystream para cifrar dos mensajes diferentes?")
    message1 = "Mensaje uno"
    message2 = "Mensaje dos"
    seed = 9999
    ciphertext1 = encrypt(message1, seed)
    ciphertext2 = encrypt(message2, seed)
    xor_result = bytes(a ^ b for a, b in zip(ciphertext1, ciphertext2))
    print("   - Cifrado mensaje 1:", ciphertext1)
    print("   - Cifrado mensaje 2:", ciphertext2)
    print("   - XOR de ambos cifrados:", xor_result)

    print("\n3. ¿Cómo afecta la longitud del keystream a la seguridad del cifrado?")
    message = "Longitud segura"
    seed = 4321
    keystream = generate_keystream(len(message), seed)
    print("   - Mensaje original:", message)
    print("   - Keystream generado:", keystream)
    print("   - Longitud keystream == Longitud mensaje:", len(keystream) == len(message))

    print("\n4. ¿Qué consideraciones debes tener al generar un keystream en un entorno real?")
    message = "Seguridad"
    seed1 = 1111
    seed2 = 2222
    ciphertext1 = encrypt(message, seed1)
    ciphertext2 = encrypt(message, seed2)
    print("   - Cifrado con seed1:", ciphertext1)
    print("   - Cifrado con seed2:", ciphertext2)
    print("   - Son diferentes:", ciphertext1 != ciphertext2)
