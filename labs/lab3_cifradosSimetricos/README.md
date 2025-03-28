# Criptografía Práctica - Análisis y Reflexiones

Este laboratorio analiza diferentes técnicas de cifrado simétrico. Abarca la ruptura de ECB en imágenes, la captura de tráfico cifrado con AES-CBC, la implementación de ChaCha20 y un simulacro de ransomware.

---

## **Parte 1: Rompiendo ECB en Imágenes**

### Escenario:
Un usuario almacena imágenes sensibles cifradas con AES-ECB. Los atacantes descubren que pueden extraer patrones de la imagen.

### Reflexiones:
- **¿Por qué el cifrado ECB revela los patrones de la imagen?**
  El modo ECB cifra bloques de datos de forma independiente. Bloques idénticos de texto plano producen bloques cifrados idénticos, revelando patrones visuales. En el caso del resultado
  se puede observar que el diagrama tiene la silueta de las figuras, eso no es tan seguro, ya que aun se percibe que hay.

![image](https://github.com/user-attachments/assets/db67cf5c-1aee-482a-94e3-6380d6388789)

- **¿Cómo cambia la apariencia con CBC?**
  El modo CBC mezcla cada bloque de texto plano con el bloque cifrado anterior antes de cifrar, eliminando patrones y produciendo una apariencia similar al ruido aleatorio.

![image](https://github.com/user-attachments/assets/c83dfc16-903b-42b9-85b4-1baeb4c15117)


- **¿Qué tan seguro es usar ECB para cifrar datos estructurados?**
  No es seguro para datos estructurados o patrones repetitivos. ECB puede permitir la recuperación parcial de datos sensibles.

---

## **Parte 2: Capturando Cifrado en Red con Wireshark**

### Escenario:
Captura y análisis de mensajes cifrados con AES-CBC sobre una red TCP.

### Reflexiones:
- **¿Se puede identificar que los mensajes están cifrados con AES-CBC?**
  Aunque no se puede descifrar fácilmente, es posible identificar patrones en los tamaños de los bloques y la estructura del tráfico.

- **¿Cómo podríamos proteger más esta comunicación?**
  - Uso de TLS/SSL para proteger el tráfico.
  - Perfect Forward Secrecy (PFS) para cambiar claves de sesión.
  - HMAC para autenticar y verificar la integridad de los mensajes.

---

## **Parte 3: Implementando un Cifrado de Flujo con ChaCha20**

### Escenario:
Implementación y comparación del cifrado de flujo ChaCha20 contra AES.

### Reflexiones:
- **¿Qué cifrado es más rápido, ChaCha20 o AES?**
  En este caso, ChaCha20 se tardo mas en el cifrado, pero fue mas eficiente en el decifrado y en el consumo de memoria para ambos casos.
  Con respecto a AES-GCM fue lo inverso, ya que cifro muy rapido, pero el resto de metricas fue malo en comparacion a ChaCha20.

  ![image](https://github.com/user-attachments/assets/4cb29637-7bb2-411d-aa17-9426a468480b)

- **¿En qué casos debería usarse en vez de AES?**
  - Dispositivos móviles y IoT donde AES-NI no está disponible.
  - Protocolos TLS modernos.
  - Escenarios donde se busca simplicidad y alta seguridad.

---

## **Parte 4: Implementación de un Ransomware Simulado**

### Escenario:
Creación de un script que cifre archivos de texto con AES para simular un ransomware.

### Reflexiones:
- **¿Cómo podríamos evitar ataques de ransomware?**
  - Mantener un backup constante, esto es depende de la persona, pero recomendable, diario, quizas sea exagerado, pero es mas seguro.
  - Implementar controles estrictos de acceso y segmentación de red.
  - Tener precaucion con el phishing y evitar utilizar herramientas o dispositivos ajenos en el dispositivo, puede estar compremetidos.

- **¿Qué tan importante es almacenar claves de manera segura?**
  Es crucial. El almacenamiento incorrecto de claves compromete la confidencialidad de los datos.

  ## SIN CIFRAR
  ![image](https://github.com/user-attachments/assets/a84e399d-1c68-45eb-8ab2-285bcfe4a1a8)

  ## CIFRADO
  ![image](https://github.com/user-attachments/assets/eab2358a-3a9e-48f9-9345-aa68c5d1d8e4)


---


