import pygame
import random

pygame.init()

w, h = 800, 800
red = (255, 0,0)
h=800
red = (255, 0 ,0)
blue = (0,0,255)
rectx = 200
recty = 375
circlex = random.randint(20, w-20)
circlerad = 20
rect = pygame.Rect(rectx, recty, 50, 50)
screen = pygame.display.set_mode((w, h))


last_time = pygame.time.get_ticks()
score = 0
score_increment = 1
# Create Caption and Clock
pygame.display.set_caption(" Snake Game")
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
balls = []
block = 0
block_speed = 5
# Function to display the score
def show_score(color, font, size):
      
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    screen.blit(score_surface, score_rect)
    
def game_over(color, font, size):
      
    # creating font object score_font
    game_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    game_surface = game_font.render('GAME OVER', True, color)
    
    # create a rectangular object for the text
    # surface object
    game_rect = game_surface.get_rect()
    
    game_rect.center = (w// 2, h //2)
    
    # displaying text
    screen.blit(game_surface, game_rect)


running = True

# Main game loop
while running:
    screen.fill((255,255,255))
    # Movement of the rectangle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                recty -= 50
            elif event.key == pygame.K_DOWN:
                recty += 50
            elif event.key == pygame.K_LEFT:
                rectx -= 50
            elif event.key == pygame.K_RIGHT:
                rectx += 50 
                
    # Draw the Circle 
    circle_rect = pygame.draw.circle(screen, red, (circlex, block ), circlerad)
    block += block_speed
    # Allow circle to have a random x position

    current_time = pygame.time.get_ticks()
    if current_time - last_time > 3000:
        circlex = random.randint(20, w-20)
        y = 0
        balls.append((circlex, y))
        last_time = current_time
        
    
    pygame.draw.rect(screen, blue, rect, 0)
    # Check for collision   
    if rect.colliderect(circle_rect):
        print("Game over")
        game_over((255, 0, 0), 'freesansbold.ttf', 64)
        pygame.display.flip()
        pygame.time.delay(4000)
        running = False
    # Check if the circle has fallen below the screen
    # and if it is not colliding with the rectangle
    if block > h:
        if not rect.colliderect(circle_rect):
            block = 0
            circlex = random.randint(20, w-20)
            score += score_increment
            if score % 5 == 0:
                block_speed += 1
                circlerad += 5
                
    # Display the score
    show_score((0, 0, 0), 'freesansbold.ttf', 32)
    # Update the display
    clock.tick(60)
    rect.x = rectx
    rect.y = recty
    pygame.display.set_caption(f" Surrvive the falling Circle: {score} - Ball Speed: {block_speed}")
    pygame.display.flip()