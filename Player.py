class Player:
  def __init__(self):
    self.money = 25.00
    self.supplies = [0, 0, 0, 0] #L to R: scoops, cones, fruits, sprinkles
    self.scoops = 2 #Recipe?
    self.cones = 1
    self.fruits = 3
    self.sprinkles = 10
    self.price = 4.00
    
  def set_money(self, new_money):
    self.money += float(new_money)

  def get_money(self):
    return self.money

  def get_supplies(self, index):
    return self.supplies[index]

  def set_supplies(self, index, amount):
    if (index == "I"): #Set to proper index based on letter input
      index = 0
    elif (index == "C"):
      index = 1
    elif (index == "F"):
      index = 2
    elif (index == "S"):
      index = 3
    #If not given as letter, go straight to this
    self.supplies[index] += int(amount)
    
     
