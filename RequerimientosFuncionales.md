# Introducción #

En este documento se describen los requerimientos funcionales de la aplicación, necesarios para empezar el diseño del mismo.


# Requerimientos funcionales #

Agreguen aquí lo que necesita que haga el software:

El programa debe permitir la generación de señales eléctricas, con capacidad de modificacion de parámetros. Tales señales se describen a continuación:

  * Generación de señales:

  1. Cuadradas.
  1. Triangulares.
  1. Rampa
  1. Diente de sierra
  1. Pulso
  1. Pulso gaussiano
  1. Escalón
  1. Sinusoidales
  1. Aleatorias
  1. Señales cargadas por el usuario (wav)

Por otra parte el generador de señales debe independizarse del medio por el cual se saca la señal. Esto es, modularizando y separando el generador en si de las posibles salidas como son la placa de sonido, puertos, o simplemente una conexión de software a software.
Se desarrollará una interfaz de consola y una gráfica que permita la configuración de los parámetros y el control del funcionamiento del generador.

Los formatos de archivos serán los más estándares posibles siendo el wav un formato optimo para el trabajo.

  * También debe existir una familia de módulos de adquisición (como contrapunto a la generación). Esta familia debe tener un núcleo al cual se conectan todos los posibles periféricos. Se desarrollarán interfaces gráficas que permitan la visualización de las señales adquiridas.
Todos los módulos e interfaces gráficas estarán debidamente protocolizados. Esto permitirá su uso en otros desarrollos.

  * Otra familia de módulos estará destinada al diseño de filtros analógicos y digitales de todo tipo. También se confeccionará una interfaz gráfica que ayude y asista para el diseño de estos filtros.