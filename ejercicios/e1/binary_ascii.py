def binary_to_ascii(binary):
    """
    Convierte una cadena binaria en su representación en texto ASCII.

    Esta función toma una cadena binaria, la divide en grupos de 8 bits (1 byte) y convierte
    cada grupo en su carácter ASCII correspondiente.

    Parámetros:
    -----------
    binary : str
        La cadena binaria que se desea convertir a texto ASCII. Debe tener una longitud
        múltiplo de 8 para que la conversión sea correcta.

    Retorna:
    --------
    str
        Una cadena que representa el texto ASCII resultante de la conversión.

    Ejemplo:
    --------
    >>> binario = "01001000011011110110110001100001"
    >>> binary_to_ascii(binario)
    'Hola'
    """
    # Dividir el binario en grupos de 8 bits
    groups = [binary[i:i+8] for i in range(0, len(binary), 8)]
    # Convertir cada grupo a su carácter ASCII correspondiente
    text = ''
    for group in groups:
        text += chr(int(group, 2))
    return text

# Ejemplo de uso
binario = "01001000011011110110110001100001"
print(binary_to_ascii(binario))  # Salida: Hola