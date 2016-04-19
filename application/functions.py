#functions for the creation of sound waves

#functions will have a time dependence that must be defined within audio module

import numpy as np

def sqr_wav(f, v):
    #square wave takes frequency (f) and amplitude (v) inputs
    h = 0
    if np.sin(2*np.pi*t) > 0:
        h = v
    if np.sin(2*np.pi*t) < 0:
        h = -v
    return h
    
def sin_wave(f, v):
    #regular wave takes frequency (f) and amplitude (v) inputs
    
    return v * np.sin(2*np.pi*t)
    
def tri_up(f, v):
    p = t
    if p > v:
        p -= 2*(v/f)
    if p == v:
        p -= 2*(v/f)
    return p*v

def modal(f, v, a, b, c):
    #gives adjustable weighted average function while retaining volume
    mod = ((a*functions.tri_up(f,v) + (b*functions.sin_wave(f,v)) + (c*functions.sqr_wav(f,v))))/(a+b+c)
    return mod
            
def notes(x):
    #takes integer tone (from "middle c") and converts to frequency corresponding to a musical note in the European musical language
    #if x.type not int:
     #   raise ValueError "input must be integer"
 
    f = 440 * 2**((x-9)/12)
    
    return f