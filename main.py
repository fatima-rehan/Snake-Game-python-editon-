#Name: Fatima Rehan
#Student#: 342605409
#Date: 01/10/2023
#File: PYTHON Game.py
#Purpose: Creates a "Snake Game" inspired Pygame, called "The PYTHON Game"

#Importing necessary libraries
import pygame
import random
import time

pygame.mixer.init()
pygame.init()

#Setting up the font text
pygame.font.get_fonts()
font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("copperplategothic", 35)

#Creating output screen, and labelling the game
display_width = 500
display_height = 500
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("The PYTHON Game, by Fatima")
size = display_width, display_height
screen = pygame.display.set_mode(size)

#Variable to store passed time/python speed/python size/
clock = pygame.time.Clock()
python_block = 25
python_speed = 6

#Setting up colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (85, 107, 47)
beige = (255, 228, 196)
gray = (131, 139, 139)

#Creating background music
sounda = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

#importing images
background = pygame.image.load("background.png")
food = pygame.image.load("mouse.png").convert_alpha()
food_size = (125, 125)
food = pygame.transform.scale(food, food_size)
pygame.display.flip()


#Setting up scoreboard
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, beige)
    dis.blit(value, [0, 0])


#Setting up sound variables
python_growth_Sound = pygame.mixer.Sound("munch.wav")
game_close_Sound = pygame.mixer.Sound("game over.wav")


#Colouring the python, defining the python variables
def our_python(python_block, python_list):
    for x in python_list:
        pygame.draw.rect(dis, green, [x[0], x[1], python_block, python_block])


#Defining text variable, and size
def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg, [display_width / 5, display_height / 5])


#Defining game over, and game close veriables
def gameLoop():  #Game Loop
    game_over = False
    game_close = False

    #Setting up python, x & y variables
    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    python_List = []
    Length_of_python = 1

    #Setting up food x and y variables
    foodx = round(
        random.randrange(0, display_width - python_block) / 25.0) * 25.0
    foody = round(
        random.randrange(0, display_height - python_block) / 25.0) * 25.0

    while not game_over:
        #Setting up "Game Over" screen
        while game_close == True:
            dis.fill(black)
            message("GAME OVER! Press P-Play Again, or Q-Quit", red)
            game_close_Sound.play()
            pygame.time.wait(3000)
            game_close_Sound.set_volume(0)
            Your_score(Length_of_python - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  #Q-Quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:  #P-Play Again
                        gameLoop()
#Moving the python using the up, down, left, right keys
        for event in pygame.event.get():
            dis.blit(food, (foodx, foody, python_block, python_block))
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -python_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = python_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -python_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = python_block
                    x1_change = 0


#Ends game if python touches border
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.blit(background, (0, 0))  #Setting background image
        dis.blit(
            food,
            (foodx, foody, python_block, python_block))  #Displaying the food

        #Creating the python growth by food variable
        python_Head = []
        python_Head.append(x1)
        python_Head.append(y1)
        python_List.append(
            python_Head)  #Adding the python length, after the head
        if len(python_List) > Length_of_python:
            del python_List[0]
        for x in python_List[:
                             -1]:  #If the pythons head touches x border, you lose
            if x == python_Head:
                game_close = True

        our_python(python_block, python_List)
        Your_score(Length_of_python - 1)

        pygame.display.update()
        #Makes the python grow a block, when touching food. Also plays sound
        food_rect = pygame.Rect(foodx, foody, python_block, python_block)
        python_rect = pygame.Rect(x1, y1, python_block, python_block)

        if food_rect.colliderect(python_rect):
            print("The python is full, wait 3 seconds")
            foodx = round(
                random.randrange(0, display_width - python_block) /
                25.0) * 25.0
            foody = round(
                random.randrange(0, display_height - python_block) /
                25.0) * 25.0
            Length_of_python += 1
            python_growth_Sound.play()
        dis.blit(food, (foodx, foody, python_block, python_block))
        clock.tick(python_speed)  #game speed

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()
    quit()

gameLoop()
