class MainMenu:  
    def __init__(self, day_number): #Constructor
        self.day_number = day_number
        self.options = ["B - Buy Supplies", "S - Set Recipe and Prices", "V - View Career", "Q - Quit Game", "A - Advance to Day"]
        self.commands = ["B", "S", "V", "A", "Q"]


    def menu(self): #Run the menu and its options
        print("It is day " + str(self.day_number))
        self.list_options()

        user_in = str(input("Which action would you like to take? ")).upper()
        while user_in not in self.commands: #While not a valid action, repeat the question
        	user_in = str(input("Invalid action. Enter one of BSVA: ")).upper()
        return user_in #Return the user's choice

    
    def list_options(self): #Print out all of the options for the user
    	for elem in self.options:
    		print(elem)

    
    def inc_day(self): #Run the day and all of its actions
    	self.day_number += 1

 
