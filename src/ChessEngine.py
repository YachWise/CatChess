import pygame
import os


class GameState:

    def __init__(self):
        # game board
        # -- denotes empty space
        # first char is piece color
        # second char is piece type
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.whiteToMove = True
        self.moveLog = []

    def make_move(self, move):
        self.board[move.startRow][move.startColumn] = move.endPiece
        self.board[move.endRow][move.endColumn] = move.movingPiece

        print(self.board)
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

    def undo_move(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startColumn] = move.movingPiece
            self.board[move.endRow][move.endColumn] = move.endPiece
            self.whiteToMove = not self.whiteToMove

    def get_valid_moves(self):
        return self.get_all_possible_moves()

    def get_pawn_moves(self, row, column, moves):
        if self.whiteToMove:
            if self.board[row - 1][column] == "--":
                move_to_append = Move((row, column), (row-1, column), self.board)
                moves.append(move_to_append)
    def get_rook_moves(self, row, column, moves):
        pass

    def get_queen_moves(self, row, column, moves):
        pass

    def get_king_moves(self, row, column, moves):
        pass

    def get_bishop_moves(self, row, column, moves):
        pass

    def get_knight_moves(self, row, column, moves):
        pass

    def get_all_possible_moves(self):
        moves = []
        for rows in range(len(self.board)):
            for columns in range(len(self.board[rows])):
                turn = self.board[rows][columns][0]
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[rows][columns][1]
                    if piece == 'P':
                        self.get_pawn_moves(rows, columns, moves)
                    elif piece == 'R':
                        self.get_rook_moves(rows, columns, moves)
                    elif piece == 'B':
                        self.get_bishop_moves(rows, columns, moves)
                    elif piece == 'Q':
                        self.get_queen_moves(rows, columns, moves)
                    elif piece == 'K':
                        self.get_king_moves(rows, columns, moves)
                    elif piece == 'N':
                        self.get_knight_moves(rows, columns, moves)


class Move:
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {value: key for key, value in ranksToRows.items()}

    filesToColumns = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    columnsToFiles = {value: key for key, value in filesToColumns.items()}

    def __init__(self, start_square, end_square, board):
        self.startRow = start_square[0]
        self.startColumn = start_square[1]
        self.endRow = end_square[0]
        self.endColumn = end_square[1]

        self.movingPiece = board[self.startRow][self.startColumn]
        self.endPiece = board[self.endRow][self.endColumn]
        self.move_id = self.startRow * 1000 + self.startColumn * 100 + self.endRow * 10 + self.endColumn

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False

    def get_chess_notation(self):
        return self.get_rank_file(self.startRow, self.startColumn) + self.get_rank_file(self.endRow, self.endColumn)

    def get_rank_file(self, row, column):
        return self.columnsToFiles[column] + self.rowsToRanks[row]
