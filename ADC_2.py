import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4
comparatorvalue = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)


def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def bin2led(value):
    signal = dec2bin(value)
    GPIO.output(leds, signal)
    return signal

def poisk():
    value = 2**(bits - 1)
    for i in range(1, 8):
        signal = bin2dac(value)
        time.sleep(0.001)
        comparatorvalue = GPIO.input(comparator)
        if comparatorvalue == 1:
            value += (2**(bits - i - 1))
        else:
            value -= (2**(bits - i - 1))
    value -= (value % 2)
    signal = bin2dac(value)
    return value

def adc():
    signal = [0, 0, 0, 0, 0, 0, 0, 0]
    value = poisk()
    for i in range(value // 32):
        signal[7 - i] = 1
    signal[0] = value // 250
    GPIO.output(leds, signal)

try:
    while True:
        adc()
except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleanup completed, your majesty!")