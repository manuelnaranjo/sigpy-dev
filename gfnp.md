# gfnp #
Es el modulo encargado de contener las clases generadoras de funciones no periódicas.
Las funciones que alberga actualmente son:
  * Señal aleatoria
  * Pulso
  * Escalón
  * Rampa
  * Pulso gaussiano
Todas las clases generadoras tienen los metodos start(), stop(), pause() y el atributo dat que es donde se almacena el estado actual de la función.
El método start() comienza la generación de la función instanciada, stop() lo detiene y finaliza. Por último pause() funciona junto con el argumento True o False. De esta manera se pausa o deja proseguir la generación de la función. Mientras la generación está pausada, el valor de dat no cambia en absoluto, conservando el valor último que había tomado.

> ## Señal aleatoria ##
> Esta función se instancia mediante gfnp.RandomSignal(dc, hi, low, rate)
> Siendo:
  * dc: la componente de continua sobre la que se monta la señal
  * hi: el máximo valor que puede tomar la señal
  * low: el mínimo valor que puede tomar la señal
  * rate: la frecuencia de sampleo con que se genera la señal.

> ### Ejemplo de uso ###
> >>> import gfnp as sig

> >>> ran = sig.RandomSignal(0,1,-1,100)

> >>> ran.start()

> >>> ran.dat

> 0.98625539020219599

> >>> ran.dat

> 0.34830366602194052

> >>> ran.dat

> -0.66773361171216128

> >>> ran.stop()


> En este caso se mostró el valor de la señal (ran.dat) en un instante arbitrario. Para poder reproducir la señal habría que hacer una adquisición de ran.dat por lo menos a una frecuencia igual a rate.

> ## Pulso ##
> Esta función se instancia mediante gfnp.PulseSignal(dc, ampl, t, rate)
> Siendo:
  * dc: la componente de continua sobre la que se monta la señal
  * ampl: la amplitud máxima que alcanzará la señal
  * t: el tiempo a partir de start(), en segundos, al que se produce el pulso
  * rate: la frecuencia de sampleo con que se genera la señal.

Una aclaración importante sobre esta función es que, si bien tiene propiedades temporales similares, no es la función impulso. La punción pulso que aquí se genera tiene una amplitud finita, mientras que la función impulso tiene amplitud infinita y energía unitaria.
Sin embargo, para muchos usos puede reemplazarse la función impulso con la función pulso.

> ### Ejemplo de uso ###
> >>> import gfnp as sig

> >>> pul = sig.PulseSignal(0,1,0.5,100)

> >>> pul.start()

> >>> pul.dat

> 0

> >>> pul.dat

> 0

> >>> pul.dat

> 0

> >>> pul.stop()


> En este caso se mostró el valor de la señal (pul.dat) en un instante arbitrario. Para poder reproducir la señal habría que hacer una adquisición de pul.dat por lo menos a una frecuencia igual a rate.
También puede observarse que el pulso no fue detectado ya que ninguna de las adquisiciones coincidió con el acontecimiento del pulso.


> ## Escalón ##
> Esta función se instancia mediante gfnp.StepSignal(dc, ampl, t, rate)
> Siendo:
  * dc: la componente de continua sobre la que se monta la señal
  * ampl: la amplitud máxima que alcanzará la señal
  * t: el tiempo a partir de start(), en segundos, al que se produce el escalón
  * rate: la frecuencia de sampleo con que se genera la señal.

Si se mantiene la amplitud ampl, de esta función en 1 entonces será el escalón unitario.

> ### Ejemplo de uso ###
> >>> import gfnp as sig

> >>> u = sig.StepSignal(0,1.3,1,100)

> >>> u.start()

> >>> u.dat

> 0

> >>> u.dat

> 0

> >>> u.dat

  1. 3

> >>> u.dat

  1. 3


> >>> u.stop()


> En este caso se mostró el valor de la señal (u.dat) en un instante arbitrario. Para poder reproducir la señal habría que hacer una adquisición de u.dat por lo menos a una frecuencia igual a rate.
Puede observarse que la función vale 0 hasta alcanzado cierto tiempo (t) en donde comienza a valer 1.3 para todo tiempo futuro.

> ## Rampa ##
> Esta función se instancia mediante gfnp.RampSignal(dc, pend, t, rate)
> Siendo:
  * dc: la componente de continua sobre la que se monta la señal
  * pend: la pendiente con la que evolucionará la señal
  * t: el tiempo a partir de start(), en segundos, en el que comienza la rampa
  * rate: la frecuencia de sampleo con que se genera la señal.

Podría considerarse que esta función es una función diente de sierra con un periodo infinito. Claro que podría realizarse mediante la función gfp.SawTooth con una frecuencia muy pequeña. Sin embargo se prefirió escribir una clase exclusiva para la rampa.
Debe tenerse en cuenta que esta función crece indefinidamente por lo que si se aplica a un dispositivo de hardware como la placa de sonido, seguramente se saturará en algún momento.

> ### Ejemplo de uso ###
> >>> import gfnp as sig

> >>> ramp = sig.RampSignal(0,0.25,1,100)

> >>> ramp.start()

> >>> ramp.dat

> 0

> >>> ramp.dat

> 0.58499999999999996

> >>> ramp.dat

> 0.78499999999999992

> >>> ramp.dat

  1. 0024999999999999

> >>> ramp.stop()


> En este caso se mostró el valor de la señal (ramp.dat) en un instante arbitrario. Para poder reproducir la señal habría que hacer una adquisición de ramp.dat por lo menos a una frecuencia igual a rate.


> ## Pulso gaussiano ##
> Esta función se instancia mediante gfnp.GaussPulseSignal(dc, ampl, t, sigma, rate)
> Siendo:
  * dc: la componente de continua sobre la que se monta la señal
  * ampl: la amplitud máxima que alcanzará la señal
  * t: el tiempo a partir de start(), en segundos, en el que se produce el máximo del pulso
  * igma: ancho de la campana
  * rate: la frecuencia de sampleo con que se genera la señal.


> ### Ejemplo de uso ###
> >>> import gfnp as sig

> >>> gauss = sig.GaussPulseSignal(0,1,0.5,0.2,100)

> >>> gauss.start()

> >>> gauss.dat

> 9.0697191770992349e-14

> >>> gauss.dat

> 6.1821713241296712e-49

> >>> gauss.dat

> 8.9297869115723941e-81

> >>> gauss.dat

> 3.2346762837951976e-149


> >>> gauss.stop()


> En este caso se mostró el valor de la señal (gauss.dat) en un instante arbitrario. Para poder reproducir la señal habría que hacer una adquisición de gauss.dat por lo menos a una frecuencia igual a rate.