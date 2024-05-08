import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.IN)

def sensor():
    print("Waiting for movement")
    while True:
        if GPIO.input(16):
            i = 1
        elif i == 1:
            sleep(0.1)
        else:
            print("Movement detected")
            break

def greenlight():
    print("hello green")
    GPIO.output(8, GPIO.HIGH)
    sleep(5)
    print("changing to red")
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    sleep(2)
    GPIO.output(10, GPIO.LOW)

def redlight():
    print("hello red")
    GPIO.output(12, GPIO.HIGH)
    sleep(5)
    print("changing to green")
    GPIO.output(12, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    sleep(2)
    GPIO.output(10, GPIO.LOW)

def yellowlight():
    print("hello yellow")
    GPIO.output(10, GPIO.HIGH)
    sleep(1)
    GPIO.output(10, GPIO.LOW)
    sleep(1)

for i in range(3):
    yellowlight()
    redlight()
