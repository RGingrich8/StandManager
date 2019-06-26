class Shop:
	def __init__(self, ice_cream, cones, fruits, sprinkles, player):
		self.ice_cream = ice_cream #Cost
		self.cones = cones #Cost
		self.fruits = fruits #Cost
		self.sprinkles = sprinkles #Cost
		self.names = ["Ice Cream Scoops", "Cones", "Fruits", "Sprinkles"]
		self.price_list = [self.ice_cream, self.cones, self.fruits, self.sprinkles]
		self.player = player

	def print_prices(self): #Print all of the available items and their prices
		for x in range(len(self.price_list)):
			if (len(str(self.price_list[x])) < 4): 
				my_print = str(self.price_list[x]) + "0" #Add an extra 0 (formatting)
			else:
				my_print = str(self.price_list[x])
			print(self.names[x] + " at a cost of $" + my_print + " per unit. You own " + str(self.player.get_supplies(x)) + ".")


	def buy(self):
		leave_shop = False #Keep the shop open until the user would like to leave
		while not leave_shop:
			print("\n\n>>>Items to be purchased<<<")
			self.print_prices()
			print("\nIn order to buy items, enter the first letter of that item followed directly by the amount you would like.\nExample: c200 would be 200 cones, s50 would be 50 sprinkles. Use 'b' to leave the shop.")
			print("You have $" + str(self.player.get_money()))
			player_in = str(input("Enter what you would like: "))
			while (player_in == ""): #Empty input
				player_in = str(input("Invalid format: "))
			try: #Check formatting
				letter = player_in[0].upper()
				amount = player_in[1:]
				if (letter == "B"): #Leave the shop
					leave_shop = True #End the loop
				else:
					checkout = self.cost_calculation(letter, float(amount)) #Calculate cost
					if checkout > self.player.get_money(): #Cost of items is too much
						print("\nYou do not have the available funds to buy this.")
					else:
						self.player.set_money(-1 * checkout) #Subtract from user's money
						self.player.set_supplies(letter, amount) #Add the materials to the user
			except ValueError: #Invalid value type entered
				print("\nInvalid format\n")


	def cost_calculation(self, letter, amount): #Calculate the cost of the purchase
		if (letter == "I"):
			cost = self.ice_cream * amount
		elif (letter == "C"):
			cost = self.cones * amount
		elif (letter == "F"):
			cost = self.fruits * amount
		elif (letter == "S"):
			cost = self.sprinkles * amount
		return cost

'''
	def numCheck(text): #Checks to see if number is entered
	userNum = input(text)
	try:
		userNum = abs(int(userNum))
	except ValueError:
		print("Please enter a number.")
		userNum = numCheck(text)
	return userNum
'''