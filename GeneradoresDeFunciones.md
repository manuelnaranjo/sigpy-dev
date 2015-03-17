# Introducción #

Ambos módulos, [gfp](gfp.md) y [gfnp](gfnp.md) son en su estructura interna exactamente iguales. [gfp](gfp.md) es el que contiene a los generadores de funciones periódicas y [gfnp](gfnp.md) es el que contiene a los generadores de funciones no periódicas.
Estos generados son en esencia generadores en tiempo real. Es decir que generan la función no en tiempos digitales sino que lo hacen en linea.
Esta característica hace que se pueda inyectar la señal directamente a un conversor digital analógico o a una placa de sonido. También podría inyectarse por software a otro programa que la reproduzca.
Todos los generadores son clases que heredan gran parte de su funcionalidad de los Thread de Python, por lo que quedan corriendo "por detrás" de nuestra aplicación.

**[Clases generadores de funciones periódicas](gfp.md)**

