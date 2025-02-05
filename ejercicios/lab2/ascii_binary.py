"""_summary_
    En este caso, sirve para pasar de una cadena a bytes
    @see https://cryptii.com/pipes/text-to-binary
"""

def text_to_bits(text):
    """
    Convierte un texto en su representación binaria de 8 bits por carácter.

    @param text: str - Cadena de texto a convertir.
    @return: str - Representación binaria de la cadena, separada por espacios.

    @example:
        >>> text_to_bits("Hi")
        "01001000 01101001"

    @note:
        - Convierte cada carácter a su valor ASCII.
        - Luego lo representa en binario de 8 bits.
        - Imprime el proceso paso a paso.

    @dependencies:
        - Se requiere la función decimal_to_binary(n) para mostrar la conversión paso a paso.

    """
    bites = []
    # Paso a paso
    for letter in text:
        print(f"Caracter actual: {letter}")
        print(f"Valor ascii: {ord(letter)}")
        valor_ascii = ord(letter)
        print(decimal_to_binary(valor_ascii)) 
        # Esta es la version mas facil, con herramiesntas de python       
        bites.append(format(ord(letter), '08b'))
    return ' '.join(bites)

def decimal_to_binary(n):
    """
    Convierte un número decimal a su representación en binario de 8 bits.

    @param n: int - Número decimal positivo a convertir.
    @return: str - Representación binaria en formato de 8 bits.

    @example:
        >>> decimal_to_binary(72)
        "01001000"

    @note:
        - Usa divisiones sucesivas por 2.
        - Asegura que el resultado tenga 8 bits, agregando ceros a la izquierda si es necesario.
    """
    binary = []
    # Meintas sea mayor a 0
    while n > 0:
        # Hacer division por 0
        residuo = n % 2
        print(f"{n} / 2 = {n//2}, residuo = {residuo}")
        # Agregar el bit actual
        binary.append(str(residuo))
        # Hacer la division para bytes
        n //=2
    # En caso de no haber 8 bits, se agrega uno al inicio
    if len(binary) < 8:
        binary.append(str(0))
    # Esta al reves, se voltea
    binary.reverse()
    print(binary)
    # se retorna una sola cadena
    return ''.join(binary)

if __name__ == "__main__":
    # Ejemplo
    print(text_to_bits("Buenas tardes"))
