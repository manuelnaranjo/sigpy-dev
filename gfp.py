#Este archivo contien las clases que generan funciones no periodicas. Funciona mediante hilos que se pueden pausar o terminar. La idea es generar el valor actual de la funcion deseada y esperar (sleep) durante el periodo de muestreo. Contiene generadores de funciones sinusoidales, diente de sierra, triangulares y cuadradas

from threading import Thread
from time import sleep
import numpy as np



class SinSignal(Thread):

        def __init__(self, dc, ampl, freq, phase, rate):
                Thread.__init__(self)

                self.dc = dc
                self.ampl = ampl
                self.freq = freq
                self.phase = phase
                self.t_sample = 1/float(rate)
                self.dat = 0.0
                self.alive = True
                self.pause_flag = False
        
        def run(self):
                count = 0
                while self.alive:
                        self.dat = (self.dc+self.ampl*np.sin(2*np.pi * self.freq * self.t_sample * count + self.phase))
                        sleep(self.t_sample) 
                        count += 1 
                        
                        while self.pause_flag:
                                pass
                                
                                        
        def pause(self, flag):
                self.pause_flag = flag


        def stop(self):
                self.alive = False
                self.join()
                
                

class SawtoothSignal(Thread):

        def __init__(self, dc, ampl, freq, phase, rate, width=0.5):
                Thread.__init__(self)

                self.dc = dc
                self.ampl = ampl
                self.freq = freq
                self.phase = phase
                self.t_sample = 1/float(rate)
                self.dat = 0
                self.alive = True
                self.pause_flag = False
                
                self.width = width
                self.dpi = (2*np.pi)
                self.w = self.dpi*self.width
                self.cw = self.dpi - self.w
                
                
        def sawtooth(self, ang, width=0.5):
                self.pos = (ang / self.dpi)
                self.frac = self.pos-int(self.pos) #fraccion de periodo que corresponde al angulo
                self.ang_n = self.frac * self.dpi #angulo en el primer pediodo
         
                if (self.frac) < width:
                        return ((2/self.w)*self.ang_n) - 1
                else:
                        return (-2/self.cw)*self.ang_n+(2*(self.dpi/self.cw)-1)
                        
        
        def run(self):
                count = 0
                while self.alive:
                        self.dat = (self.dc+self.ampl*self.sawtooth(2*np.pi * self.freq * self.t_sample * count + self.phase, width=0.5))
                        sleep(self.t_sample)
                        count += 1   
                        
                        while self.pause_flag:
                                pass
                                        
        def pause(self, flag):
                self.pause_flag = flag


        def stop(self):
                self.alive = False
                
                
class TriangleSignal(Thread):

        def __init__(self, dc, ampl, freq, phase, rate):
                Thread.__init__(self)

                self.dc = dc
                self.ampl = ampl
                self.freq = freq
                self.phase = phase
                self.t_sample = 1/float(rate)
                self.dat = 0
                self.alive = True
                self.pause_flag = False
                
                self.width = 0.5
                self.dpi = (2*np.pi)
                self.w = self.dpi*self.width
                self.cw = self.dpi - self.w
                
                
        def triangle(self, ang, width=0.5):
                self.pos = (ang / self.dpi)
                self.frac = self.pos-int(self.pos) #fraccion de periodo que corresponde al angulo
                self.ang_n = self.frac * self.dpi #angulo en el primer pediodo
         
                if (self.frac) < width:
                        return ((2/self.w)*self.ang_n) - 1
                else:
                        return (-2/self.cw)*self.ang_n+(2*(self.dpi/self.cw)-1)
                        
        
        def run(self):
                count = 0
                while self.alive:
                        self.dat = (self.dc+self.ampl*self.triangle(2*np.pi * self.freq * self.t_sample * count + self.phase, width=0.5))
                        sleep(self.t_sample)
                        count += 1   
                        
                        while self.pause_flag:
                                pass
                                        
        def pause(self, flag):
                self.pause_flag = flag


        def stop(self):
                self.alive = False
                
                
                
class SquareSignal(Thread):

        def __init__(self, dc, ampl, freq, phase, rate, duty=0.5):
                Thread.__init__(self)

                self.dc = dc
                self.ampl = ampl
                self.freq = freq
                self.phase = phase
                self.t_sample = 1/float(rate)
                self.dat = 0
                self.alive = True
                self.pause_flag = False
                
                self.duty = duty
                self.dpi = (2*np.pi)
                
                
        def square(self, ang, duty):
                self.pos = (ang / self.dpi)
                self.frac = self.pos-int(self.pos) #fraccion de periodo que corresponde al angulo
         
                if (self.frac) < duty:
                        return 1
                else:
                        return 0
                        
        
        def run(self):
                count = 0
                while self.alive:
                        self.dat = (self.dc+self.ampl*self.square(2*np.pi * self.freq * self.t_sample * count + self.phase, duty=0.5))
                        sleep(self.t_sample)
                        count += 1   
                        
                        while self.pause_flag:
                                pass
                                        
        def pause(self, flag):
                self.pause_flag = flag


        def stop(self):
                self.alive = False
                

                

                                                                                     
