# Importing stuff
from constants import SNAKE_X, SNAKE_Y, INIT_SNAKE_LENGHT, MAX_X, MAX_Y
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

class Snake:
    # Initilizing
    def __init__(self, window):
        self.window = window
        self.snakeBody = []
        self.length = INIT_SNAKE_LENGHT
        self.direction = KEY_RIGHT
        self.head = 'o'
        self.tail = '+'
        self.snakeBody.append([self.head, SNAKE_X, SNAKE_Y])
        for i in range(self.length):
            self.snakeBody.append([self.tail, SNAKE_X-i, SNAKE_Y])
        # Reverse movment dictionary
        self.rev = {
        KEY_RIGHT: KEY_LEFT,
        KEY_LEFT:KEY_RIGHT,
        KEY_DOWN: KEY_UP,
        KEY_UP: KEY_DOWN}    

    # Rendering the snake
    def render(self):
        for i in range(self.length+1):
            self.window.addstr(self.snakeBody[i][2], self.snakeBody[i][1], self.snakeBody[i][0])

    # Changing snake direction
    def changeDir(self, dir):
        if (self.rev.get(self.direction) == dir):
            return
        else:
            self.direction = dir

    # Checks if snake has eaten food
    def eaten(self, x, y):
        if(self.snakeBody[0][1] == x and self.snakeBody[0][2] == y ):
            return True
        else:
            return False

    # Increase size of tail by 1
    def grow(self):
        self.length += 1
        self.snakeBody.append([self.tail, 0, 0])

    # Helper function. change cordinates of entire snake according to input
    def moveSnake(self, change_x, change_y):
        #dealing with body
        for i in range(1, self.length+1):
            self.snakeBody[-1*i][2] = self.snakeBody[(-1*i)-1][2]
            self.snakeBody[-1*i][1] = self.snakeBody[(-1*i)-1][1]
        
        #dealing with head
        self.snakeBody[0][2] = self.snakeBody[0][2] + change_y
        self.snakeBody[0][1] = self.snakeBody[0][1] + change_x 

    # updating snake with time. ie moving it
    def updateSnake(self):
        if self.direction == KEY_UP:
            self.moveSnake(0, -1)
        elif self.direction == KEY_DOWN:
            self.moveSnake(0, 1)
        elif self.direction == KEY_RIGHT:
            self.moveSnake(1, 0)
        elif self.direction == KEY_LEFT:
            self.moveSnake(-1, 0)
    
    # Checking if snake is dead 
    def isDead(self):
        #case where snake hit itself
        self.snakeBody[0][0] = self.tail
        if self.snakeBody[0] in self.snakeBody[1:]:
            return True
        
        #case where snake hit the wall
        elif self.snakeBody[0][1] == 0 or self.snakeBody[0][1] == MAX_X+1 or self.snakeBody[0][2] == 0 or self.snakeBody[0][2] == MAX_Y+1:
            return True
        
        else:
            self.snakeBody[0][0] = self.head
            return False
