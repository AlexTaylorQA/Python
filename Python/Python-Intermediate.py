# Blackjack
class blackjack():
	def __init__(self):
		pass
		
	def theCheck(self, num1, num2):
		if(num1 > 21 and num2 > 21):
			return str(0) + ": Both numbers exceeded 21."
		elif (num1 <= 0 or num2 <= 0):
			return str(0) + ": Please enter valid numbers above 0."
		elif(num1 > 21 and num2 <= 21):
			return str(num2) + " was the highest number! (" + num1 + " went over 21)"
		elif(num1 <= 21 and num2 > 21):
			return str(num1) + " was the highest number! (" + num2 + " went over 21)"
		elif(num1 > num2):
			return str(num1) + " was the highest number!"
		elif(num2 > num1):
			return str(num2) + " was the highest number!"
		elif(num1 == num2):
			return "The numbers were equal to one another."
		else:
			print("An error occured.")	
			
bjCall = blackjack()
print(bjCall.theCheck(18,21))
print(bjCall.theCheck(20,18))
print(bjCall.theCheck(22,22))

# Unique Sum
class uniqueSum():
	def __init__(self):
		pass
		
	def theCheck(self, num1, num2, num3):
		if(num1 == num2 and num2 == num3):
			return 0
		elif(num1 == num2):
			return num3
		elif(num2 == num3):
			return num1
		elif(num1 == num3):
			return num2
		else:
			return num1 + num2 + num3

uSumCall = uniqueSum()
print(uSumCall.theCheck(1,2,3))
print(uSumCall.theCheck(3,3,3))
print(uSumCall.theCheck(1,1,2))

# Too Hot?
class tooHot():
	def __init__(self):
		pass
		
	def theCheck(self, temperature, isSummer):
		theMax = 0
		if(isSummer == False):
			theMax = 90
		else:
			theMax = 100
		
		if(temperature >= 60 and temperature <= theMax):
			return True
		else:
			return False

tooHotCall = tooHot()
print(tooHotCall.theCheck(20, True))
print(tooHotCall.theCheck(95, True))
print(tooHotCall.theCheck(95, False))

# Leap Year
class leapYear():
	def __init__(self):
		pass
		
	def theCheck(self, theYear):
		if(theYear % 4 == 0 and (theYear % 400 == 0 or theYear % 100 != 0)):
			return True
		else:
			return False
			
leapCall = leapYear()
print(leapCall.theCheck(1996))
print(leapCall.theCheck(1997))
print(leapCall.theCheck(1998))
print(leapCall.theCheck(1999))
print(leapCall.theCheck(2000))
print(leapCall.theCheck(2001))

# Paint Wizard
class paintWizard():
	def __init__(self, theName, litres, cost, coverage):
		self.theName = theName
		self.litres = litres
		self.cost = cost
		self.coverage = coverage
		
	def theCost(self, roomSize):
		totalCoverage = self.coverage * self.litres
		cansCoverage = 0
		numCans = 0
		while(cansCoverage < roomSize):
			cansCoverage += totalCoverage
			numCans += 1
		return(numCans * self.cost)
		
can1 = paintWizard("CheapoMax", 20.0, 19.99, 10)
can2 = paintWizard("Average Joes", 15.0, 17.99, 11)
can3 = paintWizard("DuluxourousPaints", 10.0, 25.0, 20)

canList = [can1, can2, can3]
roomSizes = [165,175,200,450,1000]

for y in range (0, len(roomSizes)):
	canList.sort(key=lambda x: x.theCost(roomSizes[y]), reverse=False)
	print(canList[0].theName + " is the cheapest brand for a " + str(roomSizes[y]) + "m² room.\nIt costs: £" + str(canList[0].theCost(roomSizes[y])) + "\n")
	
# Working with Files
class thePerson():
	def __init__(self, theName, occupation, theAge):
		self.theName = theName
		self.occupation = occupation
		self.theAge = theAge
	
p1 = thePerson("Alan", "Consultant", 42)
p2 = thePerson("Beth", "Analyst", 36)
p3 = thePerson("Cole", "Developer", 53)
p4 = thePerson("Dave", "Strategist", 24)
p5 = thePerson("Evan", "Manager", 61)

personList = [p1,p2,p3,p4,p5]

file = open("file.txt", "w+")
file.write("")
file.close()

for x in range (0, len(personList)):
	file = open("file.txt", "a")
	file.write(personList[x].theName + ", " + personList[x].occupation + ", " + str(personList[x].theAge) + "\n")
	file.close()

dataList = []
file = open("file.txt", "r")
lines = file.read().splitlines()
dataList = lines
print(dataList)
