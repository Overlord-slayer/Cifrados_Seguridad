from const import BASE64_ALPHABET

def base64_to_text_manual(base64_text):
    """
    Convierte una cadena codificada en Base64 a su representación en texto ASCII.

    Esta función sigue los pasos manuales para decodificar Base64:
    1. Elimina los caracteres de padding ('=').
    2. Convierte cada carácter Base64 en su valor binario de 6 bits.
    3. Elimina los bits de padding sobrantes.
    4. Agrupa los bits en bloques de 8 y los convierte a caracteres ASCII.

    Parámetros:
        base64_text (str): Cadena en Base64 a decodificar (por ejemplo, "SG9sYQ==").

    Retorna:
        str: Texto decodificado.

    Ejemplo:
        >>> base64_to_text_manual("SG9sYQ==")
        'Hola'

    @see https://es.wikipedia.org/wiki/Base64
    @see https://codebeautify.org/ascii-to-base64-converter
    @see https://cryptii-com.translate.goog/pipes/base64-to-binary?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
    """

    # Paso 1: Contar y eliminar el padding ('=')
    padding_chars = base64_text.count('=')
    base64_text = base64_text.rstrip('=')
    print("Paso 1 - Base64 sin padding:", base64_text, "| Padding eliminado:", padding_chars)

    # Paso 2: Convertir cada carácter Base64 en su valor binario de 6 bits
    binary_string = ''.join(format(BASE64_ALPHABET.index(c), '06b') for c in base64_text)
    print("Paso 2 - Cadena binaria (6 bits por carácter):", binary_string)

    # Paso 3: Eliminar bits de padding sobrantes
    if padding_chars:
        binary_string = binary_string[:-padding_chars * 2]  # Cada '=' representa 2 bits de padding
        print("Paso 3 - Cadena binaria después de quitar padding:", binary_string)

    # Paso 4: Agrupar en bloques de 8 bits y convertir a ASCII
    text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
    print("Paso 4 - Texto decodificado:", text)

    return text

# Ejemplo de uso
print(base64_to_text_manual("SG9sYQ=="))  # Salida esperada: 'Hola'
print(base64_to_text_manual("YnVlbmFz"))
