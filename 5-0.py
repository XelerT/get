import RPi.GPIO as RG
import time

dac = [26, 19, 13, 6, 5, 11, 9 , 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4

RG.setmode(RG.BCM)
RG.setup(dac, RG.OUT, initial=RG.LOW)
RG.setup(troykaModule, RG.OUT, initial=RG.HIGH)
RG.setup(comparator, GPIO.IN)

def dec2bin(dec):
  return [int(bit) for bit in bin(dec)[2:].zfill(bits)]
  
 def num2dac(value):
  signal = dec2bin(value)
  RG.output(dac, signal)
  return signal
  
try:
  while True:
    for value in range(256):
      time.sleep(0.0007)
      signal = num2dac(value)
      voltage = value / levels * maxVoltage
      comparatorValue = RG.input(comparator)
      if comparator == 0:
        print("ADC value = {:^3} ->, input voltage = {:.2f}".format(value, signal, voltage))
        break
        
finally:
  RG.output(dac, RG.LOW)
  RG.cleanup(dac)
  print('Cleaned and ended')
        
