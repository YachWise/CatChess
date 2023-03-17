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

    def get_chess_notation(self):
        return self.get_rank_file(self.startRow, self.startColumn) + self.get_rank_file(self.endRow, self.endColumn)

    def get_rank_file(self, row, column):
        return self.columnsToFiles[column] + self.rowsToRanks[row]
