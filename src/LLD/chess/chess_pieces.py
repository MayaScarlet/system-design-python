from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Piece(ABC):
	is_white: bool = False

	@abstractmethod
	def possible_moves(self, board, curr_x, curr_y):
		...


@dataclass
class King(Piece):
	castling: bool = False

	def __post_init__(self):
		super().__init__(self.is_white)

	def possible_moves(self, board, curr_x, curr_y):
		# King can only move one cell in all directions, can kill one direction
		...

	def perform_castling(self, board, move):
		...

	def is_castling_possible(self):
		"""
		It consists of moving one’s king two squares toward a rook on the same rank and then moving the rook
		to the square that the king passed over.
		- Castling is permissible provided all the following conditions hold:
		- Neither the king nor the rook has previously moved.
		- There are no pieces between the king and the rook.
		- The king is not currently in check.
		- The king does not pass through a square that is attacked by an opposing piece.
		- The king does not end up in check. (True of any legal move.)
		"""
		...


@dataclass
class Queen(Piece):
	def __post_init__(self):
		super().__init__(self.is_white)

	def possible_moves(self, board, curr_x, curr_y):
		# Queen can move in all directions, take any steps
		...


@dataclass
class Rook(Piece):
	def __post_init__(self):
		super().__init__(self.is_white)

	def possible_moves(self, board, curr_x, curr_y):
		# Rook can move in four directions, take any no of steps
		...


@dataclass
class Bishop(Piece):
	def __post_init__(self):
		super().__init__(self.is_white)

	def possible_moves(self, board, curr_x, curr_y):
		# Bishop can move diagonally in 4 directions, take any no of steps and can kill pieces along the path
		...


@dataclass
class Knight(Piece):
	def __post_init__(self):
		super().__init__(self.is_white)

	def possible_moves(self, board, curr_x, curr_y):
		# Knight can move forward, backward, left or right two squares and must then move one square in either
		# perpendicular direction
		...


@dataclass
class Pawn(Piece):
	initial_move: bool = True

	def __post_init__(self):
		super().__init__(self.is_white)

	def possible_moves(self, board, curr_x, curr_y):
		# Pawn can move forward 1 or 2 steps in the initial move and later 1 step only and can kill diagonally
		...


@dataclass
class BoardCell:
	x: int
	y: int
	piece: Pawn | King | Queen | Bishop | Knight | Rook = None

	def set_piece(self, board_piece: Piece):
		self.piece = board_piece

	def possible_moves(self, board):
		return self.piece.possible_moves(board, self.x, self.y)

	def move_piece(self, board, move):
		[new_x, new_y] = move.new_position

		if hasattr(self.piece, 'initial_move') and self.piece.initial_move:
			self.piece.initial_move = False

		if board[new_y][new_y] is not None:
			move.piece_killed = board[new_x][new_y].piece

		board[new_x][new_y] = BoardCell(new_x, new_y, self.piece)
		self.piece = None

	def is_valid_move(self, board, new_x, new_y):
		...
