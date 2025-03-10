# XOR Cipher con PRNG

## Descripción del Ejercicio
Este proyecto implementa un cifrado de flujo utilizando la operación XOR y un generador de números pseudoaleatorios (PRNG). Se genera un keystream basado en una clave (seed) y se usa para cifrar y descifrar mensajes de texto.

### Objetivos del Ejercicio
- Comprender el concepto de un keystream y su importancia en los cifrados de flujo.
- Implementar un esquema básico de cifrado y descifrado utilizando XOR.
- Analizar las implicaciones de la reutilización del keystream y su longitud en la seguridad.

## Instrucciones de Uso
1. Clonar el repositorio:
   ```bash
   git clone <repositorio>
   cd <repositorio>
   ```
2. Ejecutar el script de cifrado:
   ```bash
   python xor_cipher_prng.py
   ```
3. Para ejecutar las pruebas unitarias:
   ```bash
   python -m unittest xor_cipher_prng.py
   ```
4. Para ejecutar las preubas unitarias en modo detallado
   ```bash
      python3 -m unittest -v test_xor_prng.py
   ```

## Preguntas y Respuestas

**1. ¿Qué sucede cuando cambias la clave utilizada para generar el keystream?**
   - Si la clave cambia, el keystream generado será diferente, por lo que el mensaje cifrado no podrá ser descifrado correctamente.
   # Con variabilidad, en este caso, se utiliza el tiempo como semilla
   ![image](https://github.com/user-attachments/assets/09ae4e3b-5e1e-4589-9785-922a7419639b)
   # Con semilla fija
   ![image](https://github.com/user-attachments/assets/a18e9f5a-db02-4e18-8f64-71d3829158cf)


**2. ¿Qué riesgos de seguridad existen si reutilizas el mismo keystream para cifrar dos mensajes diferentes?**
   - Si dos mensajes distintos se cifran con el mismo keystream, se puede obtener información sobre ambos mensajes mediante análisis XOR de los textos cifrados.

**3. ¿Cómo afecta la longitud del keystream a la seguridad del cifrado?**
   - Si el keystream es más corto que el mensaje, se repetirá, reduciendo la seguridad. Debe ser al menos de la misma longitud que el mensaje.

**4. ¿Qué consideraciones debes tener al generar un keystream en un entorno real?**
   - Se debe usar un generador criptográficamente seguro como ChaCha20 o AES-CTR en lugar de un PRNG simple para evitar vulnerabilidades.

![image](https://github.com/user-attachments/assets/5468b2b4-a5cc-40ff-b3de-0325afa10749)
