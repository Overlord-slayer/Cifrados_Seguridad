"""_summary_
Este archivo sirve para obtener la frecuencia en que se repiten los caracteres
en una oracion/plabara/texto. En este caso, solo se hace conteo y se grafica de manera simple
como esta distribuida. Servira para la parte B del lab
Returns:
    _type_: _description_
"""
import matplotlib.pyplot as plt
from clean_string import clean_string

def characters_frequency(cadena: str):
    """
    Cuenta la frecuencia de cada carácter en una cadena.

    Args:
        cadena (str): La cadena de la cual se contarán los caracteres.

    Returns:
        dict: Un diccionario donde las claves son los caracteres y los valores son sus frecuencias.
    """
    # Diccionario para almacenar la frecuencia de cada carácter
    frequency = {}

    # Iterar sobre cada carácter en la cadena
    for char in cadena:
        # Si el carácter ya está en el diccionario, incrementar su contador
        if char in frequency:
            frequency[char] += 1
        # Si no está en el diccionario, agregarlo con un contador de 1
        else:
            frequency[char] = 1

    return frequency

def graph(frequency: dict):
    """
    Genera un gráfico de barras que muestra la frecuencia de caracteres.
    
    Args:
        frequency (dict): Un diccionario donde las claves son caracteres (str) y los valores
                          son las frecuencias (int) de aparición de cada carácter.
    
    Returns:
        None: La función no retorna ningún valor, pero muestra un gráfico de barras.
    
    Example:
        >>> frequency = {'a': 10, 'b': 5, 'c': 3}
        >>> graph(frequency)
        # Muestra un gráfico de barras con los caracteres 'a', 'b', 'c' y sus frecuencias.
    """
    letras = list(frequency.keys())
    frecuencias = list(frequency.values())
    plt.bar(letras, frecuencias)
    plt.title("Frecuencia de caracteres")
    plt.xlabel("Caracteres")
    plt.ylabel("Apariciones")
    plt.show()


if __name__ == "__main__":
    # Ejemplo de uso
    cadena = "hola papa"
    cadena_sin_espacios = clean_string(cadena)
    result = characters_frequency(cadena_sin_espacios)
    print("Frecuencia de caracteres:")
    for char, count in result.items():
        print(f"'{char}': {count}")
    graph(result)