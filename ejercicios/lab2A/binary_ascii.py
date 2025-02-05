def bits_to_text(bits):
    """
    Convierte una cadena de bits en texto.

    Esta función toma una cadena de bits (0s y 1s), la divide en bloques de 8 bits,
    convierte cada bloque a su valor decimal ASCII correspondiente, y luego convierte
    esos valores decimales en caracteres para formar una cadena de texto.

    Parámetros:
    bits (str): Una cadena de bits (por ejemplo, "0100100001101001").

    Retorna:
    str: La cadena de texto resultante.

    Ejemplo:
    >>> bits_to_text("0100100001101001")
    'Hi'

    @see https://cryptii.com/pipes/text-to-binary
    """
    #Paso 0: Eliminar espacioes en blanco
    bits = bits.replace(" ","")

    # Paso 1: Dividir en bloques de 8 bits
    blocks = [bits[i:i+8] for i in range(0, len(bits), 8)]
    print("Paso 1 - Bloques de 8 bits:", blocks)

    # Paso 2: Convertir cada bloque a decimal
    decimal_values = [int(block, 2) for block in blocks]
    print("Paso 2 - Valores decimales ASCII:", decimal_values)

    # Paso 3: Convertir a caracteres
    characters = [chr(num) for num in decimal_values]
    print("Paso 3 - Caracteres correspondientes:", characters)

    # Paso 4: Unir los caracteres
    text = ''.join(characters)
    print("Paso 4 - Texto final:", text)

    return text

# Ejemplo
print(bits_to_text("0100100001101001"))  # Salida esperada: 'Hi'
print(bits_to_text("01101000 01101111 01101100 01100001 00100000 01110000 01100001 01110000 01100001"))
# help(bits_to_text)