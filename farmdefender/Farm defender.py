import time
import random
import math
from gamelib import *

max_level = 30
inv_passed = 0
inv_passed_threshold = 3
ani_killed = 0
ani_killed_threshold = 3
speed_slow = 3
speed_med = 5
speed_fast = 10


def countdown():
    pause_bet_level = 5
    if not game.over:
        game.drawText("Level " + str(l+1) + " starting...",490,300,Font(red))
        game.update(30)
        time.sleep(1)
        while pause_bet_level:
            timeformat = '{:02d}'.format(pause_bet_level)
            #print(timeformat, end='\r')
            bk.draw()
            game.drawText(timeformat,490,300,Font(red))
            game.update(30)
            time.sleep(1)
            pause_bet_level -= 1

game = Game(1000,600,"Farm Defender")
bk = Image("images/farm_bkground.jpg", game)
bk.resizeTo(game.width, game.height)
bk.draw()

crosshair = Image("images/crosshair_s.png", game)
crosshair.resizeBy(-70)

for l in range(max_level):
    inv_passed = 0
    ani_killed = 0
    invaders = []
    invaders2 = []
    animals = []

    countdown()

    for x in range(0, 7):
        invaders.append(Image("images/invader_small.png", game))
        invaders[x].resizeBy(-80)
        invaders[x].setSpeed(random.randint(1,5),90)
        invaders[x].moveTo(900+random.randrange(5,60,5),500+x*10)
    #print("invaders count " + str(len(invaders)))
    for y in range(0, ceil(l/3)):
        invaders2.append(Image("images/invader2.png", game))
        invaders2[y].resizeBy(-80)
        invaders2[y].setSpeed(random.randint(1,5),90)
        invaders2[y].moveTo(900+random.randrange(5,60,5),500+x*10)
    for z in range(0, ceil(l/5)):
        animals.append(Image("images/new_born.png", game))
        animals[z].resizeBy(-70)
        animals[z].setSpeed(random.randint(1,5),90)
        animals[z].moveTo(900+random.randrange(5,60,5),500+x*10)
            
    while not game.over:

        game.processInput()

        bk.draw()
        for x in invaders:
            x.move()
        for y in invaders2:
            y.move()
        for z in animals:
            z.move()
        crosshair.moveTo(mouse.x, mouse.y)
        #game.displayTime()
        game.drawText("Level: " + str(l+1),900, 0)
        game.update(30)

        for x in invaders:
            if x.collidedWith(mouse) and mouse.LeftButton:
                print("killed" + str(x))
                invaders.remove(x)
                break
            if x.isOffScreen('all'):
                inv_passed += 1
                print(inv_passed)
                invaders.remove(x)
            if inv_passed == inv_passed_threshold:
                game.drawText("Game Over - Press space to quit",430,300,Font(red))
                game.over = True
                break
        for y in invaders2:
            if y.collidedWith(mouse) and mouse.LeftButton:
                print("killed" + str(y))
                invaders2.remove(y)
                break
            if y.isOffScreen('all'):
                inv_passed += 1
                print(inv_passed)
                invaders2.remove(y)
            if inv_passed == inv_passed_threshold:
                game.drawText("Game Over - Press space to quit",430,300,Font(red))
                game.over = True
                break
        for z in animals:
            if z.collidedWith(mouse) and mouse.LeftButton:
                print("killed" + str(y))
                ani_killed += 1
                animals.remove(z)
                break
            if z.isOffScreen('all'):
                animals.remove(z)
            if ani_killed == ani_killed_threshold:
                game.drawText("Game Over - Press space to quit",430,300,Font(red))
                game.over = True
                break
        if len(invaders) == 0 and len(invaders2) == 0 and len(animals) == 0:
            break
        #print("level " + str(l) + " completed.")

if not game.over:
    game.drawText("You won - Press space to quit",430,300,Font(red))
game.update(30)
game.wait(K_SPACE)
game.quit()
