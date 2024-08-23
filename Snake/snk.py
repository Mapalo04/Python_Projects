import pygame, sys
from pygame.locals import *
import random
import time
import os

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))
try:
 icon = pygame.image.load('icon.jpg')
 pygame.display.set_icon(icon)

except:
    print("image not found")
def write(font_type, size, text, b, text_cl, highlighter, xpos, ypos):
    font = pygame.font.SysFont(font_type, size)
    text_on = font.render(text, b, text_cl, highlighter)
    rect_on = text_on.get_rect()
    rect_on.center = (xpos, ypos)
    screen.blit(text_on, rect_on)

screen = pygame.display.set_mode((680, 300))
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
fruit_c = (0, 230, 30)
blue = (0,0, 200)
WHITE = (255, 255, 255)
image = pygame.Surface((5, 15))
rect = pygame.Rect((20,68), (4,15))

imagex = 20
imagey = 275
direction = 'right'

def resta():
    global imagex, imagey, direction, loop, score
    imagex = 20
    imagey = 275
    direction = 'right'
    loop = 0
    score = 0
    
def Game_Over():
    global SP, running, High_Score
    pygame.draw.rect(screen, blue, (0,0, 680, 150))
    if score > High_Score:
        High_Score = score
    
    
    while SP == True:
        sp_cl = random.choice([blue, WHITE])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SP = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resta()
                    SP = False
                    

        write("Algerian", 30, "Game Over", True, blue, WHITE, 350,50)
        write("Algerian", 30, "Press The spacebar to restart", True, sp_cl, WHITE, 350,150)
        
        
        
        pygame.display.update()
    return score

def paused(loop):
    global running
    pygame.draw.rect(screen, blue, (0,0, 680, 150))
    
    while loop < 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 2
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 2

        write("Algerian", 30, "Game Has Paused", True, blue, WHITE, 350,50)

        
        pygame.display.update()
                

#file = ""
#pygame.mixer.init()
#pygame.mixer.music.load(file)
fruit_x = random.randint(0, 640)
fruit_y = random.randint(160, 260)
dth = random.choice(["yes", "no", "maybe"])
sve = random.choice(["yes", "no", "maybe"])

#save data file
if os.path.exists("Save.txt") == False:
    save_f = open("Save.txt", 'w+')
    save_f.write("high score 0")
    save_f.close()

save_r = open("Save.txt", "r+")
score_r = str(save_r.read(-1))
score_r =  score_r[11:]
print(score_r)
save_r.close()


loop = 0
score = 0
High_Score = int(score_r)
SP = False
running = True
while running:
    
    a = random.choice([123, 200, 250, 150, 80, 40, 90])
    b = random.choice([132, 255, 220, 150, 70, 20, 85])
    c = random.choice([145, 230, 215, 129, 61, 50, 47])
    
    screen.fill(WHITE)
    clock.tick(fps)
    pygame.draw.rect(screen, blue, (0,0, 680, 150))
    write("Berlin Sans FB Demi", 20, str(score), True, black, blue, 10, 10)
    write("Berlin Sans FB Demi", 20, "High Score: {0}".format(High_Score), True, black, blue, 580,10)
#this is for the green ball which appears
    pygame.draw.circle(screen, fruit_c, (fruit_x, fruit_y), 6)
    if score % 10 == 0 and score > 0:
        write("Berlin Sans FB Demi", 30, "You're in The Safe Zone", True, blue, WHITE, 350,100)
    if dth == sve :
        SP = True
        write("Berlin Sans FB Demi", 30, "Warning", True, black, blue, 350,100)
   
        if score % 10 == 0:
            sve = random.choice(["yes", "no", "maybe"])
            SP = False
        


    print(str(imagex)+", " + str(imagey))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write("Algerian", 30, "Thank You for Playing", True, blue, WHITE, 350,50)
            
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = 0
                paused(loop)
            if event.key == pygame.K_d:
                direction = 'right'
            elif event.key == pygame.K_a:
                direction = 'left'
            elif event.key == pygame.K_s:
                direction = 'down'
            elif event.key == pygame.K_w:
                direction = 'up'

    #if imagey >= 275:
     #   if direction == "up" or direction =="right" or direction == "left":
      #      for event in pygame.event.get():
       #         if event.type == pygame.KEYDOWN:
        #            if event.key == pygame.K_w:
         #               imagey -= 10
          #              direction = "up"
           #         elif event.key == pygame.K_d:
            #            direction = 'right'
             #       elif event.key == pygame.K_a:
                        #direction = 'left'
        #else:
           # direction = "no"

    y_res = imagey - fruit_y
    x_res = imagex - fruit_x
    if  ((y_res <= 5 and y_res >=0) or (y_res >= -20 and y_res <= 0))  and abs(x_res) <= 12 :
        score = score + 1
        fruit_x = random.randint(20, 640)
        fruit_y = random.randint(160, 260)
    
    if imagey >= 275:
        if SP == True:
            write("Arial", 20, "Warning", True, black, blue, 10, 10)
            Game_Over()
        random.choice([sve , dth])

        sve = random.choice(["yes", "no", "maybe"])
        direction = "up"
        #pygame.mixer.music.play(0, 99.5)
        blue = (a, b, c)
    elif imagey <= 150:
        if SP == True:
            write("Arial", 20, "Warning", True, black, blue, 10, 10)
            Game_Over()
        random.choice([sve , dth])

        dth = random.choice(["yes", "no", "maybe"])
        direction = "down"
        blue = (a, b, c)
    if imagex <=10 :
        
        if SP == True:
            write("Arial", 20, "Warning", True, black, blue, 10, 10)
            Game_Over()
        random.choice([sve , dth])
        dth = random.choice(["yes", "no", "maybe"])
        direction = "right"
        blue = (a, b, c)
    if imagex >=670 :
        if SP == True:
            write("Arial", 20, "Warning", True, black, blue, 10, 10)
            Game_Over()
        random.choice([sve , dth])
        
        direction = "left"
        blue = (a, b, c)

        sve = random.choice(["yes", "no", "maybe"])
                
    if direction == 'right':
         imagex += 5
         
    elif direction == 'down':
         imagey += 5
         
    elif direction == 'left':
         imagex -= 5
         
    elif direction == 'up':
         imagey -= 5

        

    screen.blit(image, (imagex, imagey))
    pygame.display.update()

if score > High_Score:
        High_Score = score
        
save_f = open("Save.txt", 'w+')
save_f.write(f"high score {High_Score}")
save_f.close()


print('byeee Thanks for playing')
pygame.time.delay(1000)
pygame.quit()
