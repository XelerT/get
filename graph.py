import RPi.GPIO as RG
import time
import matplotlib.pyplot as plt

leds = [24, 25, 8, 7, 12, 16, 20, 21]
dac  = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

RG.setmode(RG.BCM)

RG.setup(dac,    RG.OUT, initial = RG.LOW)
RG.setup(troyka, RG.OUT, initial = 0)

RG.setup(comp, RG.IN)
RG.setup(leds, RG.OUT)


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k+=2**i
        RG.output(dac, dec2bin(k))
        time.sleep(0.005)
        if RG.input(comp) == 0:
            k-=2**i

    return k


def num2leds(value):

    signal = dec2bin(value)
    RG.output(leds, signal)
    
    return signal

try:
    points = []
    start_time = time.time()

    for i in range(1000):
        number = adc()
        print("Adc: ", number)
        num2leds(number)
        points.append(number)

        if number > 250:
            RG.output(troyka, False)
            print('DOWN')

    end_time = time.time()
    print(end_time - start_time)

    plt.plot(points)
    plt.show()

    with open("data.txt", "w") as outfile:
        outfile.write("\n".join([str(item) for item in points]))

    with open("settings.txt", "w") as settingfile:
        settingfile.write("descr Frequency:\n")
        settingfile.write(str(1000/(end_time - start_time)))

finally:
    RG.output(dac, 0)
    RG.output(leds, 0)
    RG.cleanup()