import RPi.GPIO as RG
import sys
from time import sleep

RG.setmode(RG.BCM)
RG.setup(2, RG.OUT)

dac=[26, 19, 13, 6, 5, 11, 9, 10]      

RG.setup(dac, RG.OUT, initial=RG.HIGH)

pwm=RG.PWM(2, 1000)                                    
pwm.start(0)

pwm

try:
        while True:
                DutyCycle=input()            
                if DutyCycle=='q':
                        sys.exit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                pwm.ChangeDutyCycle(int(DutyCycle))
                print("{:.2f}".format(int(DutyCycle)*3.3/100))
finally:
    RG.output(2, 0)
    RG.output(dac, 0)
    RG.cleanup()   
