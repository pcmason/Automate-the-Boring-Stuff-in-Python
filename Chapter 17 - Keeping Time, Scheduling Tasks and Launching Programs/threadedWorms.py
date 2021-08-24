#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
threadedworms.py
Created on Sat Aug 21 18:16:19 2021

@author: paulmason

program that is a 'snake' style clone but instead of one snake going around eating apples
this program uses multiple threads to create many snakes that move around on their own thread
using locks this program ensures 2 worms cannot occupy the same cell at the same time
"""
#import threading to create the multiple threads for each worm, pygame to create window and draw
#rectangles and lines, random to randomly assign colors to the worms and sys to quit the program
import threading, sys, pygame, random
from pygame.locals import *

#define constants
#number of worms in the grid
NUM_WORMS = 20
#frames per seconds program runs
FPS = 30
#how many pixels wide and high each cell in the grid is
CELL_SIZE = 20
#how many cells wide the grid is
CELLS_WIDE = 32
#how many cells high the grid is
CELLS_HIGH = 24
#variable to keep track of the grid is a list of lists representing x and y values
GRID = []

#fill the grid with None values to state they are unoccupied
for x in range(CELLS_WIDE):
    GRID.append([None] * CELLS_HIGH)
    
#create a global Lock object the threads will acquire before modifying GRID
GRID_LOCKS = []
for x in range(CELLS_WIDE):
    column = []
    for y in range(CELLS_HIGH):
        #create a lock for each cell
        column.append(threading.Lock())
    GRID_LOCKS.append(column)    

#create constants for colors using RGB tuples
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
DARKGRAY = (40, 40, 40)
#set the background color to be black
BGCOLOR = BLACK
#set the color of the lines of the grid to be dark gray
GRID_LINES_COLOR = DARKGRAY

#calculate the total pixels wide and high for the window
WINDOWWIDTH = CELL_SIZE * CELLS_WIDE
WINDOWHEIGHT = CELL_SIZE * CELLS_HIGH

#create constants for the movements of the worms
UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

#set constants for the head and tail of the worm
HEAD = 0
BUTT = -1

#global variable that tells the worms when to exit (stop running)
WORMS_RUNNING = True

#create a class for the worms, which is a child of the Thread class from threading
class Worm(threading.Thread):
    #create the init method for the Worm class
    def __init__(self, name = 'Worm', maxsize = None, color = None, speed = None):
        #use Thread's init method for Worm, since currently overriding Thread class' init method
        threading.Thread.__init__(self)
        
        #assign the name value
        self.name = name
        
        #set the maxsize to be random or the parameter given
        if maxsize is None:
            self.maxsize = random.randint(4, 10)
            
            #create a small chance of there being a really long worm
            if random.randint(0, 4) == 0:
                self.maxsize += random.randint(10, 20)
                
        else:
            self.maxsize = maxsize
            
        #set the color to the parameter or a random color
        if color is None:
            self.color = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
        else:
            self.color = color
            
        #set the speed to the parameter or a random speed
        if speed is None:
            #the worm will move between every 0.02 or 0.5 seconds
            self.speed = random.randint(20, 500)
        else:
            self.speed = speed
            
        #now get the create the starting location of the worm using the global GRID variable
        #now loop through random values in the grid until you find an unoccupied cell
        while True:
            #get a random x and y coordinate
            startx = random.randint(0, CELLS_WIDE - 1)
            starty = random.randint(0, CELLS_HIGH - 1)
            #first have to acquire the lock so 2 worms do not occupy the same cell upon creation
            GRID_LOCKS[startx][starty].acquire()
            #if the cell is unoccupied break out of the while loop
            if GRID[startx][starty] is None:
                break
        
        #now set the cell to be the color of the worm (all worms begin with the length of 1)
        GRID[startx][starty] = self.color
        #finally release the lock so other worms can be created
        GRID_LOCKS[startx][starty].release()
        
        #set the body variable of the worm to be the starting location of the worm determine above
        #the body variable is a list of dictionaries where each dict represents a unit of the worm's body
        self.body = [{'x': startx, 'y': starty}]
        #set the direction the worm moves in to start randomlly
        self.direction = random.choice((UP, DOWN, LEFT, RIGHT))
        
    #since start() is inherited from Thread DO NOT have to redefine it here
    #instead when start() is called it will immediatebly run the run() method defined here
    def run(self):
        #thread code goes here
        #create an infinite loop so the worms are always moving
        while True:
            #first check that WORMS_RUNNING is true, if not then return and exit the run method
            if not WORMS_RUNNING:
                return
            
            #randomly decide to change direction
            #20% chance to change direction
            if random.randint(0, 100) < 20:
                #the new direction chosen may be the same as the old direction
                self.direction = random.choice((UP, DOWN, LEFT, RIGHT))
            
            #get the next x and y value from the worm's method
            nextx, nexty = self.getNextPosition()
            
            #get the lock first
            origx, origy = nextx, nexty
            if origx not in (-1, CELLS_WIDE) and origy not in (-1, CELLS_HIGH):
                #do not return until the thread can acquire the lock
                gotLock = GRID_LOCKS[origx][origy].acquire(timeout = 1)
                if not gotLock:
                    continue
            
            #check if the new x and y is outside of the grid or the next cell is occupied 
            if nextx in (-1, CELLS_WIDE) or nexty in (-1, CELLS_HIGH) or GRID[nextx][nexty] is not None:
                #space worm is heading towards is taken so change direction
                self.direction = self.getNewDirection()
                
                #check if there is no places for the worm to move
                if self.direction is None:
                    #reverse the worm so the head is the tail and vice versa
                    self.body.reverse()
                    self.direction = self.getNewDirection()
                    
                #check if it is possible to move in some direction
                if self.direction is not None:
                    #reask for the next position
                    nextx, nexty = self.getNextPosition()
                    
            if origx not in (-1, CELLS_WIDE) and origy not in (-1, CELLS_HIGH):
                GRID_LOCKS[origx][origy].release()
                    
            #check if the space on the grid is free if so move there
            if self.direction is not None:
                GRID_LOCKS[nextx][nexty].acquire()
                #update the GRID
                GRID[nextx][nexty] = self.color
                GRID_LOCKS[nextx][nexty].release()
                #update the worm's state
                self.body.insert(0, {'x': nextx, 'y': nexty})
                
                #check if worm has grown too long, if so cut off the tail to give the illusion of movement
                if len(self.body) > self.maxsize:
                    gotLock = GRID_LOCKS[self.body[BUTT]['x']][self.body[BUTT]['y']].acquire(timeout=2)
                    
                    if not gotLock:
                        self.maxsize -= 1 
                        
                    #update the GRID
                    GRID[self.body[BUTT]['x']][self.body[BUTT]['y']] = None
                    GRID_LOCKS[self.body[BUTT]['x']][self.body[BUTT]['y']].release()
                    #update the worm's state
                    del self.body[BUTT]
                    
            else:
                #cannot move so do nothing except set a new random direction
                self.direction = random.choice((UP, DOWN, LEFT, RIGHT))
            
            #put the worm's thread to sleep for the number of milliseconds speed is set to
            pygame.time.wait(self.speed)
            
    #figure out the next x and y of the worm based on the direction and current location of the head
    def getNextPosition(self):
        #update the worm's head based on the direction
        if self.direction == UP:
            nextx = self.body[HEAD]['x']
            nexty = self.body[HEAD]['y'] - 1
        elif self.direction == DOWN:
            nextx = self.body[HEAD]['x']
            nexty = self.body[HEAD]['y'] + 1
        elif self.direction == LEFT:
            nextx = self.body[HEAD]['x'] - 1
            nexty = self.body[HEAD]['y']
        elif self.direction == RIGHT:
            nextx = self.body[HEAD]['x'] + 1
            nexty = self.body[HEAD]['y']
        else:
            assert False, 'Bad value for self.direction: %s' % self.direction
            
        return nextx, nexty
    
    #figure out what possible directions, if any, the worm can move and return one randomly or None
    def getNewDirection(self):
        #mae the code more readable by defining x and y
        x = self.body[HEAD]['x']
        y = self.body[HEAD]['y']
        
        #create a list of possible directions the worm can move
        newDirection = []
        if y-1 not in (-1, CELLS_HIGH) and GRID[x][y-1] is None:
            newDirection.append(UP)
        if y+1 not in (-1, CELLS_HIGH) and GRID[x][y+1] is None:
            newDirection.append(DOWN)
        if x-1 not in (-1, CELLS_WIDE) and GRID[x-1][y] is None:
            newDirection.append(LEFT)
        if x+1 not in (-1, CELLS_WIDE) and GRID[x+1][y] is None:
            newDirection.append(RIGHT)
        
        if newDirection == []:
            #return None if there is no possible direction for the worm to move
            return None
        
        #else return a random direction from the open options on the grid
        return random.choice(newDirection)
    
#now define the main part of the program
def main():
    global FPSCLOCK, DISPLAYSURF
    
    squares = """
...........................
...........................
...........................
.H..H..EEE..L....L.....OO..
.H..H..E....L....L....O..O.
.HHHH..EE...L....L....O..O.
.H..H..E....L....L....O..O.
.H..H..EEE..LLL..LLL...OO..
...........................
.W.....W...OO...RRR..MM.MM.
.W.....W..O..O..R.R..M.M.M.
.W..W..W..O..O..RR...M.M.M.
.W..W..W..O..O..R.R..M...M.
..WW.WW....OO...R.R..M...M.
...........................
...........................
"""
    #this line will write out 'Hello Worm' on the grid, comment it out if you just want a blank grid
    setGridSquares(squares)

    #pygame window setup
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Threadworms')

    #create the worm objects
    #create a list that contains all of the worm objects
    worms = []
    
    for i in range(NUM_WORMS):
        worms.append(Worm())
        #start the worm code in its own thread, this will call the run() method for each worm
        worms[-1].start()
        
    #the main game loop
    while True:
        #check if the user has terminated the program
        handleEvents()
        #draw the grid lines and cells to the screen
        drawGrid()
        #tell the window to update the screen
        pygame.display.update()
        #pause for how long is needed to achieve the framerate specified by FPS
        FPSCLOCK.tick(FPS)
        
#define method to handle game events, only events will be terminating the program
def handleEvents():
    #use the global WORMS_RUNNING to terminate the worms threads before exiting the program
    global WORMS_RUNNING 
    
    #event handling loop
    for event in pygame.event.get():
        #check for events that involve terminating the program
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            #tell the worm threads to exit
            WORMS_RUNNING = False
            pygame.quit()
            sys.exit()

#method that draws the screen based on values in GRID
def drawGrid():
    #draw the grid lines
    DISPLAYSURF.fill(BGCOLOR)
    #draw vertical lines
    for x in range(0, WINDOWWIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, GRID_LINES_COLOR, (x, 0), (x, WINDOWHEIGHT))
    #draw horizontal lines
    for y in range(0, WINDOWHEIGHT, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, GRID_LINES_COLOR, (0, y), (WINDOWWIDTH, y))
    
    for x in range(0, CELLS_WIDE):
        for y in range(0, CELLS_HIGH):
            #need to acquire the lock before modifying GRID
            gotLock = GRID_LOCKS[x][y].acquire(timeout=0.02)
            
            if not gotLock:
                continue
            
            
            if GRID[x][y] is None:
                #no body segment at this cell to draw, so draw a blank square
                pygame.draw.rect(DISPLAYSURF, BGCOLOR, (x * CELL_SIZE + 1, y * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1))
                #release lock
                GRID_LOCKS[x][y].release()
            else:
                #modify the grid data struct
                color = GRID[x][y]
                #release lock
                GRID_LOCKS[x][y].release()
            
                #draw the body segment on the screen
                darkerColor = (max(color[0] - 50, 0), max(color[1] - 50, 0), max(color[2] - 50, 0))
                pygame.draw.rect(DISPLAYSURF, darkerColor, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(DISPLAYSURF, color, (x * CELL_SIZE + 4, y * CELL_SIZE + 4, CELL_SIZE - 8, CELL_SIZE - 8))

    
#method that writes static blocks to the grid
def setGridSquares(squares, color = (192, 192, 192)):
    squares = squares.split('\n')
    if squares[0] == '':
        del squares[0]
    if squares[-1] == '':
        del squares[-1]
        
    for y in range(min(len(squares), CELLS_HIGH)):
        for x in range(min(len(squares[y]), CELLS_WIDE)):
            #acquire the lock
            GRID_LOCKS[x][y].acquire()
            if squares[y][x] == ' ':
                GRID[x][y] = None
            elif squares[y][x] == '.':
                pass
            else:
                GRID[x][y] = color
            GRID_LOCKS[x][y].release()
    
#finally run all of the above code with this trick
if __name__ == '__main__':
    main()
            
            
    
    
