#importing stuff
import curses
import Food
import Snake
from constants import HEIGHT, WIDTH, TIMEOUT
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP


class GameManager:
    #initializing
    def __init__(self):
        try:
            curses.initscr()
            self.score = 0;
            self.window = curses.newwin(HEIGHT, WIDTH, 0, 0)
            self.window.timeout(TIMEOUT)
            self.window.keypad(1)
            curses.noecho()
            curses.curs_set(0)
            self.window.border(0)
            self.snake = Snake.Snake(self.window)
            self.food = Food.Food(self.window)
        except:
            curses.endwin()
    
    #Method to play game
    def play(self):
        #Game Loop
        while True:  
            try:
                #rendering
                self.window.clear()
                self.window.border(0)
                self.window.addstr(0, 5, "Score: {}" .format(self.score))
                self.snake.render()
                self.food.render()
            
                #taking Input
                event = self.window.getch()

                #handling input
                if event == 27:
                    break
                elif event in [KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP]:
                    self.snake.changeDir(event)
            
                #checking if eaten food
                if(self.snake.eaten(self.food.x, self.food.y)):
                    self.snake.grow()
                    self.food.update()
                    self.score += 1

                #updating snake
                self.snake.updateSnake()

                #checking if sanke is dead
                if(self.snake.isDead()):
                    break

            except:
                break

        curses.endwin()
        self.gameOver()

    def gameOver(self):
        print "Game Over\n"
        print "Your score is {}" .format(self.score)


