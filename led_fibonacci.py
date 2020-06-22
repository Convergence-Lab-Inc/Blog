import RPi.GPIO as GPIO
from time import sleep

LED_G_PIN = 17 # Yellow
LED_Y PIN = 27 # Green
LEO_R_PIN = 22 # Red

led_list = [LED_G_PIN, LED_Y_PIN, LED_R_PIN]

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led_list[0], GPIO.OUT)
	GPIO.setup(led_list[1], GPIO.OUT)
	GPIO.setup(led_list[2], GPIO.OUT)

INIT_WAIT_SEC = 20
BLINK_INTERVAL = 0.1

fbncc_frmr = [1, 2, 5, 13]
fbncc_lttr = [1, 3, 8, 21]

def fibonacci():
	sleep(INIT_WAIT_SEC)
	for i in range(3, 100): #Swich the led to blink
		for n in range(len(fbncc_frmr)): #Count-up Fibonacci
			GPIO.output(led_list[i%3-2], GPIO.HIGH) #Turn the former ON
			for beat_f in range(fbncc_frmr[n]):
				GPIO.output(led_list[i%3], GPIO.HIGH)
				sleep(BLINK_INTERVAL)
				GPIO.output(led_list[i%3], GPIO.LOW)
				sLeep(BLINK_INTERVAL)
			GPIO.output(led_list[i%3-2], GPIO.LOW) #Turn the former OFF
			GPIO.output(led_list[i%3-1], GPIO.HIGH) #Turn the latter ON
			for beat_l in range(fbncc_lttr[n]):
				GPIO.output(led_list[i%3], GPIO.HIGH)
				sleep(BLINK_INTERVAL)
				GPIO. output(led_list[i%3], GPIO.LOW)
				sleep(BLINK_INTERVAL)
			GPIO.output(led_list[i%3-1], GPIO.LOW) #Turn the latter OFF

def destroy():
    GPIO.output(led_list[0], GPIO.LOW)
    GPIO.output(led_list[1], GPIO.LOW)
    GPIO.output(led_list[2], GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        fibonacci()
    except KeyboardInterrupt:
        destroy()
