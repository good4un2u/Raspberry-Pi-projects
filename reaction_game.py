#import necessary libraries
import time, random
from gpiozero import RGBLED, Button

#define objects for gpiozero
btnR = Button(19)
btnB = Button(26)
RGB = RGBLED(22,27,17)


#set variables
red = (1,0,0)
green = (0,1,0)
blue = (0,0,1)
BlueWinTimes = 0
RedWinTimes = 0
    

#define a function to monitor for button pressed
def monitorButtons(seconds):

    #loop for specified time, checking for button press
    timeEnd = time.time() + seconds
     
    while time.time() < timeEnd:
        if btnR.is_pressed:            
            return announceWinner(btnR)
        
        if btnB.is_pressed:            
            return announceWinner(btnB)
        
    return False

# define a function to announce the winner
def announceWinner(btn):
    global BlueWinTimes
    global RedWinTimes
    blueWins = "Blue wins: "
    redWins = "Red wins: "
    
    #determine if LED was green when button was pressed
    if RGB.color == green:
        #button press was valid, player wins!
        winner = blue if btn == btnB else red

        #print the winner and number of times they won
        if winner == blue:
            BlueWinTimes = BlueWinTimes + 1
            print("Blue Wins! Blue Wins! Blue Wins! Blue Wins!")
            print(blueWins + str(BlueWinTimes))
            print(redWins + str(RedWinTimes))
        else:            
            RedWinTimes = RedWinTimes + 1
            print("Red Wins! Red Wins! Red Wins! Red Wins!")
            print(blueWins + str(BlueWinTimes))
            print(redWins + str(RedWinTimes))
            
    else:
        #button press was invalid, opponent wins!
        winner = blue if btn == btnR else red

        #print the winner and number of times they won
        if winner == blue:            
            BlueWinTimes = BlueWinTimes + 1
            print("Blue Wins! Blue Wins! Blue Wins! Blue Wins!")
            print(blueWins + str(BlueWinTimes))
            print(redWins + str(RedWinTimes))
        else:            
            RedWinTimes = RedWinTimes + 1
            print("Red Wins! Red Wins! Red Wins! Red Wins!")
            print(blueWins + str(BlueWinTimes))
            print(redWins + str(RedWinTimes))

    # flash winning color 5 time    
    RGB.blink(on_color = winner, n = 5, background = 0)


def play_game():
    #play the game, loop until a button is pressed
    btnPressed = False
    while btnPressed == False:

        # select a random color
        ledColor = random.choice([red, green, blue])

        #play through one color cycle
        RGB.color = ledColor    #turn on LED
        btnPressed = monitorButtons(1)  #monitor buttons
    return

def main():
    
    try:
        while True:
            play_game()
            
    except KeyboardInterrupt:
        pass


main()

