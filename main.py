row1 = []
emptyrow1 = []
row2 = []
emptyrow2 = []
row3 = []

print("You are X, Bot is O\n")

def playAgain():
	playAgain = input("Do you want to play again?\n")
	if playAgain in ('Yes', 'y', 'Y', 'yes'):
		startGame()
	elif playAgain in ('No', 'n', 'N', 'no'):
		quit()
	else:
		print("Invalid Selection\n")
		playAgain()

def win():
	printBoard()
	print("You win!\n")
	playAgain()

def lose():
	printBoard()
	print("You lose!\n")
	playAgain()

def checkWin():
	global row1, row2, row3
	if row1[0] in ('X', 'O') and row1[1] in ('X', 'O') and row1[2] in ('X', 'O'):
		if row1[0] == 'X':
			win()
		else:
			lose()
	elif row2[0] in ('X', 'O') and row2[1] in ('X', 'O') and row2[2] in ('X', 'O'):
		if row2[0] == 'X':
			win()
		else:
			lose()
	elif row3[0] in ('X', 'O') and row3[1] in ('X', 'O') and row3[2] in ('X', 'O'):
		if row3[0] == 'X':
			win()
		else:
			lose()

	if row1[0] in ('X', 'O') and row2[0] in ('X', 'O') and row3[0] in ('X', 'O'):
		if row1[0] == 'X':
			win()
		else:
			lose()
	elif row1[1] in ('X', 'O') and row2[1] in ('X', 'O') and row3[1] in ('X', 'O'):
		if row1[1] == 'X':
			win()
		else:
			lose()
	elif row1[2] in ('X', 'O') and row2[2] in ('X', 'O') and row3[2] in ('X', 'O'):
		if row1[2] == 'X':
			win()
		else:
			lose()

def printBoard():
	global row1, emptyrow1, row2, emptyrow2, row3
	print(row1)
	print(emptyrow1)
	print(row2)
	print(emptyrow2)
	print(row3)

def startGame():
	global row1, emptyrow1, row2, emptyrow2, row3
	row1 = ['_', '_', '_']
	emptyrow1 = ['           ']
	row2 = ['_', '_', '_']
	emptyrow2 = ['           ']
	row3 = ['_', '_', '_']
	turn()

def botTurn():
	print("Bot's move\n")
	global row1, row2, row3
	checkWin()
	if row2[1] == '_':
		row2[1] == 'O'
	printBoard()
	turn()

def turn():
	print("Your move\n")
	checkWin()
	printBoard()
	placex = input("Where would you like to go? (x)\n")
	placey = input("Where would you like to go? (y)\n")
	try:
		placex = int(placex)
		placey = int(placey)
	except ValueError:
		print("Not a number\n")
		turn()

	if placey == 1:
		if row1[placex - 1] in ('X', 'O'):
			print("Space already occupied!\n")
			turn()
		row1[placex - 1] = 'X'
	elif placey == 2:
		if row2[placex - 1] in ('X', 'O'):
			print("Space already occupied!\n")
			turn()
		row2[placex - 1] = 'X'
	else:
		if row3[placex - 1] in ('X', 'O'):
			print("Space already occupied!\n")
			turn()
		row3[placex - 1] = 'X'

	botTurn()

startGame()
printBoard()





