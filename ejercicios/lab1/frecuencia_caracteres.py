"""_summary_
Este archivo sirve para obtener la frecuencia en que se repiten los caracteres
en una oracion/plabara/texto. En este caso, solo se hace conteo y se grafica de manera simple
como esta distribuida. Servira para la parte B del lab
Returns:
    _type_: _description_

@see https://chatgpt.com/share/67a2c125-33bc-8001-8b61-455de4cfc96d
"""
import matplotlib.pyplot as plt
from clean_string import clean_string

def characters_frequency(cadena: str):
    """
    Cuenta la frecuencia de cada carácter en una cadena.
    
    Args:
        cadena (str): La cadena de entrada de la cual se contarán los caracteres.
    
    Returns:
        dict: Un diccionario con la frecuencia de cada carácter.
    """
    frequency = {}
    for char in cadena:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def calculate_probabilities(frequency: dict):
    """
    Calcula la distribución de probabilidades de los caracteres.
    
    Args:
        frequency (dict): Un diccionario con la frecuencia de cada carácter.
    
    Returns:
        dict: Un diccionario con la probabilidad de cada carácter.
    """
    total_chars = sum(frequency.values())
    probabilities = {char: count / total_chars for char, count in frequency.items()}
    return probabilities

def compare_with_theoretical(actual_probs: dict):
    """
    Compara la distribución observada con la teórica del español.
    
    Args:
        actual_probs (dict): Un diccionario con las probabilidades observadas de los caracteres.
    
    Returns:
        tuple: Dos diccionarios, uno con las probabilidades observadas y otro con las teóricas.
    """
    theoretical_probs = {
        'a': 0.1253, 'b': 0.0142, 'c': 0.0468, 'd': 0.0586, 'e': 0.1368, 'f': 0.0069,
        'g': 0.0101, 'h': 0.0070, 'i': 0.0625, 'j': 0.0044, 'k': 0.0002, 'l': 0.0497,
        'm': 0.0315, 'n': 0.0671, 'ñ': 0.0031, 'o': 0.0868, 'p': 0.0251, 'q': 0.0088, 'r': 0.0687,
        's': 0.0798, 't': 0.0463, 'u': 0.0393, 'v': 0.0090, 'w': 0.0001, 'x': 0.0022,
        'y': 0.0090, 'z': 0.0052
    }
    all_chars = set(theoretical_probs.keys()).union(set(actual_probs.keys()))
    actual_probs = {char: actual_probs.get(char, 0) for char in all_chars}
    return actual_probs, theoretical_probs

def plot_comparison(actual_probs: dict, theoretical_probs: dict):
    """
    Genera un gráfico comparativo entre la distribución real y la teórica.
    
    Args:
        actual_probs (dict): Un diccionario con las probabilidades observadas.
        theoretical_probs (dict): Un diccionario con las probabilidades teóricas del español.
    """
    chars = sorted(actual_probs.keys())
    actual_values = [actual_probs[char] for char in chars]
    theoretical_values = [theoretical_probs.get(char, 0) for char in chars]
    
    x = range(len(chars))
    plt.figure(figsize=(12, 6))
    plt.bar(x, actual_values, width=0.4, label="Observado", align='center')
    plt.bar(x, theoretical_values, width=0.4, label="Teórico", align='edge')
    plt.xticks(ticks=x, labels=chars)
    plt.xlabel("Caracteres")
    plt.ylabel("Probabilidad")
    plt.title("Comparación de Distribución de Caracteres")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    cadena = "hola papa"
    cadena_sin_espacios = clean_string(cadena)
    frequency = characters_frequency(cadena_sin_espacios)
    probabilities = calculate_probabilities(frequency)
    actual_probs, theoretical_probs = compare_with_theoretical(probabilities)
    print("Distribución de Probabilidades Observada:")
    for char, prob in actual_probs.items():
        print(f"'{char}': {prob:.4f}")
    plot_comparison(actual_probs, theoretical_probs)