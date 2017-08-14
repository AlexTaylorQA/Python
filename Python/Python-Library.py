# Entry point
class toStart():
	def __init__(self, theLibrary):
		self.theLibrary = theLibrary
		theInput = input("\n=====\n\nPlease select an option:"
		+ "\n 1 - Enter the Library"
		+ "\n 2 - Import a Library"
		+ "\n 3 - Export the Library"
		+ "\n 4 - Quit\n\n")
		if(int(theInput) not in range (1, 5)):
			print("\n=====\n\nPlease input a valid option.\n")
			toStart(theLibrary)
		else:
			if(int(theInput) == 1):
				theMenu(theLibrary)
			
			elif(int(theInput) == 2):
				theLibrary.bookList = []
				theLibrary.mediaList = []
				theLibrary.mapList = []
				theLibrary.personList = []
			
				file = open("library.txt", "r")
				theFile = file.read().split("\n")
				for x in range(0, len(theFile)):
					theItem = theFile[x].split("-/-")
					if(theItem[0] == "Book"):
						theLibrary.bookList.append(Book(theItem[1], theItem[2], theItem[3], theItem[4], theItem[5]))
					elif(theItem[0] == "Media"):
						theLibrary.mediaList.append(Media(theItem[1], theItem[2], theItem[3]))
					elif(theItem[0] == "Map"):
						theLibrary.mapList.append(Map(theItem[1], theItem[2], theItem[3], theItem[4]))
					elif(theItem[0] == "Person"):
						theLibrary.personList.append(Person(theItem[1], theItem[2], theItem[3], theItem[4], theItem[5]))
				
				toStart(theLibrary)
						
			elif(int(theInput) == 3):
				file = open("library.txt", "w+")
				for e in theLibrary.bookList:
					file.write("Book-/-" + str(e.bID) + "-/-" + e.bTitle + "-/-" + e.bAuthor + "-/-" + e.bGenre + "-/-" + str(e.bCheckout) + "\n")
				for e in theLibrary.mediaList:
					file.write("Media-/-" + str(e.mID) + "-/-" + e.mType + "-/-" + str(e.mCheckout) + "\n")
				for e in theLibrary.mapList:
					file.write("Map-/-" + str(e.mapID) + "-/-" + e.mapRegion + "-/-" + e.mapDate + "-/-" + str(e.mapCheckout) + "\n")
				for e in theLibrary.personList:
					file.write("Person-/-" + str(e.pID) + "-/-" + e.pFirstName + "-/-" + e.pLastName + "-/-" + e.pDOB + "-/-" + e.pAddress + "\n")
				file.close()
				
				print("\n=====\n\nThe Library has been exported successfully.\n")
				toStart(theLibrary)
				
			elif(int(theInput) == 4):
				return

# Main menu
class theMenu():
	def __init__(self, theLibrary):
		self.theLibrary = theLibrary
		
		theInput = input("\n=====\n\nPlease select an option:"
		+ "\n 0 - Display Library Contents"
		+ "\n 1 - Check Out Item"
		+ "\n 2 - Check In Item"
		+ "\n 3 - Add Item"
		+ "\n 4 - Remove Item"
		+ "\n 5 - Update Item"
		+ "\n 6 - Register Person"
		+ "\n 7 - Delete Person"
		+ "\n 8 - Update Person"
		+ "\n 9 - Close Library"
		+ "\n\n"
		)
		if(int(theInput) not in range (0, 10)):
			print("\n=====\n\nPlease input a valid option.\n")
			theMenu(theLibrary) 
		else:
			if(int(theInput) == 0):
				theLibrary.displayAll()
				theMenu(theLibrary)
				
			elif(int(theInput) == 1):
				theLibrary.checkOut()
				theMenu(theLibrary)
				
			elif(int(theInput) == 2):
				theLibrary.checkIn()
				theMenu(theLibrary)
				
			elif(int(theInput) == 3):
				theLibrary.addItem()
				theMenu(theLibrary)
			
			elif(int(theInput) == 4):
				theLibrary.removeItem()
				theMenu(theLibrary)				
			
			elif(int(theInput) == 5):
				theLibrary.updateItem()
				theMenu(theLibrary)

			elif(int(theInput) == 6):
				theLibrary.newPerson()
				theMenu(theLibrary)
			
			elif(int(theInput) == 7):
				theLibrary.deletePerson()
				theMenu(theLibrary)
				
			elif(int(theInput) == 8):
				theLibrary.updatePerson()
				theMenu(theLibrary)
				
			elif(int(theInput) == 9):
				toStart(theLibrary)
				
# Library class				
class Library():
	def __init__(self, bookList, mediaList, mapList, personList):
		self.bookList = bookList
		self.mediaList = mediaList
		self.mapList = mapList
		self.personList = personList
	
	# Option 0
	def displayAll(self):
		zeroInput = input("\n=====\n\nPlease select an option:"
				+ "\n 1 - Display All Books"
				+ "\n 2 - Display All Media"
				+ "\n 3 - Display All Maps"
				+ "\n 4 - Display All People"
				+ "\n\n"
				)
		if(int(zeroInput) not in range (1, 5)):
			print("\n=====\n\nPlease input a valid option.\n")

		else:
			if(int(zeroInput) == 1):
				if(len(self.bookList) == 0):
					print("\n=====\n\nNo books found.\n")
				else:
					print("\nBooks:\n======\n")
					for x in range (0, len(self.bookList)):
						print("BookID: " + str(self.bookList[x].bID) + "\nTitle:  " + self.bookList[x].bTitle + "\nAuthor: " + self.bookList[x].bAuthor + "\nGenre:  " + self.bookList[x].bGenre + "\nStatus: " + self.bookList[x].doCheck() + "\n")
	
			elif(int(zeroInput) == 2):
				if(len(self.mediaList) == 0):
					print("\n=====\n\nNo media found.\n")
				else:
					print("\nMedia:\n======\n")
					for x in range (0, len(self.mediaList)):
						print("MediaID: " + str(self.mediaList[x].mID) + "\nType:    " + self.mediaList[x].mType + "\nStatus:  " + self.mediaList[x].doCheck() + "\n")
		
			elif(int(zeroInput) == 3):
				if(len(self.mapList) == 0):
					print("\n=====\n\nNo maps found.\n")
				else:
					print("\nMaps:\n======\n")
					for x in range (0, len(self.mapList)):
						print("MapID: " + str(self.mapList[x].mapID) + "\nRegion: " + self.mapList[x].mapDate + "\nStatus:  " + self.mapList[x].doCheck() + "\n")
	
			elif(int(zeroInput) == 4):
				if(len(self.personList) == 0):
					print("\n=====\n\nNo people found.\n")
				else:
					print("\nPeople:\n======\n")
					for x in range(0, len(self.personList)):
						print("PersonID: " + str(self.personList[x].pID) + "\nName:     " + self.personList[x].pFirstName + " " + self.personList[x].pLastName + "\nD.O.B.:   " + self.personList[x].pDOB + "\nAddress:  " + self.personList[x].pAddress + "\n")
	
	# Option 1
	def checkOut(self):
		oneInput = input("\n=====\n\nPlease select an option:"
				+ "\n 1 - Check out a Book"
				+ "\n 2 - Check out Media"
				+ "\n 3 - Check out a Map"
				+ "\n\n"
				)
				
		if(int(oneInput) not in range (1, 4)):
			print("\n=====\n\nPlease input a valid option.\n")

		else:
			theID = int(input("\n=====\n\nPlease enter an ID.\n\n"))
			if(int(oneInput) == 1):
				for x in range (0, len(self.bookList)):
					if(self.bookList[x].bID == theID):
						if(self.bookList[x].bCheckout == True):
							print("\n=====\n\nThis book is already checked out.\n")
						else:
							self.bookList[x].bCheckout = True
							print("\n=====\n\nThe book has been checked out successfully.\n")
							
			elif(int(oneInput) == 2):
				for x in range (0, len(self.mediaList)):
					if(self.mediaList[x].mID == theID):
						if(self.mediaList[x].mCheckout == True):
							print("\n=====\n\nThis media is already checked out.\n")
						else:
							self.mediaList[x].mCheckout = True
							print("\n=====\n\nThe media has been checked out successfully.\n")
							
			elif(int(oneInput) == 3):
				for x in range (0, len(self.mapList)):
					if(self.mapList[x].mapID == theID):
						if(self.mapList[x].mapCheckout == True):
							print("\n=====\n\nThis map is already checked out.\n")
						else:
							self.mapList[x].mapCheckout = True
							print("\n=====\n\nThe map has been checked out successfully.\n")
	
# Option 2	
	def checkIn(self):
		twoInput = input("\n=====\n\nPlease select an option:"
				+ "\n 1 - Check in a Book"
				+ "\n 2 - Check in Media"
				+ "\n 3 - Check in a Map"
				+ "\n\n"
				)
				
		if(int(twoInput) not in range (1, 4)):
			print("\n=====\n\nPlease input a valid option.\n")

		else:
			theID = int(input("\n=====\n\nPlease enter an ID.\n\n"))
			if(int(twoInput) == 1):
				for x in range (0, len(self.bookList)):
					if(self.bookList[x].bID == theID):
						if(self.bookList[x].bCheckout == False):
							print("\n=====\n\nThis book is already checked in.\n")
						else:
							self.bookList[x].bCheckout = False
							print("\n=====\n\nThe book has been checked in successfully.\n")
							
			elif(int(twoInput) == 2):
				for x in range (0, len(self.mediaList)):
					if(self.mediaList[x].mID == theID):
						if(self.mediaList[x].mCheckout == False):
							print("\n=====\n\nThis media is already checked in.\n")
						else:
							self.mediaList[x].mCheckout = False
							print("\n=====\n\nThe media has been checked in successfully.\n")
							
			elif(int(twoInput) == 3):
				for x in range (0, len(self.mapList)):
					if(self.mapList[x].mapID == theID):
						if(self.mapList[x].mapCheckout == False):
							print("\n=====\n\nThis map is already checked in.\n")
						else:
							self.mapList[x].mapCheckout = False
							print("\n=====\n\nThe map has been checked in successfully.\n")
	
	# Option 3
	def addItem(self):
		threeInput = input("\n=====\n\nPlease select an option:"
				+ "\n 1 - Add a new Book"
				+ "\n 2 - Add new Media"
				+ "\n 3 - Add a new Map"
				+ "\n\n"
				)

		if(int(threeInput) not in range (1, 4)):
			print("\n=====\n\nPlease input a valid option.\n")

		else:
			theID = 0
			
			if(int(threeInput) == 1):
				for x in range(0, len(self.bookList)):
					if(self.bookList[x].bID > theID):
						theID = (self.bookList[x].bID + 1)
				
				theTitle = input("\nEnter the new book's title.\n\n")
				theAuthor = input("\nEnter the new book's author.\n\n")
				theGenre = input("\nEnter the new book's genre.\n\n")
				
				theBook = Book(theID, theTitle, theAuthor, theGenre, False)
				self.bookList.append(theBook)
				print("\n=====\n\nThe book has been added successfully.\n")
							
			elif(int(threeInput) == 2):
				for x in range(0, len(self.mediaList)):
					if(self.mediaList[x].mID > theID):
						theID = (self.mediaList[x].mID + 1)
				
				theType = input("\nEnter the new media's type.\n\n")

				theMedia = Media(theID, theType, False)
				self.mediaList.append(theMedia)
				print("\n=====\n\nThe media has been added successfully.\n")
							
			elif(int(threeInput) == 3):
				for x in range(0, len(self.mapList)):
					if(self.mapList[x].mapID > theID):
						theID = (self.mapList[x].mapID + 1)
				
				theRegion = input("\nEnter the new map's region.\n\n")
				theDate = input("\nEnter the new map's date.\n\n")
			
				theMap = Map(theID, theRegion, theDate, False)
				self.mapList.append(theMap)
				print("\n=====\n\nThe map has been added successfully.\n")
	
	# Option 4
	def removeItem(self):
		fourInput = input("\n=====\n\nPlease select an option:"
				+ "\n 1 - Remove a Book"
				+ "\n 2 - Remove Media"
				+ "\n 3 - Remove a Map"
				+ "\n\n"
				)
				
		if(int(fourInput) not in range (1, 4)):
			print("\n=====\n\nPlease input a valid option.\n")

		else:	
			if(int(fourInput) == 1):
				theID = int(input("\nEnter the ID of the book.\n\n"))
				for x in range(0, len(self.bookList)):
					if(self.bookList[x].bID == theID):
						self.bookList.remove(self.bookList[x])
						print("\n=====\n\nThe book has been removed successfully.\n")
						break
					break

			elif(int(fourInput) == 2):	
				theID = int(input("\nEnter the ID of the media.\n\n"))
				for x in range(0, len(self.mediaList)):
					if(self.mediaList[x].mID == theID):
						self.mediaList.remove(self.mediaList[x])
						print("\n=====\n\nThe media has been removed successfully.\n")
						break
					break
					
			elif(int(fourInput) == 3):
				theID = int(input("\nEnter the ID of the map.\n\n"))
				for x in range(0, len(self.mapList)):
					if(self.mapList[x].mapID == theID):
						self.mapList.remove(self.mapList[x])
						print("\n=====\n\nThe map has been removed successfully.\n")
						break
					break
	
	# Option 5
	def updateItem(self):
		fiveInput = input("\n=====\n\nPlease select an option:"
				+ "\n 1 - Update a Book"
				+ "\n 2 - Update Media"
				+ "\n 3 - Update a Map"
				+ "\n\n"
				)

		if(int(fiveInput) not in range (1, 4)):
			print("\n=====\n\nPlease input a valid option.\n")

		else:

			if(int(fiveInput) == 1):
				theID = int(input("\nEnter the ID of the book.\n\n"))
				for x in range(0, len(self.bookList)):
					if(self.bookList[x].bID == theID):				
						theTitle = input("\nEnter the book's updated title.\n\n")
						theAuthor = input("\nEnter the book's updated author.\n\n")
						theGenre = input("\nEnter the book's updated genre.\n\n")
						
						self.bookList[x].bTitle = theTitle
						self.bookList[x].bAuthor = theAuthor
						self.bookList[x].bGenre = theGenre
						print("\n=====\n\nThe book has been updated successfully.\n")
							
			if(int(fiveInput) == 2):
				theID = int(input("\nEnter the ID of the media.\n\n"))
				for x in range(0, len(self.mediaList)):
					if(self.mediaList[x].mID == theID):				
						theType = input("\nEnter the media's updated type.\n\n")
						
						self.mediaList[x].mType = theType
						print("\n=====\n\nThe media has been updated successfully.\n")
							
			elif(int(fiveInput) == 3):
				theID = int(input("\nEnter the ID of the map.\n\n"))
				for x in range(0, len(self.mapList)):
					if(self.mapList[x].mapID == theID):				
						theRegion = input("\nEnter the map's updated region.\n\n")
						theDate = input("\nEnter the map's updated date.\n\n")
						
						self.mapList[x].mapRegion = theRegion
						self.mapList[x].mapDate = theDate
						print("\n=====\n\nThe map has been updated successfully.\n")
	
	# Option 6
	def newPerson(self):
		theID = 0
		
		for x in range(0, len(self.personList)):
			if(self.personList[x].pID > theID):
				theID = (self.personList[x].pID + 1)
		
		theFirstName = input("\nEnter the new person's first name.\n\n")
		theLastName = input("\nEnter the new person's last name.\n\n")
		theDOB = input("\nEnter the new person's date of birth.\n\n")
		theAddress = input("\nEnter the new person's address.\n\n")	
		
		thePerson = Person(theID, theFirstName, theLastName, theDOB, theAddress)
		print("\n=====\n\nThe person has been created successfully.\n")
		self.personList.append(thePerson)
	
	# Option 7
	def deletePerson(self):
		theID = int(input("\nEnter the ID of the person to be deleted.\n\n"))
		
		for x in range(0, len(self.personList)):
			if(self.personList[x].pID == theID):
				self.personList.remove(self.personList[x])
				print("\n=====\n\nThe person has been removed successfully.\n")
				break
			break

	# Option 8
	def updatePerson(self):
		theID = int(input("\nEnter the ID of the person to be updated.\n\n"))
		
		for x in range(0, len(self.personList)):
			if(self.personList[x].pID == theID):

				self.personList[x].pFirstName = input("\nEnter the person's updated first name.\n\n")
				self.personList[x].pLastName = input("\nEnter the person's updated last name.\n\n")
				self.personList[x].pDOB = input("\nEnter the person's updated date of birth.\n\n")
				self.personList[x].pAddress = input("\nEnter the person's updated address.\n\n")
				print("\n=====\n\nThe person has been updated successfully.\n")
				
# Book class
class Book():
	def __init__(self, bID, bTitle, bAuthor, bGenre, bCheckout):
		self.bID = bID
		self.bTitle = bTitle
		self.bAuthor = bAuthor
		self.bGenre = bGenre
		self.bCheckout = bCheckout
		
	def doCheck(self):
		if(self.bCheckout == True):
			return "Checked Out"
		else:
			return "Checked In"

# Media class
class Media():
	def __init__(self, mID, mType, mCheckout):
		self.mID = mID
		self.mType = mType
		self.mCheckout = mCheckout
	
	def doCheck(self):
		if(self.mCheckout == True):
			return "Checked Out"
		else:
			return "Checked In"
			
# Map class
class Map():
	def __init__(self, mapID, mapRegion, mapDate, mapCheckout):
		self.mapID = mapID
		self.mapRegion = mapRegion
		self. mapDate = mapDate
		self.mapCheckout = mapCheckout
	
	def doCheck(self):
		if(self.mapCheckout == True):
			return "Checked Out"
		else:
			return "Checked In"

# Person class
class Person():
	def __init__(self, pID, pFirstName, pLastName, pDOB, pAddress):
		self.pID = pID
		self.pFirstName = pFirstName
		self.pLastName = pLastName
		self.pDOB = pDOB
		self.pAddress = pAddress
		
# Main code body
bookList = []
mediaList = []
mapList = []
personList = []

theLibrary = Library(bookList, mediaList, mapList, personList)

toStart(theLibrary)