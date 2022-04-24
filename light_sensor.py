#import necessary libraries
import RPi.GPIO as GPIO, time

#set variables for easy reference
photoPin = 21
ledPin = 22
threshold = 0.02 # in seconds, adjust as needed

#initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

#define function to measure fill time
def measureFillTime(pin):
    #discharge the capacitor (empty the bucket)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(0.1)

    #fill capacitor and measure time
    timeStart = time.time()
    GPIO.setup(pin, GPIO.IN)
    while (GPIO.input(pin) == False):
        pass
    return time.time() - timeStart

# run for one minute, then cleanup!
timeEnd = time.time() + 120
while time.time() < timeEnd:
    fillTime = measureFillTime(photoPin)

    #turn on LED if "fillTime" greater than 'threshold'
    if fillTime > threshold:
        print("dark, fillTime:",fillTime)
        GPIO.output(ledPin,True)
    else:
        print("light, fillTime:",fillTime)
        GPIO.output(ledPin,False)

GPIO.cleanup()
