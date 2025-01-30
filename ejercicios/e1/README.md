### Archivo descriptivo
En este caso, se hallan los scrips para cifrados. Son solamente "librerias" propias
para poder desarrollar o implementar cifrados para el laboratorio 1.

Tomar en cuenta que se utilizo un entorno virutal de python

python -m venv <nombre_del_entorno>

### Ejecutar entorno en windos
```
<nombre_del_entorno>\Scripts\activate
```
## Ejecutar el entorno en Linux
```
source <nombre_del_entorno>/bin/activate
```

Tomar en cuenta que los elementos necesarios para su compilacion, estan en requirements.txt.

Realizar la creación de un script que permita la conversión de palabras en texto ASCII a BINARIO
ascii_binary.py
Hola, mama respectivamente

Realizar la creación de un script que permita la conversión de palabras en texto BASE64 a BINARIO
SG9sYQ==, 924sdfv

Realizar la creación de un script que permita la conversión de BINARIO a BASE64
010010000110111101101100011000010000/01001000011011110110110001100001 => SG9sYQ==
111101110110111000101100011101011111101111 => 924sdfv

Realizar la creación de un script que permita la conversión de BINARIO a ASCII
111101110110111000101100011101011111101111 => ÷n,uû
01001000011011110110110001100001 => Hola

Realizar la creación de un script que permita la conversión de BASE64 a ASCII
924sdfv => ÷n,uû
SG9sYQ== => Hola


Realizar la creación de un script que permita aplicar XOR a un BINARIO

10101010
11001100
01100110 ← resultado xor

01010101
11011100
10001001 ← resultado xor


Realizar la creación de un script que permita generar llaves dinámicas (utilizar ASCII)
longitud 10
jZvWYDyv0I

longitud 15
ZjP2lCNE7E0YfBK

Realizar la creación de un script que generar un nuevo cypher en ASCII con una llave k de tamaño fijo

Realizar la creación de un script que generar un nuevo cypher en ASCII con una llave k de tamaño dinámico

