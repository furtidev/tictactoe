import colorama
from colorama import Fore

colorama.init()

class Game:
	def __init__(self):
		# the game board itself. 
		self.board =	["-", "-", "-",
						 "-", "-", "-",
						 "-", "-", "-"]
		# check if the game is still running
		self.gameIsRunning = True
		# determine current player
		self.currentPlayer = "X"
		# winner
		self.winner = None

	# Init the game. 
	def initGame(self):
		print(Fore.MAGENTA + "++++++++++++++++++++++++++++++++++++++++")
		self.DisplayBoard()

		# main game loop
		while self.gameIsRunning:
			self.InputHandler(self.currentPlayer)
			self.checkGameOver()
			self.flipPlayer()

		# print who is the winner after game is over.
		if self.winner == "X" or self.winner == "O":
			print(f"{self.winner} wins.")

	# ASCII board. No graphics library needed. :)
	def DisplayBoard(self):
		print(Fore.CYAN + "-------------")
		# oh man what the hell is this o.o
		print(Fore.GREEN + f"| {Fore.RED}{self.board[0]}{Fore.GREEN} | {Fore.RED}{self.board[1]}{Fore.GREEN} | {Fore.RED}{self.board[2]}{Fore.GREEN} |\n| {Fore.RED}{self.board[3]}{Fore.GREEN} | {Fore.RED}{self.board[4]}{Fore.GREEN} | {Fore.RED}{self.board[5]}{Fore.GREEN} |\n| {Fore.RED}{self.board[6]}{Fore.GREEN} | {Fore.RED}{self.board[7]}{Fore.GREEN} | {Fore.RED}{self.board[8]}{Fore.GREEN} |")
		print(Fore.CYAN + "-------------")

	# Player Input Handler.
	def InputHandler(self, player):
		print(f"{Fore.RED}{player}'s turn")
		position = input(Fore.GREEN + "Choose position (1-9): ")

		# let's verify the position. (Check if the spot is empty or if the spot even exists)
		valid = False
		while not valid:
			while position not in ["1", "2", "3","4", "5", "6","7", "8", "9"]:
				position = input(Fore.GREEN + "Choose position (1-9): ")
			position = int(position) - 1

			if self.board[position] == "-":
				print(Fore.MAGENTA + "++++++++++++++++++++++++++++++++++++++++")
				valid = True
			else:
				print(Fore.RED + '❌ That spot is already filled. Choose Again.')

		self.board[position] = player
		self.DisplayBoard()

	# check if game is over.... i guess?????????
	def checkGameOver(self):
		self.checkWinner()
		self.checkTie()

	def checkWinner(self):
		row = self.check_row()
		column = self.check_column()
		diagonal = self.check_diagonal()

		if row != None:
			self.winner = row
		elif column != None:
			self.winner = column
		elif diagonal != None:
			self.winner = diagonal
		else:
			self.winner = None

	def check_row(self):
		row_1 = self.board[0] == self.board[1] == self.board[2] != "-"
		row_2 = self.board[3] == self.board[4] == self.board[5] != "-"
		row_3 = self.board[6] == self.board[7] == self.board[8] != "-"

		if row_1 or row_2 or row_3:
			self.gameIsRunning = False
		if row_1:
			return self.board[0]
		elif row_2:
			return self.board[3]
		elif row_3:
			return self.board[6]
		else:
			return None
	def check_column(self):
		column_1 = self.board[0] == self.board[3] == self.board[6] != "-"
		column_2 = self.board[1] == self.board[4] == self.board[7] != "-"
		column_3 = self.board[2] == self.board[5] == self.board[8] != "-"
		if column_1 or column_2 or column_3:
			self.gameIsRunning = False
		if column_1:
			return self.board[0]
		elif column_2:
			return self.board[1]
		elif column_3:
			return self.board[2]
		else:
			return None
	def check_diagonal(self):
		diagonal_1 = self.board[0] == self.board[4] == self.board[8] != "-"
		diagonal_2 = self.board[2] == self.board[4] == self.board[6] != "-"

		if diagonal_1 or diagonal_2:
			self.gameIsRunning = False
		if diagonal_1:
			return self.board[0]
		elif diagonal_2:
			return self.board[2]
		else:
			return None
	def checkTie(self):
		if "-" not in self.board:
			gameIsRunning = false
			return True
		else:
			return False

	# flip the player character to X -> 0 or vice versa.
	def flipPlayer(self):
		if self.currentPlayer == "X":
			self.currentPlayer = "O"
		elif self.currentPlayer == "O":
			self.currentPlayer = "X"
