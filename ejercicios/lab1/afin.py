from clean_string import clean_string

def gcd(a: int, b: int) -> int:
    """
    Calcula el máximo común divisor (GCD) de dos números.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: El máximo común divisor de a y b.
    """
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a: int, m: int) -> int:
    """
    Calcula el inverso modular de a módulo m.

    Args:
        a (int): Número del cual se calculará el inverso.
        m (int): Módulo.

    Returns:
        int: El inverso modular de a módulo m.
    """
    if gcd(a, m) != 1:
        raise ValueError("a y m deben ser coprimos (GCD = 1).")
    
    # Algoritmo extendido de Euclides para encontrar el inverso modular
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = m // a, m % a
        m, a = a, r
        x, y, u, v = u, v, x - q * u, y - q * v
    
    return x % m


def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    """
    Cifra un texto usando el cifrado afín.

    Args:
        plaintext (str): Texto plano a cifrar.
        a (int): Clave a (debe ser coprimo con 26).
        b (int): Clave b.

    Returns:
        str: Texto cifrado.
    """
    if gcd(a, 26) != 1:
        raise ValueError("a y 26 deben ser coprimos (GCD = 1).")
    
    ciphertext = ""
    for char in plaintext:
        if char.islower():
            # Cifrar letras minúsculas
            P = ord(char) - ord('a')
            C = (a * P + b) % 26
            ciphertext += chr(C + ord('a'))
        elif char.isupper():
            # Cifrar letras mayúsculas
            P = ord(char) - ord('A')
            C = (a * P + b) % 26
            ciphertext += chr(C + ord('A'))
        else:
            # Mantener otros caracteres sin cambios
            ciphertext += char
    return ciphertext


def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    """
    Descifra un texto cifrado usando el cifrado afín.

    Args:
        ciphertext (str): Texto cifrado.
        a (int): Clave a (debe ser coprimo con 26).
        b (int): Clave b.

    Returns:
        str: Texto plano descifrado.
    """
    if gcd(a, 26) != 1:
        raise ValueError("a y 26 deben ser coprimos (GCD = 1).")
    
    a_inv = mod_inverse(a, 26)
    plaintext = ""
    for char in ciphertext:
        if char.islower():
            # Descifrar letras minúsculas
            C = ord(char) - ord('a')
            P = (a_inv * (C - b)) % 26
            plaintext += chr(P + ord('a'))
        elif char.isupper():
            # Descifrar letras mayúsculas
            C = ord(char) - ord('A')
            P = (a_inv * (C - b)) % 26
            plaintext += chr(P + ord('A'))
        else:
            # Mantener otros caracteres sin cambios
            plaintext += char
    return plaintext


# Ejemplo de uso
if __name__ == "__main__":
    plaintext = "Hola Mundo"
    justText = clean_string(plaintext)
    a, b = 5, 8  # Claves del cifrado afín

    # Cifrar
    ciphertext = affine_encrypt(justText, a, b)
    print("Texto cifrado:", ciphertext)

    # Descifrar
    decrypted_text = affine_decrypt(ciphertext, a, b)
    print("Texto descifrado:", decrypted_text)