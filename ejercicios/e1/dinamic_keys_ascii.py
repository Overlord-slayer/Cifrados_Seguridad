import random
import string

def generar_llave(longitud):
    """
    Genera una clave aleatoria compuesta por caracteres ASCII (letras mayúsculas, minúsculas y dígitos).

    Esta función crea una clave de una longitud específica, utilizando caracteres aleatorios
    seleccionados de entre letras mayúsculas, minúsculas y dígitos.

    Parámetros:
    -----------
    longitud : int
        La longitud de la clave que se desea generar.

    Retorna:
    --------
    str
        Una cadena que representa la clave generada aleatoriamente.

    Ejemplo:
    --------
    >>> longitud = 10
    >>> generar_llave(longitud)
    'aB3dE7fG9h'
    """
    # Generar una llave aleatoria de caracteres ASCII
    llave = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(longitud))
    return llave

# Ejemplo de uso
longitud = 10
print(generar_llave(longitud))  # Salida: algo como "aB3dE7fG9h"