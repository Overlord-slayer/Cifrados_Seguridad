import random
import string

def generar_llave(longitud):
    # Generar una llave aleatoria de caracteres ASCII
    llave = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(longitud))
    return llave

# Ejemplo de uso
longitud = 10
print(generar_llave(longitud))  # Salida: algo como "aB3dE7fG9h"