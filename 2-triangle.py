import RPi.GPIO as RG
import time

RG.setmode(RG.BCM)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 15, 19, 26]
number = [0, 1, 0, 0, 0, 0, 0, 0]

RG.setup(dac, RG.OUT)

number2show = 0

period = input()
try:
    while (1):
        if period == "q":
            break
        if 0 < int(period) <= 1000: 
            for j in range(256):
                number2show += 1    
                number = dec2bin(int(number2show))
                time.sleep(1/float(period))
                
                for i in range(len(dac)):
                    RG.output(dac[i], number[i])

        elif int(period) < 0:
            print("inter positive numbers")
        else:
            print("Too big number")

finally:
    for i in range(len(dac)):
        RG.output(dac[i], 0)
    RG.cleanup() 
