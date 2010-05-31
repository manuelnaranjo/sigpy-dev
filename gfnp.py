#Este archivo contien las clases que generan funciones no periodicas. Funciona mediante hilos que se pueden pausar o terminar. La idea es generar el valor actual de la funcion deseada y esperar (sleep) durante el periodo de muestreo. Contiene generadores de funciones aleatoreas, pulso (no impulso), rampa y escalon

from threading import Thread
from time import sleep
import numpy as np


class RandomSignal(Thread):

        def __init__(self, dc, hi, low, rate):
                Thread.__init__(self)
                
                self.dc = dc
                self.hi = hi
                self.low = low
                self.t_sample = 1/float(rate)
                self.dat = 0.0
                self.alive = True
                self.pause_flag = False
        
        def run(self):
                while self.alive:
                        self.dat = (self.dc + self.low + (self.hi-self.low)*np.random.random_sample())
                        sleep(self.t_sample)
                        
                        while self.pause_flag:
                                pass
                                
                                        
        def pause(self, flag):
                self.pause_flag = flag

        def stop(self):
                self.alive = False


class PulseSignal(Thread):

        def __init__(self, dc, ampl, t, rate):
                Thread.__init__(self)

                self.dc = dc
                self.ampl = ampl
                self.t = t
                self.t_sample = 1/float(rate)
                self.dat = 0
                self.alive = True
                self.pause_flag = False
                self.shut = False
               
        def pulse(self, t, current_t):

         
                if ((t > (current_t-self.t_sample)) and (t < (current_t+self.t_sample))) and (not self.shut):
                        self.shut = True
                        return 1
                else:
                        return 0
                        
        
        def run(self):
                count = 1
                while self.alive:
                        self.dat = (self.dc+self.ampl*self.pulse(self.t, self.t_sample*count))
                        sleep(self.t_sample)
                        count += 1   
                        
                        while self.pause_flag:
                                pass
                                        
        def pause(self, flag):
                self.pause_flag = flag


        def stop(self):
                self.alive = False
                
                
class StepSignal(Thread):

        def __init__(self, dc, ampl, t, rate):
                Thread.__init__(self)

                self.dc = dc
                self.ampl = ampl
                self.t = t
                self.t_sample = 1/float(rate)
                self.dat = 0
                self.alive = True
                self.pause_flag = False

               
        def step(self, t, current_t):

         
                if t < current_t:
                        return 1
                else:
                        return 0
                        
        
        def run(self):
                count = 1
                while self.alive:
                        self.dat = (self.dc+self.ampl*self.step(self.t, self.t_sample*count))
                        sleep(self.t_sample)
                        count += 1   
                        
                        while self.pause_flag:
                                pass
                                        
        def pause(self, flag):
                self.pause_flag = flag


        def stop(self):
                self.alive = False
                
                
class RampSignal(Thread):

        def __init__(self, dc, pend, t, rate):
                Thread.__init__(self)

                self.dc = dc
                self.pend = pend
                self.t = t
                self.t_sample = 1/float(rate)
                self.dat = 0
                self.alive = True
                self.pause_flag = False
                
                
                
        def ramp(self, t, pend, current_t):
           
                if (t < current_t):
                        return (current_t-t)*pend
                else:
                        return 0
                        
        
        def run(self):
                count = 0
                while self.alive:
                        self.dat = (self.dc + self.ramp(self.t, self.pend, self.t_sample * count))
                        sleep(self.t_sample)
                        count += 1   
                        
                        while self.pause_flag:
                                pass
                                        
        def pause(self, flag):
                self.pause_flag = flag


        def stop(self):
                self.alive = False
                
                
class GaussPulseSignal(Thread):

        def __init__(self, dc, ampl, t, sigma, rate):
                Thread.__init__(self)

                self.dc = dc
                self.ampl = ampl
                self.t = t
                self.sigma = sigma
                self.t_sample = 1/float(rate)
                self.dat = 0
                self.alive = True
                self.pause_flag = False
                
                
                
        def gauss(self, t, sigma, current_t):
                return np.e**-(((current_t-t)**2)/(2*(sigma**2)))
                
                        
        
        def run(self):
                count = 0
                while self.alive:
                        self.dat = (self.dc + self.gauss(self.t, self.sigma, self.t_sample * count))
                        sleep(self.t_sample)
                        count += 1   
                        
                        while self.pause_flag:
                                pass
                                        
        def pause(self, flag):
                self.pause_flag = flag


        def stop(self):
                self.alive = False
