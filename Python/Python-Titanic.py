import csv

class getFile:
	def __init__(self):
		with open('titanic.csv') as csvfile:
			theRecords = [[],[],[],[],[],[],[],[],[],[],[],[]]
			reader = csv.DictReader(csvfile)
			for row in reader:
				theRecords[0].append(row['PassengerId'])
				theRecords[1].append(row['Survived'])
				theRecords[2].append(row['Pclass'])
				theRecords[3].append(row['Name'])
				theRecords[4].append(row['Sex'])
				theRecords[5].append(row['Age'])
				theRecords[6].append(row['SibSp'])
				theRecords[7].append(row['Parch'])
				theRecords[8].append(row['Ticket'])
				theRecords[9].append(row['Fare'])
				theRecords[10].append(row['Cabin'])
				theRecords[11].append(row['Embarked'])
				
			theMenu(theRecords)

class theMenu:
	def __init__(self, theRecords):
		self.theRecords = theRecords
		theOption = int(input("\n\nSelect an option: "
			+ "\n 1 - Count No. of Missing Values in Each Column"
			+ "\n 2 - Add Missing Values to Data Set"
			+ "\n\n"
			))
			
		if(theOption == 1):
			doTask.one(theRecords)
		elif(theOption == 2):
			doTask.two(theRecords)

class doTask:
	def one(theRecords):
		theCount = [0,0,0,0,0,0,0,0,0,0,0,0]
		for y in range(0, len(theCount)):
			for x in range(0, len(theRecords[0])):
				if str(theRecords[y][x]) == "":
					theCount[y] += 1
				
		print("\nMissing PassengerId: " + str(theCount[0]) 
		+ "\nMissing Survived: " + str(theCount[1])
		+ "\nMissing Pclass: " + str(theCount[2])
		+ "\nMissing Name: " + str(theCount[3])
		+ "\nMissing Sex: " + str(theCount[4])
		+ "\nMissing Age: " + str(theCount[5])
		+ "\nMissing SibSp: " + str(theCount[6])
		+ "\nMissing Parch: " + str(theCount[7])
		+ "\nMissing Ticket: " + str(theCount[8])
		+ "\nMissing Fare: " + str(theCount[9])
		+ "\nMissing Cabin: " + str(theCount[10])
		+ "\nMissing Embarked: " + str(theCount[11])
		)
		
		theMenu(theRecords)

	def two(theRecords):
		for y in range(0, len(theRecords)):
			for x in range(0, len(theRecords[y])):
				if str(theRecords[y][x]) == "":
					if y == 0:
						theID = 0
						for z in range(0, len(theRecords[0])):
							if theID < theRecords[y][z]:
								theID = theRecords[y][z] + 1
								
					elif y == 1:
						theRecords[y][x] = 0
					
					elif y == 2:
						theRecords[y][x] = 3
					
					elif y == 3:
						theRecords[y][x] = "Doe, Mr. John"
					
					elif y == 4:
						theRecords[y][x] = "unknown"
						
					elif y == 5:
						theRecords[y][x] = "unknown"
					
					elif y == 6:
						theRecords[y][x] = 0
					
					elif y == 7:
						theRecords[y][x] = 0
					
					elif y == 8:
						from random import randint
						theRecords[y][x] = randint(0, 1000000)
					
					elif y == 9:
						theTotal = 0.0
						for w in range(0, len(theRecords[y])):
							theTotal += theRecords[y][w]
						
						theAvg = theTotal / len(theRecords[y])
						
						theRecords[y][x] = theAvg
					
					elif y == 10:
						theRecords[y][x] = "None"
					
					elif y == 11:
						theRecords[y][x] = "n/a"
						
		print("\nMissing data has been accounted for.")
		theMenu(theRecords)
	
	def three(theRecords):
		
	
getFile()
			
			
#for row in reader:
#	print(row['Name'], row['Sex'])