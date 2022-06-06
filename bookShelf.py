import pygame
import sys
import random
from book import *
import platform

if platform.system() == "Darwin":
    sys.path.append("/opt/homebrew/lib/python3.9/site-packages/")


class Bookshelf:
    boardThickness = 8
    boardLength = 256

    bookList = []

    def __init__(self, rows=4, cols=40):
        self.nRows = (lambda: 1, lambda: rows)[rows > 1]()
        self.nCols = (lambda: 1, lambda: cols)[cols > 1]()
        self.spots = [[False] * self.nCols] * self.nRows
        self.nSpots = self.nCols * self.nRows
        self.initialise()

    def initialise(self):
        cntr = 0
        for i in range(self.nRows):
            for j in range(self.nCols):
                self.bookList.append(Book())
                self.bookList[cntr].setRow(i)
                self.bookList[cntr].setCol(j)
                cntr += 1

    def getFreeSpots(self):
        spots = 0
        for book in self.bookList:
            if book.getGenre() == "Generic":
                spots += 1
        return spots

    def getBook(self, x, y):
        x = x % self.nCols
        y = y % self.nRows
        return self.bookList[y*self.nCols+x]

    def insertBook(self, book):
        if self.getFreeSpots() > 0:
            rand = random.randrange(0, len(self.bookList))
            while (self.bookList[rand].getGenre() != "Generic"):
                rand = random.randrange(0, len(self.bookList))

            self.bookList[rand] = book
            self.bookList[rand].setColor("r")

            print((self.getFreeSpots()-1) + " spots left in bookshelf.")

        else:
            print("Sorry your bookshelf is full!")

    def drawSelf(self, screen):
        pygame.draw.rect(screen, rgbBrown,
                         (10, 10, self.boardThickness, self.boardLength))
        pygame.draw.rect(screen, rgbBrown,
                         (10, 10, self.boardLength, self.boardThickness))
        pygame.draw.rect(screen, rgbBrown,
                         (10, 256, self.boardLength, self.boardThickness))
        pygame.draw.rect(screen, rgbBrown,
                         (266, 10, self.boardThickness, self.boardLength))

    def drawBooks(self, screen):
        for book in self.bookList:
            book.drawSelf(screen)
