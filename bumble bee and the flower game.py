import pgzrun
import time
start = time.time()
import random
WIDTH = 600
HEIGHT = 500
TITLE = "Bumble bee and flower game"
bee = Actor("bee")
flower = Actor("flower")

bee.pos = 400,200
flower.pos = 100,300
score = 0 
game_over = False

def draw() :
    if game_over == False :
        total = time.time() - start
        screen.blit("bg",(0,0))
        bee.draw()
        flower.draw()
    else :
        screen.draw.text("Game over ", (100,300) )
    screen.draw.text("score: "+str(score), (0,100))
    screen.draw.text("total "+str(round(total,2)), (300,250))

def update() :
    global score
    if keyboard.left :
        bee.x = bee.x-2
    if keyboard.right :
        bee.x = bee.x+2
    if keyboard.up :
        bee.y = bee.y-2
    if keyboard.down :
        bee.y = bee.y+2
    if bee.colliderect(flower) :
        x = random.randint(50,550)
        y = random.randint(50,450)
        flower.pos = x,y
        score = score+1
        
        
pgzrun.go()

