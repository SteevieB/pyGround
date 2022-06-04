import sys

from book import *
from bookShelf import Bookshelf

sys.path.append("/opt/homebrew/lib/python3.9/site-packages/")
import pygame

pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

b1 = Book("The Hound of the Baskervilles", "Arthur Conan Doyle")
b1.setSpot(0,0)
b2 = Book("The Hobbit", "J. R. R. Tolkien")
b2.setSpot(1,1)
b3 = Book()
bs = Bookshelf()

bookList = []
for i in range(10):
	bookList.append(Book())

x      = 0
y      = 0
speed  = 1
fps    = 60

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

go = True
while go:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	detectKeys()

	screen.fill(rgbBlack)

	bs.drawSelf(screen)
	bs.drawBooks(screen)

	pygame.display.update()
	clock.tick(fps)
