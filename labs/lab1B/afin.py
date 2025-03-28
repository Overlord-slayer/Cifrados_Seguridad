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

import math
import matplotlib.pyplot as plt
from collections import Counter

def gcd(a: int, b: int) -> int:
    """
    Calcula el Máximo Común Divisor (MCD) de dos números enteros utilizando el algoritmo de Euclides.

    Args:
        a (int): Primer número entero.
        b (int): Segundo número entero.

    Returns:
        int: El MCD de los números a y b.
    """
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a: int, m: int) -> int:
    """
    Calcula el inverso multiplicativo de un número `a` en módulo `m` mediante prueba y error.

    Args:
        a (int): El número al que se le busca el inverso.
        m (int): El módulo.

    Returns:
        int: El inverso multiplicativo de `a` módulo `m`, o None si no existe.
    """
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_decrypt(text: str, a: int, b: int) -> str:
    """
    Desencripta un texto cifrado con el cifrado afín utilizando los parámetros `a` y `b`.

    Args:
        text (str): Texto cifrado.
        a (int): Parámetro 'a' del cifrado afín.
        b (int): Parámetro 'b' del cifrado afín.

    Returns:
        str: Texto desencriptado.

    Raises:
        ValueError: Si no existe el inverso multiplicativo de `a` en módulo 26.
    """
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"No existe inverso multiplicativo para a={a}.")
    
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            y = ord(char.lower()) - ord('a')
            decrypted_char = (a_inv * (y - b)) % 26
            decrypted_text += chr(decrypted_char + ord('a'))
        else:
            decrypted_text += char  # Mantiene espacios y otros caracteres
    return decrypted_text

def characters_frequency(text: str):
    """
    Calcula la frecuencia de aparición de las letras en un texto.

    Args:
        text (str): Texto del que se calcularán las frecuencias.

    Returns:
        dict: Un diccionario con las frecuencias de las letras en el texto.
    """
    frequency = Counter(text)
    total_chars = sum(frequency.values())
    return {char: count / total_chars for char, count in frequency.items() if char.isalpha()}

def compare_frequencies(actual_freq: dict, theoretical_freq: dict):
    """
    Compara las frecuencias reales de un texto con las frecuencias teóricas utilizando la distancia Euclidiana.

    Args:
        actual_freq (dict): Frecuencias reales del texto.
        theoretical_freq (dict): Frecuencias teóricas de las letras.

    Returns:
        float: La diferencia entre las frecuencias reales y las teóricas, medida por la distancia Euclidiana.
    """
    all_chars = set(theoretical_freq.keys()).union(set(actual_freq.keys()))
    actual_freq = {char: actual_freq.get(char, 0) for char in all_chars}
    theoretical_freq = {char: theoretical_freq.get(char, 0) for char in all_chars}
    return math.sqrt(sum((actual_freq[char] - theoretical_freq[char]) ** 2 for char in all_chars))

def find_best_decryption(ciphertext: str):
    """
    Encuentra la mejor desencriptación para un texto cifrado utilizando el cifrado afín, probando todos los valores posibles
    de `a` y `b` que son válidos para la alfabetización en español.

    Args:
        ciphertext (str): El texto cifrado.

    Returns:
        tuple: Un tuple con el texto desencriptado más probable, y los valores de `a` y `b` que producen la mejor coincidencia.
    """
    theoretical_freq = {
        'a': 0.1253, 'b': 0.0142, 'c': 0.0468, 'd': 0.0586, 'e': 0.1368, 'f': 0.0069,
        'g': 0.0101, 'h': 0.0070, 'i': 0.0625, 'j': 0.0044, 'k': 0.0002, 'l': 0.0497,
        'm': 0.0315, 'n': 0.0671, 'ñ': 0.0031, 'o': 0.0868, 'p': 0.0251, 'q': 0.0088, 'r': 0.0687,
        's': 0.0798, 't': 0.0463, 'u': 0.0393, 'v': 0.0090, 'w': 0.0001, 'x': 0.0022,
        'y': 0.0090, 'z': 0.0052
    }
    
    valid_a_values = [a for a in range(1, 17) if gcd(a, 26) == 1]
    valid_b_values = range(1, 17)
    
    best_text = None
    best_score = float("inf")
    best_a, best_b = None, None
    
    for a in valid_a_values:
        for b in valid_b_values:
            try:
                decrypted_text = affine_decrypt(ciphertext, a, b)
                actual_freq = characters_frequency(decrypted_text)
                score = compare_frequencies(actual_freq, theoretical_freq)
                
                if score < best_score:
                    best_score = score
                    best_text = decrypted_text
                    best_a, best_b = a, b
            except ValueError:
                continue
    
    return best_text, best_a, best_b

if __name__ == "__main__":
    """
    Lee el contenido de un archivo cifrado, intenta desencriptarlo usando el cifrado afín,
    y muestra la mejor desencriptación encontrada con sus parámetros.
    """
    ruta_archivo = "./Cifrados/afines.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
            print("Contenido cifrado:")
            print(contenido)
            print("\nBuscando la mejor desencriptación...")
            best_text, best_a, best_b = find_best_decryption(contenido)
            print(f"\nMejor desencriptación encontrada con a={best_a}, b={best_b}:")
            print(best_text)
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
