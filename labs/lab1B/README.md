# Lab 1, Part B

Se utilizaron la implementacion de los cifrados previamente generados en la parte A:

- **Cifrado César**
- **Cifrado Afín**
- **Cifrado Vigenère**

## Compilación

Para poder compilar el proyecto, se recomienda la utilización de entornos virtuales. A continuación, se detallan los pasos:

1. Crear un entorno virtual:
   ```bash
   python3 -m venv env

Para windows:
```
.\env\Scripts\activate
```
Para Linux
```
source <nombre_entorno>/bin/activate
```
En este caso, se modularizo el codigo para tener independecia en cada codigo, asi mismo, para la parte de frecuencia, se opto por jupyter lab,
por ello hay un .ipynb. Pero igualmente esta el .py. EN CASO MAS SIMPLE DE VERIFICAR RESULTADOS, VALIDAR LOS .ipynb para previsualizar los resultados.
Formas mas sencilla. Lo hice asi, porque a veces no funciona colocar imagenes en el README.md desde linux.

# Consideraciones
En este caso, para poder probar cada uno de los algoritmos, ingresar al archivo especifico, no hay un main.py global que implemente cada uno.

# Ejemplo
## Vigenere
Para este caso, se utilizo algo de mineria de datos, en donde se utilizan bigramas para poder determinar para poder tener una limitacion de busqueda
y hacerlo mas simple. Los bigramas y trigamas redujeron la busqueda, pues se hallaban similitudes en el texto. Cuanto más alto sea este puntaje, más 
probable es que el texto tenga sentido en español. En el caso del metodo de brute_force_attack(), este puntaje se usa para ordenar los resultados y 
encontrar las claves más probables.

1. Clave: payaso
Puntuación de estructuras comunes en español: 186
Métrica de similitud: 17.718
Texto descifrado:
aunqueelerrorheartbleedsehasolucionadosiemprehayunanuevaamenazaenelhorizontehoylacuanticaesesaamenazaquepuedeatravesartodasnuestrasdefensasantesdequetodoesteperdidodebemosadoptarlacriptoagilidadparadefendernosdisponibleenlasprincipalessolucionesdecriptografiaposcuanticapqcdelaactualidadlaevidenciade...

![image](https://github.com/user-attachments/assets/f8e16998-6ae1-4bd9-a16f-67c5598e7612)

## Cesar
Para este caso, se opto por fuerza bruta, pues era lo mas sencillo. La frecuencia fue un poco extraña, ya que quizas no se hizo la mejor implementacion o la misma, no se adecuo para la busqueda.
Clave '23', resulta en 'nnuestrolaberintodigitalenconstanteevolucionlaagilidadcriptograficacriptoagilidadparaabreviaresunmecanismodedefensacrucialosbrindalacapacidaddemodificarrapidamenteelusodealgoritmosyclavescriptograficosunaaccionnecesariaparaanticiparnosalasfuturasamenazasdeciberseguridad'


En este caso, para la r
![image](https://github.com/user-attachments/assets/d95f2166-e4c6-402c-af6f-b182b290a5b8)

## Afin
En este caso, no se hallo un decifrado como con cesar, pero esta fue la mejor que se obtuvo.

Mejor desencriptación encontrada con a=9, b=14:
hicisadltidahieiqntattiebnaflajndntatqiauitiikfbaibtidlqafamuiqiabfpdiitujtidibblbbigidluhatipndntatebuenadmuiaibsnfnladlqafaeahfiqdiibdasislbnatisndiqtiqnqfisaqzblpabnhxlbsaenlhgadnlqaaqisabiqaqmuidljbablhbieuaibabqibaantasihfixuiblhdaqmuitislqfbablhebnaflajndntatbiisadaoahtlbaantasihfiquqedagiqebnafljbaxneaqzadjlbnfslqelsablsifntlqalblfblqhuiglqzqijublqqfinhentihfiqnbgielsluhedablicisadltidansalbfahenatidaebnaflajndntatihhuiqfbapafaddaelhfnhuaelhfbadaqasihaoaqtnhasneaqtienpibqijubntat

![image](https://github.com/user-attachments/assets/0810636e-b015-467d-9b47-12b1b4f9e411)

## Frecuencia de palabras
Este se recomiendo revisar el jupyter notebook -> **frecuencia_chars_graph.ipynb**
![image](https://github.com/user-attachments/assets/1617ebb3-6da2-4872-a3d5-5ae94483bf47)
![image](https://github.com/user-attachments/assets/40f921f1-deff-4720-a45b-d8a8f1566763)


