# Tic Tac Toe
import random

#globals
p1 = 'X'
p2 = 'O'

# Print out board
def display_board(board):
	
	print('    |   |')
	print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('    |   |')
	print(' ------------')
	print('    |   |')
	print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('    |   |')
	print(' ------------')
	print('    |   |')
	print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('    |   |')
	

	
"""
Receives user input for move to make. If move outside of range,
then return print statement, then ask for another move.
"""
def player_input():
	print("Please choose your move")
	move = int(input())
	if move in range(0, 10): return move
	else:
		print("Move not within range")
		return player_input()
	

# Place marker on the board
def place_marker(board, marker, position):
	# Cycle through the board to find the position
	if space_check(board, position):
		board[position] = marker
		#return board
	else:
		print("Space not available, choose another one")
		nm = int(input())
		place_marker(board, marker, nm)
	

"""
Returns True if 'X' or 'O' has won the game, False
if there's no winner
"""
def win_check(board, mark):
	# Check horizontally
	if ((board[1] == board[2] == board[3] == mark) or
	 (board[4] == board[5] == board[6] == mark) or
	 (board[7] == board[8] == board[9] == mark) or
	
	#Check vertically
	(board[1] == board[4] == board[7] == mark) or
	 (board[2] == board[5] == board[8] == mark) or
	 (board[3] == board[6] == board[9] == mark) or
	
	#Check diagonally
	 (board[1] == board[5] == board[9] == mark) or
	 (board[3] == board[5] == board[7] == mark)):
		return True
	
	#None of the patterns matched (No winner yet)
	else: return False 
	
	
# Randomly chooses if p1 or p2 goes first
def choose_first():
	n = range(1, 3)
	player = random.choice(n)
	if player == 1: return p1
	return p2
	
"""
Returns True if that specific board space is empty, False if 
a player has already chosen that spot.

"""
def space_check(board, pos):
	return board[pos] == ' '

	
"""
Returns True if board is full (ie no empty spaces),
False if otherwise.
"""
def board_check(board):
	for space in range(1, 10):
		if space_check(board, space): return False
	return True
	

"""
Function that returns true if user inputs 'y' to repeat the game,
False if any other character.
"""
def replay():
	print("Would you like to play again?")
	print("\n Hit 'Y' or 'N'" )
	# take in user input 
	choice = str(input()).upper()
	return choice == 'Y'
	
def gameOn():
# Running the game
	print("Let's play Tic Tac Toe!")
	
	board = [' '] * 10
	cont = True
	# Decide which player goes first
	player = choose_first()
	
	while cont:
		
		print("Player {0} choose your move:".format(player))
		choice = int(player_input())
		place_marker(board, player, choice)
		
		display_board(board)
		
		print("Player chooses:", + choice)
		
		# Check if current player has won with their move
		if win_check(board, player) == True:
			print("Player {0} won!".format(player))
			cont = False
				
			#break
			
		else: 
			#Check for blank board
			if board_check(board):
				print("It's a draw!")
				break
			# Swap players
			else: player = p1 if player == p2 else p2
	
	if not replay(): return
# Testing code
gameOn()