import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
frequency = 1000

def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(22, GPIO.OUT)
p = GPIO.PWM(22, frequency)
p.start(50)
try:
    while True:
        inputstr = input("Enter a value between 0 and 100 ('q' to exit) > ")
        
        if inputstr.isdigit():
            value = int(inputstr)

            if value > 100:
                print("The value is too large, try again")
                continue
            
            p.ChangeDutyCycle(value)
            print("Entered value = {:^3}%".format(value))
        elif inputstr == 'q':
            break
        else:
            print("Enter a positive integer")
            continue

except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleanup completed, your majesty!")