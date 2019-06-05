class Customer:
  def __init__(self) 
    self.upper1 = 15
    self.lower1 = 35
    self.weather = random.randint(-10, 35)
    self.reputation = 0
    self.num_people = random.randint(self.upper1, self.lower2)
    self.lower2 = 4.0
    self.upper2 = 6.0
    self.num_buyers = random.randint(self.upper2, self.lower2)
    
  def set_reputation(self, reputation): #Reputation changes the number of buyers out of the number of people
    if self.reputation >= 100:
      self.reputation = 100
    else:
      self.reputation = reputation
      self.upper2 += (self.reputation)/10
      self.lower2 += (self.reputation)/10
    
  def set_num_people(self, num_people): #Weather changes the upper/lower bounds of the number of the pople
    self.upper1 += self.weather
    self.lower1 += self.weather
    
  def prices(self, scoops, cones, fruits, sprinkles):
    self.upper2 += scoops + cones + fruits + sprinkles
    self.lower2 += scoops + cones + fruits + sprinkles
    return self.upper2, self.lower2
    
