"""_summary_
    Este documento sirve para poder hacer la version del cifrado afin.
    Este fue mucho mas complicado que los otros, al menos, para la obtencion de informacion
    con su implementacion
    
    Raises:
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_

    @see https://chatgpt.com/share/67a2ba41-867c-800a-a69d-46a1560c94bc
"""

from clean_string import clean_string
import math

def gcd(a: int, b: int) -> int:
    """
    Calcula el máximo común divisor (MCD) usando el algoritmo de Euclides.
    
    :param a: Primer número entero.
    :param b: Segundo número entero.
    :return: El máximo común divisor de a y b.
    """
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a: int, m: int) -> int:
    """
    Calcula el inverso multiplicativo de a módulo m usando el algoritmo de Euclides extendido.
    
    :param a: Número entero para encontrar su inverso multiplicativo.
    :param m: Módulo.
    :return: El inverso multiplicativo de a módulo m, o None si no existe.
    """
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text: str, a: int, b: int) -> str:
    """
    Cifra un texto usando el cifrado afín.
    
    :param text: Texto de entrada a cifrar.
    :param a: Clave de multiplicación (debe ser coprimo con 26).
    :param b: Clave de desplazamiento.
    :return: Texto cifrado.
    :raises ValueError: Si a no es coprimo con 26.
    """
    if gcd(a, 26) != 1:
        raise ValueError("a debe ser coprimo con 26.")
    
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            x = ord(char.lower()) - ord('a')
            encrypted_char = (a * x + b) % 26
            encrypted_text += chr(encrypted_char + ord('a'))
        else:
            encrypted_text += char  # Mantiene espacios y otros caracteres sin cifrar
    return encrypted_text

def affine_decrypt(text: str, a: int, b: int) -> str:
    """
    Descifra un texto cifrado con el cifrado afín.
    
    :param text: Texto cifrado de entrada.
    :param a: Clave de multiplicación usada en el cifrado.
    :param b: Clave de desplazamiento usada en el cifrado.
    :return: Texto descifrado.
    :raises ValueError: Si no existe inverso multiplicativo para a.
    """
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("No existe inverso multiplicativo para a.")
    
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            y = ord(char.lower()) - ord('a')
            decrypted_char = (a_inv * (y - b)) % 26
            decrypted_text += chr(decrypted_char + ord('a'))
        else:
            decrypted_text += char  # Mantiene espacios y otros caracteres sin cifrar
    return decrypted_text

if __name__ == "__main__":
    # Ejemplo de uso
    text: str = "prueba mega texto"
    text_sin_espacios = clean_string(text)
    a: int = 5
    b: int = 8  # Claves (a debe ser coprimo con 26)

    encrypted: str = affine_encrypt(text_sin_espacios, a, b)
    decrypted: str = affine_decrypt(encrypted, a, b)

    print(f"Texto original: {text_sin_espacios}, con espacios -> {text}")
    print(f"Texto cifrado: {encrypted}")
    print(f"Texto descifrado: {decrypted}, con espacios -> {text}")
