#import necessary libraries
import time
from gpiozero import LED, RGBLED, Button

#setup gpiozero objects
ledR = LED(16)
ledY = LED(20)
ledG = LED(21)
RGB = RGBLED(22,27,17)
btn = Button(26)


#define function to run light sequence
def runLights():
    RGB.color = (1,0,0)  # set pedestrian light red
    ledR.off()
    ledG.on()            # set traffic light green
    time.sleep(2)
    ledG.off()
    ledY.on()            # set traffic light yellow
    time.sleep(2)
    ledY.off()
    ledR.on()            # set traffic light red
    time.sleep(2)

# define function to request a safe crossing
def safeCrossing():
    global pedestrian
    pedestrian = True

#define function for pedestrian crossing
def allowPedestrian():
    RGB.color = (0,1,0)     # set pedestrian light green
    time.sleep(2)

#loop through light sequence, checking for pedestrians
btn.when_pressed = safeCrossing     # set a callback
while True:
    pedestrian = False
    runLights()     #run traffic light sequence
    if pedestrian:  # check for pedestrians
        allowPedestrian()
