# gfp #
Es el modulo encargado de contener las clases generadoras de funciones periódicas.
Las funciones que alberga actualmente son:
  * Seno
  * Diente de sierra
  * Onda triangular
  * Onda cuadrada
Todas las clases generadoras tienen los metodos start(), stop(), pause() y el atributo dat que es donde se almacena el estado actual de la función.
El método start() comienza la generación de la función instanciada, stop() lo detiene y finaliza. Por último pause() funciona junto con el argumento True o False. De esta manera se pausa o deja proseguir la generación de la función. Mientras la generación está pausada, el valor de dat no cambia en absoluto, conservando el valor último que había tomado.

> ## Seno ##
> Esta función se instancia mediante gfp.SinSignal(dc, ampl, freq, phase, rate)
> Siendo:
  * dc: la componente de continua sobre la que se monta la señal
  * ampl: la amplitud máxima que alcanzará la señal
  * freq: la frecuencia de la señal
  * phase: la fase de la señal
  * rate: la frecuencia de sampleo con que se genera la señal. Para que no haya alias esta frecuencia debe ser al menos dos veces mayor a la frecuencia de la señal

> ### Ejemplo de uso ###
> >>> import gfp as sig

> >>> sin = sig.SinSignal(0,1,10,0,100)

> >>> sin.start()

> >>> sin.dat

> 0.58778525229245859

> >>> sin.dat

> 0.95105651629516452

> >>> sin.dat

> -0.58778525229245693

> >>> sin.stop()

> En este caso se mostró el valor de la señal (sin.dat) en un instante arbitrario. Para poder reproducir la señal habría que hacer una adquisición de sin.dat por lo menos a una frecuencia igual a rate.


> ## Diente de sierra ##
> Esta función se instancia mediante gfp.SawtoothSignal(dc, ampl, freq, phase, rate, width=0.5)
> Siendo:
  * dc: la componente de continua sobre la que se monta la señal
  * ampl: la amplitud máxima que alcanzará la señal
  * freq: la frecuencia de la señal
  * phase: la fase de la señal
  * rate: la frecuencia de sampleo con que se genera la señal. Para que no haya alias esta frecuencia debe ser al menos dos veces mayor a la frecuencia de la señal
  * width: es la fracción de periodo en el cual se produce el máximo del diente de sierra. Este valor va de 0 a 1.

> ### Ejemplo de uso ###
> >>> import gfp as sig

> >>> dds = sig.SawtoothSignal(0,1,10,0,100,0.7)

> >>> dds.start()

> >>> dds.dat

> 0.37626295104382734

> >>> dds.dat

> 0.37626295104382734

> >>> dds.dat

> 0.4808799060989486

> >>> dds.dat

> 0.4808799060989486

> >>> dds.dat

> -0.66197723675816178

> >>> dds.stop()

> En este caso se mostró el valor de la señal (dds.dat) en un instante arbitrario. Para poder reproducir la señal habría que hacer una adquisición de dds.dat por lo menos a una frecuencia igual a rate.

> ## Onda triangular ##
> Esta función se instancia mediante gfp.TriangleSignal(dc, ampl, freq, phase, rate)
> Siendo:
  * dc: la componente de continua sobre la que se monta la señal
  * ampl: la amplitud máxima que alcanzará la señal
  * freq: la frecuencia de la señal
  * phase: la fase de la señal
  * rate: la frecuencia de sampleo con que se genera la señal. Para que no haya alias esta frecuencia debe ser al menos dos veces mayor a la frecuencia de la señal

> En esencia es una onda tipo diente de sierra con el parámetro width fijo en 0.5

> ### Ejemplo de uso ###
> >>> import gfp as sig

> >>> tri = sig.TriangleSignal(0,1,10,0,100)

> >>> tri.start()

> >>> tri.dat

> -0.60000000000002274

> >>> tri.dat

> -0.59999999999996634

> >>> tri.dat

  1. 0

> >>> tri.stop()

> En este caso se mostró el valor de la señal (tri.dat) en un instante arbitrario. Para poder reproducir la señal habría que hacer una adquisición de tri.dat por lo menos a una frecuencia igual a rate.


> ## Onda cuadrada ##
> Esta función se instancia mediante gfp.SquareSignal(dc, ampl, freq, phase, rate, duty=0.5)
> Siendo:
  * dc: la componente de continua sobre la que se monta la señal
  * ampl: la amplitud máxima que alcanzará la señal
  * freq: la frecuencia de la señal
  * phase: la fase de la señal
  * rate: la frecuencia de sampleo con que se genera la señal. Para que no haya alias esta frecuencia debe ser al menos dos veces mayor a la frecuencia de la señal
  * duty: el fracción de periodo en que la señal se encuentra en estado alto (ciclo de trabajo). duty debe estar entre 0 y 1

> En esencia es una onda tipo diente de sierra con el parámetro width fijo en 0.5

> ### Ejemplo de uso ###
> >>> import gfp as sig

> >>> quad = sig.SquareSignal(0,1,10,0,100,0.5)

> >>> quad.start()

> >>> quad.dat

> 0

> >>> quad.dat

> 0

> >>> quad.dat

  1. 

> >>> quad.dat

  1. 

> >>> quad.stop()

En este caso se mostró el valor de la señal (quad.dat) en un instante arbitrario. Para poder reproducir la señal habría que hacer una adquisición de quad.dat por lo menos a una frecuencia igual a rate.