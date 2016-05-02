from scipy import *
from scipy import signal
from pylab import *
from wave import *
import struct
import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

t = linspace(0, 1, num = 1000, endpoint = False)

def sine(f, d=0, v=1, T=t):
    #sine wave with frequency, delay and volume controls
    return v*np.sin((2*np.pi*f)*T-(np.pi*d))

def square(f, d=0 ,v=1, T=t):
    #square wave with frequency, delay and volume controls
    return -v*signal.square((2*np.pi)*f*T-(np.pi*d))

def saw(f, d=1, v=1, T=t):
    #saw wave with frequency, delay and volume controls
    #default delay = 1 to match timing of saw and sine waves
    return v*signal.sawtooth((2*np.pi)*f*T-(np.pi*d))

def slider(f, a=1, b=0, c=0, v=1):
    #inputs: f=frequency (required), a,b,c = weighting values for functions, 
    #note: some averages may lower overall volume    
    return v*((a*sine(f) + (b*square(f)) + (c*saw(f)))/(a+b+c)

def slider_complex(f, a=1, ad =0, b=0, bd=0, c=0, cd=1, v=1):
    #inputs: f=frequency (required), a,b,c = weighting values for functions, 
    #inputs: *d = phase shift, v= volume
    #note: some averages may lower overall volume
    #default d for saw should be 1, for lining up with other functions
    return v*((a*sine(f,ad)) + (b*square(f,bd)) + (c*saw(f,cd)))/(a+b+c)