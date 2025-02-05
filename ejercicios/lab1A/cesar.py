"""_summary_
    
    Este codigo sirver para la implementacion del cifrado cesar, se base en la informacion obtenida en el
    video colocado.

    El cifrado cesar consta de la cadena, y de una clave numerica, que representa la cantidad de corridas para
    el texto. En este caso, si es 'a' y es una clave de '3', se corre de 'a' -> 'd', pues se suman esas posiciones
    de corrida. Algo a tomar en cuanta, es que no se coloco un limite de corridas, lo cual puede ser en catastrofico,
    pero se piensa que si se hace tal cosa, simplemente hara un cifrado segun la cantidad de caracteres del alfabeto.
    En este caso, si se coloca 90, el mod de 90 con la cantidad de 27 es 9, con lo cual, la posicion seria j, pues es
    la novena letra del alfabeto de Spanish. El corrimiento se inicia desde la siguiente letra a la que se esta cifrando
    es decir, si es de 3 el numero clave y la letra/caracter a cifrar es 3, no se cuenta desde la posicion de la 'a',
    sino desde 'b', con lo cual, resultaria en 'd' como el valor del cifrado.

    Returns:
        _type_: _description_

        
    @see https://youtu.be/4OmhdF89TRE?si=KYAJVfHIXSaBTih8
"""

from clean_string import clean_string


letras = 'abcdefghijklmnñopqrstuvwxyz'

def main():
    """
    Función principal que maneja la interacción con el usuario.
    Solicita una cadena y una clave numérica, realiza el cifrado y descifrado usando el cifrado César,
    y muestra los resultados.
    """
    cadena = input("Ingrese la cadena a cifrar: ").lower()
    numero_clave = int(input("Ingrese la clave numerica: "))
    cadena_sin_espacioes = clean_string(cadena)
    texto_cifrado = cifrar_cesar(cadena_sin_espacioes, numero_clave)
    print(f"Cadena '{cadena}', sin espacios '{cadena_sin_espacioes}', con clave '{numero_clave}', se cifra como: '{texto_cifrado}'")
    texto_descifrado = descifrar_cesar(texto_cifrado, numero_clave)
    print(
        f"Cadena a descifrar: '{texto_cifrado}', con clave '{numero_clave}', resulta en '{texto_descifrado}', deberia ser {cadena_sin_espacioes} con espacios -> '{cadena}'"
        )

def cifrar_cesar(cadena: str, numero_clave: int):
    """
    Cifra una cadena utilizando el cifrado César.

    Args:
        cadena (str): La cadena de texto a cifrar.
        numero_clave (int): La clave numérica para el cifrado (desplazamiento).

    Returns:
        str: El texto cifrado.
    """
    texto_cifrado = ""
    # Cifrado de caracter por caracter
    for letra in cadena:
        # Posicion donde se encuentra la letra, suma de la posicion de la misma con la clave
        suma = letras.find(letra) + numero_clave
        # aplicar modulo, segun la cantidad de elementos del alfabeto
        modulo = int(suma) % len(letras)
        # el letras[modulo] es la posicion de la letra que sirve para cifrar
        texto_cifrado = texto_cifrado + str(letras[modulo])
    return texto_cifrado

def descifrar_cesar(cadena: str, numero_clave:int):
    """
    Descifra una cadena cifrada utilizando el cifrado César.

    Args:
        cadena (str): La cadena de texto cifrado.
        numero_clave (int): La clave numérica para el descifrado (desplazamiento).

    Returns:
        str: El texto descifrado.
    """
    texto_descifrado = ""
    # Cifrado de caracter por caracter
    for letra in cadena:
        # Posicion donde se encuentra la letra, suma de la posicion de la misma con la clave.
        suma = letras.find(letra) - numero_clave
        # aplicar modulo, segun la cantidad de elementos del alfabeto
        modulo = int(suma) % len(letras)
        # el letras[modulo] es la posicion de la letra que sirve para cifrar
        texto_descifrado = texto_descifrado + str(letras[modulo])
    return texto_descifrado


if __name__ == "__main__":
    main()
    print(90 % len(letras))