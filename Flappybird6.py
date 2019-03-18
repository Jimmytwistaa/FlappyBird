#we first import pygame library
import pygame
#to use the random function
import random

#initialize pygame
pygame.init()


#loading images
imageUp = pygame.image.load('goku.png')
imageUp = pygame.transform.scale(imageUp, (40,40))

imageDown = pygame.image.load('goku.png')
imageDown = pygame.transform.scale(imageDown, (50,40))

imageDead = pygame.image.load('flappydead.jpg')
imageDead = pygame.transform.scale(imageDead, (28,23))

#define colors
black = (0,0,0)
white = (255,255,255)
#define new color red
red = (255,0,0)
#define new color green
green = (0,255,0)
orange = (255,215,0)
gray = (112,138,144)
skyblue = (0,191,255)

#define screen size
size = (700,500)
screen = pygame.display.set_mode(size)

#define screen title
pygame.display.set_caption("Flappy Bird")

#boolean T/F to control game logic
done = False
#clock to control game refresh speed 
clock = pygame.time.Clock()

x = 350
y = 250
#define global variables to control speed
x_speed = 0
y_speed = 0

#define global variable position for the ground 
#sinde vertical 'size' equals 500, defined above, and 
#ball size is 20 as defined in ball defining function
ground = 477

#x-axis location of obstacles
xloc = 700
#y-axis location of obstacles
yloc = 0
#how wide we want obstacle
xsize = 70
#how randomly tall it is
ysize = random.randint(0,350)
#space between two blocks
space = 150

#the speed of the obstacles as they move across the screen
#pixels per frame/flip
obspeed = 2.5

#add global tracker of score
score = 0

#we proceed to define our obstacles 
#def obstacles(xloc,yloc,xsize,ysize):
    #pygame.draw.rect(screen,green, [xloc,yloc,xsize,ysize])
   # pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+500])
def obstacles(xloc,yloc,xsize,ysize):
    imgTop = pygame.image.load('red.png')
    imgTop = pygame.transform.rotate(imgTop, 180)
    imgTop = pygame.transform.scale(imgTop, (xsize, ysize))
    imgBottom = pygame.image.load('red.png')
    imgBottom = pygame.transform.scale(imgBottom, (xsize, 500 - ysize))
    screen.blit(imgTop, (xloc, yloc))
    screen.blit(imgBottom, (xloc, int(yloc + ysize + space)))

#define function to draw circle
def ball(x,y,image):
   #pygame.draw.circle(screen,red,(x,y),20)
   screen.blit(image, (x,y))

def gameover():
    font = pygame.font.SysFont(None,75)
    #we updated font color
    text = font.render("Game over ",True, red)
    screen.blit(text, [150,250])

#Function to write score being kept
def Score(score):
    font = pygame.font.SysFont(None,75)
    #we use str to convert score vaule to string for display
    text = font.render("Score: "+str(score),True,black)
    #top left corner coordinates
    screen.blit(text, [0,0])

#global image object
image = imageUp
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #change image up
                image = imageUp
                y_speed = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                #change image down
                image = imageDown
                y_speed = 5
#Replace the white sky with skyblue
    #screen.fill(white)
    imageB = pygame.image.load('snakeWay.png')
    imageB = pygame.transform.scale(imageB, (700,500))
    screen.fill(skyblue)
    screen.blit(imageB, (0,0))
#time to draw obstacles
    obstacles(xloc,yloc,xsize,ysize)
 #call function to draw the ball
    ball(x,y,image)
    #if the ball is between two obstacles
    Score(score)

    #adjust vertical y position
    #y = y + y_speed
    y += y_speed
 
    #time to redefine per refresh new x location
    xloc -= obspeed

    #once 'y' is changes check if ground is touches hence game over
    if y > ground:
        gameover()
        #to stop the ball
        y_speed = 4
        #if we hit the ground obstacle stops
        obspeed = 0


   #if we hit obstacles in the top block
    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        y_speed = 4
        obspeed = 0


   #if obstacle location X is
    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        y_speed = 4
        obspeed = 0


   #if obstacle location X is
    if xloc < -80:
       xloc = 700
       ysize = random.randint(0,350)
   
  #check if obstacle was passed adding to score
    if x > xloc and x < xloc+3:
       score = (score + 1)

    #refresh screen by flipping like a flipbook new animation 
    pygame.display.flip()
    #define times per second this will happen via clock defined above
    clock.tick(60)

#once logic loop and exit game
pygame.quit()
            
