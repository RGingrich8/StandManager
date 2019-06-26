from MainMenu import *
from Shop import *
from Player import *

#Variables
run_main = MainMenu(1) #Create main menu object
player = Player() #Create player
the_shop = Shop(1.00, 0.75, 0.30, 0.10, player) #Initialize shop


def intro(): #Get player name and stand name
    #ADD INTRO MESSAGE HERE
    print("Intro message here:")
    p_n = str(input("What is your name? "))
    while (p_n == ""): #Enter valid name
        p_n = str(input("Please enter your name: "))
    s_n = str(input("What will you name your stand? "))
    while (s_n == ""): #Enter valid name
        s_n = str(input("Please name your stand: "))
    return p_n, s_n


def main(): #Run everything in order
    player_name, stand_name = intro() #Set stand and player names
    game_running = True #Game runs
    
    while game_running:
        print("\nYou are currently managing " + stand_name)
        
        action_taken = run_main.menu()
        if (action_taken == "B"): #Buy
            the_shop.buy()
        elif (action_taken == "S"): #Set recipe
            pass
        elif (action_taken == "V"): #Career
            pass
        elif (action_taken == "A"): #Advance day
            pass
            run_main.inc_day() #End of day, add one
        elif (action_taken == "Q"):
            game_running = False


        if (run_main.day_number == 31): #Ends at 30
            #Outro here
            game_running = False
    
    
main() #Run