import RPi.GPIO as RG
import time

RG.setmode(RG.BCM)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 15, 19, 26]
number = [0, 1, 0, 0, 0, 0, 0, 0]

RG.setup(dac, RG.OUT)

inputed_number = 10

try:
    while (1):
        inputed_number = input()
        if inputed_number == "q":
            break
        try:
            if 0 < int(inputed_number) <= 255: 
                print(dec2bin(int(inputed_number)), '\n')
                number = dec2bin(int(inputed_number))

                for i in range(len(dac)):
                    RG.output(dac[i], number[i])
            elif int(inputed_number) < 0:
                print("inter positive numbers")
            else:
                print("Too big number")
        except:
            print("need to inter number")

finally:
    for i in range(len(dac)):
        RG.output(dac[i], 0)
    RG.cleanup() 
