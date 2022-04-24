#import necessary libraries
import random
import time
from gpiozero import LED, Button

#setup gpiozero objects
ledR = LED(22)
ledB = LED(24)
btnRed = Button(26)
btnBlue = Button(19)

#set variables
level = 1
ledArray = []
btnArray = []
#playerCorrect = False

#define a function to monitor for button pressed
def monitorButtons(seconds):
    global btnArray, ledArray

    #loop for specified time, checking for button press
    timeEnd = time.time() + seconds

    while time.time() < timeEnd:
        if btnRed.is_pressed:
            return playerInput(btnRed)
        
        elif btnBlue.is_pressed:
            return playerInput(btnBlue)

        return False

# wait for player to follow the sequence
def playerInput(btn):
    global btnArray
    
    if btn == btnRed:
        btnArray.append(0)
    elif btn == btnBlue:
        btnArray.append(1)

#increments level
def levelPlayerisOn():
    global level
    global playerCorrect
    if playerCorrect == True:
        level = level + 1
    else:
        level = level - level

#def if player is correct
def isplayerCorrect():
    global playerCorrect
    global btnArray, ledArray
    
    if btnArray == ledArray:
        playerCorrect = True
        print("Correct")
    else:
        playerCorrect = False
        print(" Not Correct")

#blinks random led
def randomLED():
    #sets variables
    global level
    global ledArray
    global ledColor
    Red = 0
    Blue = 1
    i = 1

    #loops until equal to level
    while i <= level:
        #prints current variable
        print(i)
        print(level)

        #selects a random LED color from what is available
        ledColor = random.choice([ledR, ledB])

        #turns on the led
        ledColor.on()

        #add a 1 or 0 to the ledColor array
        if ledColor == ledR:
            ledArray.append(Red)
        elif ledColor == ledB:
            ledArray.append(Blue)

        #leaves the LED lit for 1 second
        time.sleep(1)

        #turns the LED off
        ledColor.off()

        #waits a second before going forward
        time.sleep(1)

        #prints current LED Array
        print(ledArray)        

        #increments i
        i += 1


        #determines if the user moves to the next level or game is over
        if i > level:            
            continue
            


def main():
    global level
    global ledArray
    global btnArray
    i = 1
    btnPressed = False
    
    try:
        while True:
            #calls randomLED function
            randomLED()

            print("LED Array " , str(ledArray))

            print(btnArray)

            #waits for button pressed
            while len(btnArray) < len(ledArray):
                #btnPressed = False
                if btnPressed == False:
                    btnPressed = monitorButtons(1)
                else:
                    btnPressed = False

            #prints the value of the current btnArray
            print(btnArray)        

            #calls isplayerCorrect function
            isplayerCorrect()

            #calls levelPlayerisOn function
            levelPlayerisOn()

            ledArray = []
            print(ledArray)
            btnArray = []
            print(btnArray)

            
    #continues game until the user presses Ctrl + C
    except KeyboardInterrupt:
        pass
    print("game over")
    print("level " + str(level))

#executes file
main()        

