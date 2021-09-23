import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxvoltage = 3.3

def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
try:
    while True:
        for value in range(256):
            signal = bin2dac(value)
            time.sleep(0.01)
        for value in range(255, 1, -1):
            signal = bin2dac(value)
            time.sleep(0.01)
except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleanup completed, your majesty!")