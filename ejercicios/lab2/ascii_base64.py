from const import BASE64_ALPHABET

def text_to_base64_manual(text):
    """
    Convierte una cadena de texto en su representación Base64 manualmente.

    Esta función sigue los pasos detallados para codificar en Base64:
    1. Convierte cada carácter en su representación binaria de 8 bits.
    2. Ajusta la longitud de la cadena binaria para que sea múltiplo de 6 bits.
    3. Divide la cadena en bloques de 6 bits.
    4. Convierte cada bloque de 6 bits a decimal.
    5. Mapea los valores decimales a los caracteres del alfabeto Base64.
    6. Agrega los caracteres '=' si es necesario para el padding.

    Parámetros:
        text (str): La cadena de texto a codificar (por ejemplo, "Hola").

    Retorna:
        str: La cadena en Base64.

    Ejemplo:
        >>> text_to_base64_manual("Hola")
        'SG9sYQ=='

    @see https://es.wikipedia.org/wiki/Base64
    @see https://codebeautify.org/ascii-to-base64-converter
    @see https://cryptii-com.translate.goog/pipes/base64-to-binary?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
    """

    # Paso 1: Convertir cada carácter a binario de 8 bits
    binary_string = ''.join(format(ord(c), '08b') for c in text)
    print("Paso 1 - Cadena binaria (8 bits por carácter):", binary_string)

    # Paso 2: Asegurar que la longitud sea múltiplo de 6 bits
    padding_length = (6 - len(binary_string) % 6) % 6  # Cálculo del padding
    binary_string += '0' * padding_length  # Agregamos los bits necesarios
    print("Paso 2 - Cadena binaria ajustada (múltiplo de 6 bits):", binary_string)

    # Paso 3: Dividir en bloques de 6 bits
    blocks = [binary_string[i:i+6] for i in range(0, len(binary_string), 6)]
    print("Paso 3 - Bloques de 6 bits:", blocks)

    # Paso 4: Convertir cada bloque de 6 bits a decimal
    decimal_values = [int(block, 2) for block in blocks]
    print("Paso 4 - Valores decimales:", decimal_values)

    # Paso 5: Convertir valores decimales a caracteres Base64
    base64_string = ''.join(BASE64_ALPHABET[val] for val in decimal_values)
    print("Paso 5 - Cadena Base64 sin padding:", base64_string)

    # Paso 6: Agregar '=' si es necesario
    padding_chars = padding_length // 2  # Cada 2 bits de padding equivalen a un '=' en Base64
    base64_string += '=' * padding_chars
    print("Paso 6 - Cadena Base64 final con padding:", base64_string)

    return base64_string

# Prueba
print(text_to_base64_manual("Hola"))  # Salida esperada: 'SG9sYQ=='
print(text_to_base64_manual("buenas"))
