from MainMenu import *

#Variables
player_name = ""
stand_name = ""
run_main = MainMenu(1) #Create main menu object


def intro(): #Get player name and stand name
    player_name = str(input("What is your name? "))
    stand_name = str(input("What is the name of your stand? "))
    #tutorial_question = str(input("Do you need a tutorial? ")).upper()
    #if tutorial_question == "Y":
    #    return True
    #if tutorial_question == "N":
    #    return False





def main(): #Run everything in order
    intro()
    game_running = True
    
    while game_running:
        print("You are currently managing " + stand_name)
        run_main.menu()

        if (run_main.get_day() == 31): #Ends at 30
            #Outro here
            game_running = False
    
    
main() #Run