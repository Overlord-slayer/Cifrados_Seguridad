from const import BASE64_ALPHABET

def text_to_base64_manual(text):
    # Convertir cada carácter a binario de 8 bits
    binary_string = ''.join(format(ord(c), '08b') for c in text)

    # Agregar ceros si no es múltiplo de 6 bits
    padding_length = (6 - len(binary_string) % 6) % 6
    binary_string += '0' * padding_length

    # Dividir en bloques de 6 bits y convertirlos a Base64
    base64_string = ''.join(BASE64_ALPHABET[int(binary_string[i:i+6], 2)] for i in range(0, len(binary_string), 6))

    # Agregar '=' si hay padding
    padding_chars = padding_length // 2
    base64_string += '=' * padding_chars

    return base64_string

# Ejemplo
print(text_to_base64_manual("Hola"))  # Salida esperada: 'SG9sYQ=='
