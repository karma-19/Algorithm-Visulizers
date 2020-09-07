import pygame, sys, random

""" PYGAME PRACTICE 
PROJECT NAME : BUBBLE SORT VISUALIZER 
CREATED ON 08/21/2020 """
 
pygame.init()
#screen window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH , HEIGHT))

#caption
pygame.display.set_caption('BUBBLE SORT - PRAVEEN VISHWAKARMA ')

#icon
#icon = pygame.image.load("C:/Users/LG/Desktop/college/pygame_icon.png")
#pygame.display.set_icon(icon)

#clock
clock = pygame.time.Clock()


#bar width 
n = 8
w = WIDTH//n

height_arr = []
#color changing array
c_c = []


for i in range(w):
    height_arr.append(random.randint(10, 550))
    c_c.append(1)
    


counter = 0


while True:
    #screen background
    screen.fill((3, 252, 185))
    
    #sorting
    if counter<len(height_arr):
        for j in range(len(height_arr)-1-counter):
            if height_arr[j]>height_arr[j+1]:
                c_c[j] = 0
                c_c[j+1] = 0
                temp = height_arr[j]
                height_arr[j] = height_arr[j+1]
                height_arr[j+1] = temp
            else:
                c_c[j] = 1
                c_c[j+1] = 1
    counter+=1
    
    #changing color c_c array implementation
    if len(height_arr)-counter >= 0:
        c_c[len(height_arr)-counter] = 2
        
    
        
    
    
    #printing the bar on the screen
    for i in range(len(height_arr)):
        if c_c[i] == 0:
            color = (255, 0, 0)
        elif c_c[i] == 2:
            color = (52,174, 235)
        else:
            color = (235, 215, 52)
        pygame.draw.rect(screen, color, (i*n, HEIGHT-height_arr[i], n, height_arr[i]))
    
    #event 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    clock.tick(10)
    pygame.display.update()
