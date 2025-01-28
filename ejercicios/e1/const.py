"""
Cadena que contiene los caracteres válidos para la codificación BASE64.

Esta constante define los 64 caracteres utilizados en el estándar BASE64, que incluye:
- Letras mayúsculas (A-Z),
- Letras minúsculas (a-z),
- Dígitos (0-9),
- Los caracteres '+' y '/'.

Se utiliza en funciones de conversión entre binario, texto y formato BASE64.

Ejemplo de uso:
--------------
>>> BASE64_CHARS
'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
"""
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
