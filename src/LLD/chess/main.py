from __future__ import annotations

from collections import namedtuple
from dataclasses import dataclass, field
from pprint import pprint

from constants import GameStatus
from chess_pieces import BoardCell, Pawn, Rook, Bishop, King, Queen, Knight
from player import Player


@dataclass(unsafe_hash=True)
class Move:
	player: str
	old_position: list = field(default_factory=list, repr=False)
	new_position: list = field(default_factory=list, repr=False)
	piece_moved: Pawn | King | Queen | Bishop | Knight | Rook = None
	piece_killed: Pawn | King | Queen | Bishop | Knight | Rook = None
	castling_move: bool = False


@dataclass
class Game:
	current_player: (str, str) = None
	game_status: GameStatus = None
	game_over: bool = False
	logs: list[Move] = field(default_factory=list)
	board: list[list[BoardCell]] = field(default_factory=list)
	players: dict = field(default_factory=dict)

	def __post_init__(self):
		self.board = [[BoardCell(row, col) for col in range(8)] for row in range(8)]

		# Considering the layout - black pieces takes top 2 row [0, 1] and white pieces take bottom 2 rows[6, 7]
		# Setting Pawn
		for y in range(8):
			self.board[1][y] = BoardCell(1, y, Pawn())
			self.board[6][y] = BoardCell(6, y, Pawn(True))

		# Setting Rook
		for x, y in [[0, 0], [0, 7], [7, 0], [7, 7]]:
			self.board[x][y] = BoardCell(x, y, Rook(x == 7))

		# Setting Knight
		for x, y in [[0, 1], [0, 6], [7, 1], [7, 6]]:
			self.board[x][y] = BoardCell(x, y, Knight(x == 7))

		# Setting Bishop
		for x, y in [[0, 2], [0, 5], [7, 2], [7, 5]]:
			self.board[x][y] = BoardCell(x, y, Bishop(x == 7))

		# Setting King
		for x, y in [[0, 3], [7, 3]]:
			self.board[x][y] = BoardCell(x, y, King(x == 7))

		# Setting Queen
		for x, y in [[0, 4], [7, 4]]:
			self.board[x][y] = BoardCell(x, y, Queen(x == 7))

	def print_data(self):
		print(f"=================" * 3)
		print("Black")
		for row in self.board:
			print(row)
		print("White")
		print(f"=================" * 3)
		print()

	def print_board(self):
		print()
		print(str('------' * 11 + "BLACK" + '------' * 11).center(100))
		for row in self.board:
			for cell in row:
				prefix = "WHITE_" if cell.piece and cell.piece.is_white else "BLACK_" if cell.piece and not cell.piece.is_white else " "
				curr = str(prefix) + cell.piece.__class__.__name__ if cell.piece is not None else " [  ] "
				curr = curr.upper()
				print(f" {curr.center(14)} ", end="|")
			print()
		print(str('------' * 11 + "WHITE" + '------' * 11).center(100))
		print()

	def play(self):
		while True:
			try:
				print(f"Current turn: {self.current_player[0]} ({self.current_player[1]})")
				print(f"Choose chess piece to move. Enter the coordinates in the form of x y. ")
				x, y = list(map(int, input("Move from? ").split(" ")))

				# get current cell
				current_cell = self.board[x][y]

				# A player should not be able to move pieces of another player
				check = True if self.current_player[1] == "White" else False
				if current_cell.piece is None or current_cell.piece.is_white != check:
					continue

				# fetch possible moves for the chess piece
				# possible_moves = current_cell.possible_moves(self.board)
				# print("Possible moves:", end=" ")
				# print(possible_moves)

				# if no possible moves, pass to another player
				# if len(possible_moves) == 0:
				# 	continue

				# allow player to choose a position from the possible moves
				try:
					x_pos, y_pos = list(map(int, input("Move the chess piece to? ").split(" ")))

					if current_cell.is_valid_move(self.board, x_pos, y_pos):
						# move chess piece to selected position
						move = Move(self.current_player, [x, y], [x_pos, y_pos])
						move.piece_moved = current_cell.piece
						current_cell.move_piece(self.board, move)

						# update moves and logs
						self.logs.append(move)

						# add piece_killed in players
						if move.piece_killed:
							if self.current_player[0] == self.players[1].name:
								self.players[2].pieces_killed.append(move.piece_killed)
							else:
								self.players[1].pieces_killed.append(move.piece_killed)

						# display board
						self.print_board()
					else:
						continue

				# Check conditions when game ends
				# If moved piece puts King in check for the opposite player
				# Initiate check and allow moves which eliminates the check
				# If no possible moves, check mate, change game status, declare winner and change game status

				except ValueError:
					print(f"Invalid Input!!! Try again \n")
					continue

			except ValueError:
				print(f"Wrong Input!!! Try again \n")
				continue

			if self.game_over:
				break

			if self.current_player[0] == self.players[1].name:
				self.current_player = (self.players[2].name, "Black")
			else:
				self.current_player = (self.players[1].name, "White")


def main():
	game = Game()
	print("Player 1 (White) ")
	first = input("Enter your name: ")
	game.players[1] = Player(name=first, is_white=True)

	print(f"Player 2 (Black) ")
	second = input("Enter your name: ")
	game.players[2] = Player(name=second)

	game.current_player = (first, "White")
	game.print_board()
	game.play()


if __name__ == '__main__':
	main()
