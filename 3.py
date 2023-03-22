import RPi.GPIO as RG
import time

RG.setmode(RG.BCM)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 15, 19, 26]
number = [0, 1, 0, 0, 0, 0, 0, 0]

RG.setup(dac, RG.OUT)

duty_cycle = input()

try:
    while (1):
        

finally:
    for i in range(len(dac)):
        RG.output(dac[i], 0)
    RG.cleanup() 
