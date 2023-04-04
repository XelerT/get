import RPi.GPIO as RG
import sys
from time import sleep

dac=[26, 19, 13, 6, 5, 11, 9, 10]
RG.setmode(RG.BCM)
RG.setup(dac, RG.OUT)

def dec2bin(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

try:
    while (True):
        print('Input number:\n')
        T=input()
        if T=='q':
            sys.exit() 
        t=int(T)/195/2
        for i in range(195):
            RG.output(dac, dec2bin(i, 8))
            sleep(t)
        for i in range(194, -1, -1):
            RG.output(dac, dec2bin(i, 8))
            sleep(t)
finally:
    RG.output(dac, 1)
    RG.cleanup()
