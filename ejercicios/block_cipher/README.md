# Cifrado con 3DES y AES

Este proyecto implementa el cifrado y descifrado de texto e imágenes utilizando los algoritmos 3DES y AES en los modos CBC y ECB.

## Requisitos
- Python 3
- PyCryptodome (`pip install pycryptodome`)

## Uso

### Cifrado y Descifrado de Texto
```python
python encryption.py
```
El programa leerá el contenido de `3des.txt`, lo cifrará con 3DES y AES en diferentes modos, y mostrará los resultados en consola.

### Cifrado y Descifrado de Imágenes
```python
python encryption.py
```
El programa cifrará la imagen `pic.png` con AES en modo CBC y generará `pic_encrypted.png`. Luego, la descifrará en `pic_decrypted.png`.

## Preguntas y Respuestas

### ¿Qué tamaño de clave se está usando para DES, 3DES y AES?
- **3DES**: 24 bytes (192 bits), aunque su seguridad efectiva es de 112 bits debido a ataques de complejidad reducida.
- **AES-256**: 32 bytes (256 bits).

### ¿Qué modo de operación está implementado?
- **3DES**: CBC (Cipher Block Chaining).
- **AES**: CBC y ECB (Electronic Codebook).

### ¿Por qué no debemos usar ECB en datos sensibles?
ECB cifra cada bloque de manera independiente sin agregar aleatoriedad, lo que permite patrones repetitivos en los datos cifrados, haciéndolos vulnerables al análisis criptográfico.

### ¿Cuál es la diferencia entre ECB vs CBC? ¿Se puede notar directamente en una imagen?
- **ECB**: Cifra bloques de datos de manera independiente, por lo que patrones en los datos originales pueden verse en la imagen cifrada.
- **CBC**: Cada bloque se mezcla con el anterior usando un IV aleatorio, eliminando patrones visibles.
- **Ejemplo**: Si ciframos una imagen BMP con ECB, los contornos de la imagen original pueden ser visibles.

### ¿Qué es el IV?
Es el vector de inicialización (Initialization Vector), un valor aleatorio necesario para modos como CBC para asegurar que los cifrados sean únicos incluso si el mismo mensaje es cifrado varias veces con la misma clave.

### ¿Qué es el Padding?
AES y 3DES requieren que los datos sean múltiplos del tamaño de bloque. Si los datos no coinciden, se agregan bytes extra para completar el tamaño requerido (por ejemplo, con PKCS7).

### ¿En qué situaciones se recomienda cada modo de operación?
- **ECB**: No recomendado para datos sensibles.
- **CBC**: Adecuado para datos estructurados como archivos y bases de datos.
- **GCM**: Mejor opción cuando se necesita autenticación (no implementado en este proyecto).

### ¿Cómo elegir un modo seguro en cada lenguaje de programación?
- En **Python**, utilizar `AES.MODE_GCM` para seguridad óptima.
- En **Java**, `Cipher.getInstance("AES/GCM/NoPadding")`.
- En **Go**, `cipher.NewGCM(blockCipher)`.

## Referencias
- [AES Specification (NIST)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)
- [NIST Recommendation for Block Cipher Modes](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38A.pdf)
- [PyCryptodome Documentation](https://www.pycryptodome.org/)
- [Why is ECB mode bad? (Crypto.SE)](https://crypto.stackexchange.com/questions/20941/why-shouldnt-i-use-ecb-encryption)

---
Este documento cubre las implementaciones y sus fundamentos teóricos para un cifrado seguro con 3DES y AES.

