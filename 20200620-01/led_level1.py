import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 17 # Yellow

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

INIT_WAIT_SEC = 3   
SLEEPING_SEC = 0.5

def blink():
    sleep(INIT_WAIT_SEC)
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH) 
        sleep(SLEEPING_SEC)
        GPIO.output(LED_PIN, GPIO.LOW) 
        sleep(SLEEPING_SEC)

def destroy():
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()
