# Tabla de caracteres base64 estándar
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def read_image_binary(file_path):
    """
    Lee un archivo de imagen en formato binario.

    Args:
        file_path (str): La ruta del archivo de imagen.

    Returns:
        bytes: El contenido binario del archivo.
    """
    with open(file_path, "rb") as img_file:
        binary_data = img_file.read()
    return binary_data

def convert_to_base64_manual(binary_data):
    """
    Convierte datos binarios en una cadena codificada en Base64 de manera manual.

    Args:
        binary_data (bytes): Los datos binarios a convertir.

    Returns:
        str: La cadena codificada en Base64.
    """
    # Convertir los datos binarios a una cadena de bits
    binary_string = ''.join(f'{byte:08b}' for byte in binary_data)

    # Rellenar con ceros para que la longitud sea múltiplo de 6
    padding_length = (6 - len(binary_string) % 6) % 6
    binary_string += '0' * padding_length

    # Convertir cada grupo de 6 bits a su equivalente en base64
    base64_encoded = ''
    for i in range(0, len(binary_string), 6):
        six_bit_group = binary_string[i:i + 6]
        decimal_value = int(six_bit_group, 2)
        base64_encoded += BASE64_CHARS[decimal_value]

    # Agregar caracteres de padding "="
    padding = '=' * ((3 - len(binary_data) % 3) % 3)
    base64_encoded += padding

    return base64_encoded

def xor_with_key(data, key):
    """
    Aplica la operación XOR a un conjunto de datos binarios utilizando una llave de texto.

    Args:
        data (bytes): Los datos binarios a los que se aplicará XOR.
        key (str): La llave de texto utilizada para la operación XOR.

    Returns:
        bytes: Los datos resultantes después de aplicar XOR.
    """
    key_bytes = key.encode("utf-8")
    key_length = len(key_bytes)

    xor_result = bytearray()
    for i in range(len(data)):
        xor_result.append(data[i] ^ key_bytes[i % key_length])

    return bytes(xor_result)

def main():
    """
    Función principal del programa.

    - Lee una imagen en formato binario.
    - Convierte la imagen a una cadena codificada en Base64 de manera manual.
    - Aplica la operación XOR a los datos binarios utilizando una llave de texto.
    - Guarda el resultado de la operación XOR como una nueva imagen.

    Raises:
        FileNotFoundError: Si el archivo de imagen no se encuentra en la ruta especificada.
    """
    # Ruta de la imagen
    image_path = "./imagen_xor-1.png/imagen_xor.png"
    key = "cifrados_2025"

    # Leer la imagen como datos binarios
    binary_data = read_image_binary(image_path)

    # Convertir la imagen a Base64 manualmente
    base64_encoded = convert_to_base64_manual(binary_data)
    print("Imagen en Base64:")
    print(base64_encoded)

    # Aplicar XOR a los datos binarios con la llave
    xor_result = xor_with_key(binary_data, key)

    # Guardar el resultado como una nueva imagen
    with open("imagen_xor_resultante.png", "wb") as output_file:
        output_file.write(xor_result)
    print("La imagen XOR se guardó como 'imagen_xor_resultante.png'.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
