class MainMenu:  
    def __init__(self, day_number): #Constructor
        self.day_number = day_number

    def menu(self):
        print("It is day " + str(self.day_number))
        self.day_number += 1
    

    def get_day(self):
    	return self.day_number

    def day(self):
        pass
    
