#we first import pygame library
import pygame

#initialize pygame
pygame.init()

#define colors
black = (0,0,0)
white = (0,191,255)
red = (255,0,0)

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

#define function to draw circle
def ball(x,y):
   pygame.draw.circle(screen,red,(x,y),20)

def gameover():
    font = pygame.font.SysFont(None,25)
    text = font.render("Game over ", True, black)
    screen.blit(text, [150,250])

#while logic to keep game running
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 5

    screen.fill(white)
    #call function to draew the ball
    ball(x,y)

    #adjust vertical y position
    #y = y + y_speed
    y += y_speed
    x += x_speed

    #once 'y' is changes check if ground is touches hence game over
    if y > ground:
        gameover()
        #to stop the ball
        y_speed = 0

    #refresh screen by flipping like a flipbook new animation 
    pygame.display.flip()
    #define times per second this will happen via clock defined above
    clock.tick(60)

#once logic loop and exit game
pygame.quit()
            
