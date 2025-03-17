# Cifrado con 3DES y AES

Este proyecto implementa el cifrado y descifrado de texto e imágenes utilizando los algoritmos **3DES** y **AES** en los modos **CBC** y **ECB**.

## Requisitos
- Python 3
- PyCryptodome (`pip install pycryptodome`)

## Uso

### Ejercicio 1
```sh
python encryption_e1.py
```
El programa leerá el contenido de `3des.txt`, lo cifrará con 3DES y AES en diferentes modos, y mostrará los resultados en consola.

### Ejercicios 2, 3 y 4
```sh
python encryption_rest.py
```
El programa cifrará la imagen `pic.png` con AES en modo CBC y generará `pic_encrypted.png`. Luego, la descifrará en `pic_decrypted.png`.

## Preguntas y Respuestas

### ¿Qué tamaño de clave se está usando para DES, 3DES y AES?
- **DES**: 8 bytes (64 bits), pero solo 56 bits son efectivos.
- **3DES**: 24 bytes (192 bits), con seguridad efectiva de 112 bits.
- **AES-256**: 32 bytes (256 bits).

### ¿Qué modo de operación está implementado?
- **DES**: ECB (Electronic Codebook).
- **3DES**: CBC (Cipher Block Chaining).
- **AES**: CBC y ECB.

### ¿Por qué no debemos usar ECB en datos sensibles?
ECB cifra cada bloque de manera independiente sin aleatoriedad, esto permite que patrones repetitivos en los datos originales **se reflejen en el texto cifrado**, haciéndolo vulnerable a ataques de análisis de patrones. En pocas palabras, hace una capa fina traspasable a la info, siendo no seguro

### ¿Cuál es la diferencia entre ECB y CBC? ¿Se puede notar directamente en una imagen?
- **ECB**: Cada bloque se cifra de manera independiente, lo que permite que patrones en los datos originales sean visibles en el cifrado. En imágenes, esto significa que **contornos y estructuras aún se pueden ver** en la imagen cifrada.
- **CBC**: Cada bloque se mezcla con el anterior mediante un **vector de inicialización (IV)**, lo que **rompe los patrones visibles** en la imagen cifrada.

Si ciframos una imagen BMP con ECB, los colores y formas generales de la imagen original **aún se pueden distinguir en la versión cifrada**.

### ¿Qué es el IV?
El **vector de inicialización (IV)** es un valor aleatorio utilizado en modos como CBC para asegurar que los cifrados sean únicos, **incluso si se usa la misma clave y el mismo mensaje**. En este código, el IV se genera con `get_random_bytes(16)` para AES y `get_random_bytes(8)` para 3DES.

### ¿Qué es el Padding y por qué es necesario?
Tanto **AES como 3DES** requieren que los datos sean **múltiplos del tamaño del bloque**:
- **AES**: Bloques de **16 bytes**.
- **3DES**: Bloques de **8 bytes**.

Si el texto no coincide con estos tamaños, se usa **PKCS7 padding** para rellenar los datos hasta el tamaño adecuado.

### ¿En qué situaciones se recomienda cada modo de operación?
- **ECB**: **No recomendado** para datos sensibles, ya que no oculta patrones.
- **CBC**: Adecuado para cifrar **archivos y bases de datos**, ya que oculta patrones en los datos.

### ¿Cómo elegir un modo seguro en cada lenguaje de programación?
Dependiendo del lenguaje de programación, se deben considerar aspectos como la disponibilidad de librerías criptográficas, soporte para modos de operación seguros y manejo adecuado de claves e IVs. En general, se recomienda evitar ECB y optar por CBC o GCM, asegurando que los datos sean protegidos contra ataques criptográficos. La elección debe priorizar la seguridad de los datos y el cumplimiento de buenas prácticas criptográficas.

## Referencias
- [AES Specification (NIST)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)
- [PyCryptodome Documentation](https://www.pycryptodome.org/)
- [Why is ECB mode bad? (Crypto.SE)](https://crypto.stackexchange.com/questions/20941/why-shouldnt-i-use-ecb-encryption)

---

