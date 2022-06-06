import pygame
import sys

from book import *
from bookShelf import Bookshelf
import platform
print("Running on: " + platform.system())

if platform.system() == "Darwin":
    sys.path.append("/opt/homebrew/lib/python3.9/site-packages/")

pygame.init()
SCREENWIDTH = 800
SCREENHEIGHT = 600
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
clock = pygame.time.Clock()

b1 = Book("The Hound of the Baskervilles", "Arthur Conan Doyle")
b1.setSpot(0, 0)
b2 = Book("The Hobbit", "J. R. R. Tolkien")
b2.setSpot(1, 1)
b3 = Book()
bs = Bookshelf()

bookList = []
for i in range(10):
    bookList.append(Book())

x = 0
y = 0
speed = 1
fps = 10


def interact():
    global x
    global y
    global bs
    bs.getBook(x, y).getDetails()
    print("Do you want to edit this book?(Y/N)")
    waitForInput = True
    while waitForInput:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
                title = input('Title:')
                print(title)
                waitForInput = False
            if event.key == pygame.K_n:
                print('NO')
                waitForInput = False


def detectKeys():
    global x
    global y
    global speed
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= speed
    if pressed[pygame.K_RIGHT]:
        x += speed
    if pressed[pygame.K_DOWN]:
        y += speed
    if pressed[pygame.K_LEFT]:
        x -= speed
    if pressed[pygame.K_SPACE]:
        interact()


go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
            sys.exit()

    x_a = x
    y_a = y
    detectKeys()

    screen.fill(rgbBlack)

    bs.getBook(x_a, y_a).toggleHighlight()
    bs.getBook(x, y).toggleHighlight()
    bs.drawSelf(screen)
    bs.drawBooks(screen)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
