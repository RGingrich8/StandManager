class Shop:
	def __init__(self, ice_cream, cones, fruits, sprinkles):
		self.ice_cream = ice_cream
		self.cones = cones
		self.fruits = fruits
		self.sprinkles = sprinkles
		self.names = ["Ice Cream Scoops", "Cones", "Fruits", "Sprinkles"]
		self.price_list = [self.ice_cream, self.cones, self.fruits, self.sprinkles]

	def print_prices(self): #Print all of the available items and their prices
		for x in range(len(self.price_list)):
			if (len(str(self.price_list[x])) < 4): 
				my_print = str(self.price_list[x]) + "0" #Add an extra 0 (formatting)
			else:
				my_print = str(self.price_list[x])
			print(self.names[x] + " at a cost of $" + my_print + " per unit")


	def buy(self):
		print("\nIn order to buy items, enter the first letter of that item followed directly by the amount you would like.\nExample: c200 would be 200 Cones, s50 would be 50 Sprinkles")
		player_in = str(input("Enter what you would like: "))
		#ADD A CHECK FOR VALID NUMBER + LETTER HERE, AND DO A COST CALCULATION
		letter = player_in[0].upper()
		amount = player_in[1:]
		#CHECK
		print(cost_calculation(letter, amount))
		#NOW SUBTRACT THIS FROM THE USER AMOUNT IN MAIN

	def cost_calculation(self, letter, amount):
		if (letter == "I"):
			cost = self.ice_cream * amount
		elif (letter == "C"):
			cost = self.cones * amount
		elif (letter == "F"):
			cost = self.fruits * amount
		elif (letter == "S"):
			cost = self.sprinkles * amount
		return cost