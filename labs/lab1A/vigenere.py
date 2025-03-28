from clean_string import clean_string
"""
En este caso, se toma en cuenta que es mediante una matriz, no se hace como matriz
pero como una sopa de palabras, se tiene una tabla de la a-z, vertical y horizontalmente
ejemplo
abcdefg
bcdefgh
cdefghi
defghij
efghijk
fghijkl
ghijklm

donde las columnas son la entrada de texto plano. Las filas, la entrada clave

@see https://youtu.be/SkJcmCaHqS0?si=m9n2Tn5-DfrGV1u3
@see https://youtu.be/XT6zIHXhFO4?si=DbbSzhVA_12lCAXp
"""
letras = 'abcdefghijklmnñopqrstuvwxyz'

def main():
    """
    Función principal que maneja la interacción con el usuario.
    Solicita una cadena y una clave, realiza el cifrado y descifrado usando el cifrado Vigenère,
    y muestra los resultados.
    """
    cadena = input("Ingrese la cadena a cifrar: ")
    cadena_sin_espacios = clean_string(cadena)
    clave = input("Ingrese la clave a utilizar para el cifrado: ")
    texto_cifrado = cifrar(cadena_sin_espacios.lower(), clave.lower())
    print(f"Texto original '{cadena}' sin espacioes -> '{cadena_sin_espacios}'. Clave a utilizar: '{clave}' -> Texto cifrado: '{texto_cifrado}'")
    texto_descifrado = descifrar(texto_cifrado, clave)
    print(f"Con la clave: '{clave}', el texto cifrado '{texto_cifrado}' se descifra: '{texto_descifrado}', deberia ser igual a '{cadena}', sin espacios -> {cadena_sin_espacios}")


def cifrar(cadena: str, clave: str):
    """
    Cifra una cadena utilizando el cifrado Vigenère.

    Args:
        cadena (str): La cadena de texto a cifrar.
        clave (str): La clave para el cifrado.

    Returns:
        str: El texto cifrado.
    """
    texto_cifrar = ""
    i = 0
    for letra in cadena:
        # Buscar la posicion de la letra, + posicion de la clave, pero si es menor, se hace mod, para que cubra los caracteres faltantes
        suma = letras.find(letra) + letras.find(clave[i % len(clave)]) # Usar la clave cíclicamente
        # modulo con el alfabeto
        modulo = int(suma) % len(letras)
        
        texto_cifrar = texto_cifrar + str(letras[modulo])
        i=i+1
    return texto_cifrar

def descifrar(cadena: str, clave: str):
    """
    Descifra una cadena cifrada utilizando el cifrado Vigenère.

    Args:
        cadena (str): La cadena de texto cifrado.
        clave (str): La clave para el descifrado.

    Returns:
        str: El texto descifrado.
    """
    texto_cifrar = ""
    i = 0
    for letra in cadena:
        #
        suma = letras.find(letra) - letras.find(clave[i % len(clave)])
        modulo = int(suma) % len(letras)
        texto_cifrar = texto_cifrar + str(letras[modulo])
        i=i+1
    return texto_cifrar


if __name__ == "__main__":
    main()
    print(len(letras))
