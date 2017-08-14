from functools import partial

# Hello World!
print("Hello World!")

# Assignment
theHello = "Hello World!"
print(theHello)

# Parameters
class helloClass():
	def __init__(self, str):
		print(str)

inStr = "Hello from the method!"
theCall = helloClass(inStr)

# Parameters / Operators
class twoNums():
	def __init__(self):
		pass
		
	def theSum(self, num1, num2):
		return num1 + num2

numCall = twoNums()
print(numCall.theSum(2, 3))

# Conditionals
class twoNumsCond():
	def __init__(self):
		pass
		
	def theSum(self, num1, num2, isTrue):
		if(isTrue == True):
			return num1 + num2
		elif(isTrue == False):
			return num1 * num2
		else:
			print("An error occured.")

condCall = twoNumsCond()
print(condCall.theSum(2, 3, True))
print(condCall.theSum(2, 3, False))

# Conditionals 2
class twoNumsCondZero():
	def __init__(self):
		pass
		
	def theSum(self, num1, num2, isTrue):
		if(num1 == 0):
			return num2
		elif(num2 == 0):
			return num1
		elif(isTrue == True):
			return num1 + num2
		elif(isTrue == False):
			return num1 * num2
		else:
			print("An error occured.")

condCall = twoNumsCondZero()
print(condCall.theSum(1, 0, True))
print(condCall.theSum(1, 2, True))

# Recursion
for x in range (0, 10):
	print(condCall.theSum(x, 2, False))
	
# Lists
theList = [0,1,2,3,4,5,6,7,8,9]
print(condCall.theSum(theList[0], theList[3], True))
print(condCall.theSum(theList[4], theList[0], True))
print(condCall.theSum(theList[4], theList[6], False))

# Recursion / Lists (1)
for x in range (0, len(theList)):
	print(theList[x])

# Recursion / Lists (2)
loopList = []
for x in range (0, 10):
	loopList.append(x)
	print(loopList[x])

for y in range (0, len(loopList)):
	loopList[y] = loopList[y] * 10
	print(loopList[y])
	
# User Input
inputList = []
theRange = int(input("Enter a number: "))

for x in range (0, theRange):
	inputList.append(x)
	print(inputList[x])

for y in range (0, len(inputList)):
	inputList[y] = inputList[y] * 10
	print(inputList[y])
	
# Partial Functions
def multiply(x, y):
	return x * y
	
double = partial(multiply, 2)
triple = partial(multiply, 3)

print(double(5))
print(triple(5))