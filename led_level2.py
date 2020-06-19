import RPi.GPIO as GPIO
from time import sleep

LED_G_PIN = 17 # GREEN
LED_Y_PIN = 27 # Yellow
LED_R_PIN = 22 # Red

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_G_PIN, GPIO.OUT)
    GPIO.setup(LED_Y_PIN, GPIO.OUT)
    GPIO.setup(LED_R_PIN, GPIO.OUT)

INIT_WAIT_SEC = 5   
SLEEPING_SEC = 0.5

def blink():
    sleep(INIT_WAIT_SEC)
    while True:
        GPIO.output(LED_G_PIN, GPIO.HIGH) 
        sleep(SLEEPING_SEC)
        GPIO.output(LED_Y_PIN, GPIO.HIGH) 
        sleep(SLEEPING_SEC)
        GPIO.output(LED_R_PIN, GPIO.HIGH) 
        sleep(SLEEPING_SEC)
        GPIO.output(LED_G_PIN, GPIO.LOW) 
        sleep(SLEEPING_SEC)    
        GPIO.output(LED_Y_PIN, GPIO.LOW) 
        sleep(SLEEPING_SEC)
        GPIO.output(LED_R_PIN, GPIO.LOW) 
        sleep(SLEEPING_SEC)

def destroy():
    GPIO.output(LED_G_PIN, GPIO.LOW)
    GPIO.output(LED_Y_PIN, GPIO.LOW)
    GPIO.output(LED_R_PIN, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()
