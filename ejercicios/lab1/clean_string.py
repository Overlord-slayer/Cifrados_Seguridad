def clean_string(input_string: str):
    """
    Elimina todos los caracteres especiales de una cadena, dejando solo letras del alfabeto,
    incluyendo letras con tildes y caracteres especiales del español.

    Args:
        input_string (str): La cadena de la cual se eliminarán los caracteres especiales.

    Returns:
        str: La cadena limpia, conteniendo solo letras del alfabeto y caracteres especiales del español.
    """
    # Definir los caracteres permitidos (letras mayúsculas, minúsculas y caracteres especiales del español)
    allowed_chars = (
        "abcdefghijklmnopqrstuvwxyz"
        "ñÑ"
    )
    
    # Filtrar la cadena para mantener solo los caracteres permitidos
    cleaned_string = ''.join([char for char in input_string.lower() if char in allowed_chars])
    
    return cleaned_string


# Ejemplo de uso
# input_string = "Hola, ¿como estas? 123! ¡angel y Maria son amigos!ñoño"
# cleaned_string = clean_string(input_string)
# print("Cadena original:", input_string)
# print("Cadena limpia:", cleaned_string)