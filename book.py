import pygame
import random
import sys
import platform

if platform.system() == "Darwin":
    sys.path.append("/opt/homebrew/lib/python3.9/site-packages/")

rgbBrown = (139, 69, 19)
rgbSilk = (255, 248, 220)
rgbGolden = (218, 165, 32)
rgbRed = (255, 0,  0)
rgbGreen = (0,  255, 0)
rgbBlue = (0,  0,  255)
rgbYellow = (255, 255, 0)
rgbGray = (128, 128, 128)
rgbBlack = (0,  0,  0)
rgbWhite = (255, 255, 255)
rgbSelected = rgbRed


class Book:
    shelfThickness = 5
    xOffset = 20
    yOffset = 24
    width = 5
    height = 54
    row = 0
    col = 0
    x = 0
    y = 0
    lBound = 1

    def __init__(self, title="There and back again", author="Bilbo Baggins"):
        self.title = title
        self.author = author
        self.genre = "Generic"
        self.clr = rgbSilk

    def getDetails(self):
        print(self.title + " by " + self.author + " -> " + self.genre)
        print("\tis stored in Row " + str(self.row+1) +
              " and Spot " + str(self.col+1))

    def getDimensions(self):
        return (self.x, self.y, self.width, self.height)

    def drawSelf(self, screen):
        pygame.draw.rect(screen, self.clr, self.getDimensions())

    def setSpot(self, r, c):
        self.setRow(r)
        self.setCol(c)

    def setRow(self, r):
        self.row = r
        self.y = r * (self.height + self.shelfThickness) + self.yOffset

    def setCol(self, c):
        self.col = c
        self.x = c * (self.width + self.lBound) + self.xOffset

    def setTitle(self, name):
        self.title = name

    def setAuthor(self, name):
        self.author = name

    def setGenre(self, genre):
        self.genre = genre

    def getGenre(self):
        return self.genre

    def setColor(self, rgb):
        if rgb == "r":
            self.clr = self.getRandomRGB()
        else:
            self.clr = rgb

    def toggleHighlight(self):
        if self.clr == rgbSelected:
            self.clr = self.clr_a
        else:
            self.clr_a = self.clr
            self.clr = rgbSelected

    def getRandomRGB(self):
        return (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
