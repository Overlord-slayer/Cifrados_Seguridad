def xor_binary(binary1, binary2):
    """
    Aplica la operación XOR bit a bit entre dos cadenas binarias.

    Esta función toma dos cadenas binarias y aplica la operación XOR entre cada par de bits
    correspondientes. Ambas cadenas binarias deben tener la misma longitud.

    Parámetros:
    -----------
    binary1 : str
        La primera cadena binaria.
    binary2 : str
        La segunda cadena binaria.

    Retorna:
    --------
    str
        Una cadena binaria que representa el resultado de la operación XOR bit a bit.

    Lanza:
    ------
    ValueError
        Si las cadenas binarias no tienen la misma longitud.

    Ejemplo:
    --------
    >>> binario1 = "10101010"
    >>> binario2 = "11001100"
    >>> xor_binary(binario1, binario2)
    '01100110'
    """
    # Asegurarse de que ambos binarios tengan la misma longitud
    if len(binary1) != len(binary2):
        raise ValueError("Los binarios deben tener la misma longitud")
    # Aplicar XOR bit a bit
    result = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(binary1, binary2))
    return result

# Ejemplo de uso
binario1 = "10101010"
binario2 = "11001100"
print(xor_binary(binario1, binario2))  # Salida: 01100110