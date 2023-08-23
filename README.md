# teoria-de-la-informacion
## Estructura del trabajo

**FUENTE DE INFORMACIÓN**

Los archivos que se recibirán para encriptar son archivos PDF, estos archivos pueden ser documentos informativos, ensayos, o cualquiera que contenga texto.

**TRANSMISOR**

El archivo se encriptará de la siguiente manera, será transformado en código binario y se le sumará un 1 a cada valor binario. No se empaquetara por el momento. El lenguaje de programación con el que se hará el proyecto es con Python. 	

**CANAL**

Se creará una función donde pasará el código encriptado a lo que simulara el canal, el canal tendrá cierto ruido de manera aleatoria ya sea por el uso masivo de la red o por el peso del archivo, esto puede hacer que el archivo pueda retrasarse para llegar al receptor, o que sufra ciertas modificaciones. La velocidad por la que se envían los paquetes es de 1000 mb/s, será por fibra óptica.

**RECEPTOR**

Esta función recibe los archivos codificados y los decodifica con el proceso de la función invertida para obtener el mensaje correcto.

**RI**
Está función imprime los mensajes decodificados, en este apartado nos daremos cuenta que ciertos mensajes fueron o no fueron afectados por el ruido.
