from MainMenu import *
from Shop import *

#Variables
run_main = MainMenu(1) #Create main menu object
the_shop = Shop(1.00, 0.75, 0.30, 0.10) #Initialize shop costs


def intro(): #Get player name and stand name
    p_n = str(input("What is your name? "))
    s_n = str(input("What is the name of your stand? "))
    return p_n, s_n


def main(): #Run everything in order
    player_name, stand_name = intro() #Set stand and player names
    game_running = True #Game runs
    
    while game_running:
        print("\nYou are currently managing " + stand_name)
        
        action_taken = run_main.menu()
        if (action_taken == "B"): #Buy
            print("\n\n>>>Items to be purchased<<<")
            the_shop.print_prices()
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