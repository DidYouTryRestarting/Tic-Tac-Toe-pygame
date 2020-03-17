import pygame
import time
from sys import exit

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
playerX = pygame.image.load(r"C:\Users\John\Desktop\PYTHON\Python 3.8\Projects\Games\Local\In Progress\Tic Tac Toe Pygame\Best version\blueX.gif")
playerO = pygame.image.load(r"C:\Users\John\Desktop\PYTHON\Python 3.8\Projects\Games\Local\In Progress\Tic Tac Toe Pygame\Best version\blueO.jpg")
bg = pygame.image.load(r"C:\Users\John\Desktop\PYTHON\Python 3.8\Projects\Games\Local\In Progress\Tic Tac Toe Pygame\Best version\tic tac toe background.png")

playerX_width = 75
playerX_height = 75

playerO_width = 75
playerO_height = 75

#playerO = pygame.transform.scale(SCREEN, (75,75))



x = None
y = None

tile_0_X = (200-playerX_width, 225-playerX_height)
tile_1_X = (470-playerX_width, 225-playerX_height)
tile_2_X = (745-playerX_width, 225-playerX_height)
tile_3_X = (200-playerX_width, 480-playerX_height)
tile_4_X = (470-playerX_width, 480-playerX_height)
tile_5_X = (745-playerX_width, 480-playerX_height)
tile_6_X = (200-playerX_width, 770-playerX_height)
tile_7_X = (470-playerX_width, 770-playerX_height)
tile_8_X = (745-playerX_width, 770-playerX_height)

tile_0_O = (200-playerO_width, 225-playerO_height)
tile_1_O = (470-playerO_width, 225-playerO_height)
tile_2_O = (745-playerO_width, 225-playerO_height)
tile_3_O = (200-playerO_width, 480-playerO_height)
tile_4_O = (470-playerO_width, 480-playerO_height)
tile_5_O = (745-playerO_width, 480-playerO_height)
tile_6_O = (200-playerO_width, 770-playerO_height)
tile_7_O = (470-playerO_width, 770-playerO_height)
tile_8_O = (745-playerO_width, 770-playerO_height)



occupied_0_X = False  
occupied_1_X = False
occupied_2_X = False
occupied_3_X = False
occupied_4_X = False
occupied_5_X = False
occupied_6_X = False
occupied_7_X = False
occupied_8_X = False

occupied_0_O = False  
occupied_1_O = False
occupied_2_O = False
occupied_3_O = False
occupied_4_O = False
occupied_5_O = False
occupied_6_O = False
occupied_7_O = False
occupied_8_O = False





def draw_lines():                                                                   #* (SURFACE, COLOR, START POINT, END POINT, THICCNESS)
    pygame.draw.line(SCREEN, (255, 0, 0), (353, 100), (353, 900), 5)            #vertical left                       
    pygame.draw.line(SCREEN, (255, 0, 0), (636, 100), (636, 900), 5)            #vertical right
    pygame.draw.line(SCREEN, (255, 0, 0), (100, 353), (900, 353), 5)            #horizontal up
    pygame.draw.line(SCREEN, (255, 0, 0), (100, 636), (900, 636), 5)            #horizontal down


turn_X = True
turn_O = True


def check_clicks_forX():
    global occupied_0_X
    global occupied_1_X
    global occupied_2_X
    global occupied_3_X
    global occupied_4_X
    global occupied_5_X
    global occupied_6_X
    global occupied_7_X
    global occupied_8_X
    global occupied_1_O
    global turn_X
    global turn_O

    if x > -350 and x < 350 and x > 100 and y < 350 and y > 100 and occupied_0_X == False and occupied_0_O == False and turn_X == True:
        XPOS = pygame.mouse.get_pos()
        #print(XPOS)
        #print("tile 0") 
        SCREEN.blit(playerX, tile_0_X)
        occupied_0_X = True
        turn_X = False
        turn_O = True
        pygame.display.update()

    if x > 350 and x < 630 and y < 350 and y > 100 and occupied_1_X == False and occupied_1_O == False and turn_X == True:
        #print("tile 1")
        SCREEN.blit(playerX, tile_1_X)
        occupied_1_X = True
        turn_X = False
        turn_O = True
        pygame.display.update()

    if x > 630 and x < 900 and y < 350 and y > 100 and occupied_2_X == False and occupied_2_O == False and turn_X == True:
        #print("tile 2")
        SCREEN.blit(playerX, tile_2_X)
        occupied_2_X = True
        turn_X = False
        turn_O = True
        pygame.display.update()
#
    if y > 350 and y < 635 and x > 100 and x < 350 and occupied_3_X == False and occupied_3_O == False and turn_X == True:
        #print("tile 3")
        SCREEN.blit(playerX, tile_3_X)
        occupied_3_X = True
        turn_X = False
        turn_O = True
        pygame.display.update()

    if y > 350 and y < 635 and x > 360 and x < 635 and occupied_4_X == False and occupied_4_O == False and turn_X == True:
        #print("tile 4")
        SCREEN.blit(playerX, tile_4_X)
        occupied_4_X = True
        turn_X = False
        turn_O = True
        pygame.display.update()
        
#
    if y > 350 and y < 635 and x > 635 and x < 900 and occupied_5_X == False and occupied_5_O == False and turn_X == True:
        #print("tile 5")
        SCREEN.blit(playerX, tile_5_X)
        occupied_5_X = True
        turn_X = False
        turn_O = True
        pygame.display.update()

    if y > 635 and y < 900 and x > 100 and x < 350 and occupied_6_X == False and occupied_6_O == False and turn_X == True:
        #print("tile 6")
        SCREEN.blit(playerX, tile_6_X)
        occupied_6_X = True
        turn_X = False
        turn_O = True
        pygame.display.update()

    if y > 635 and y < 900 and x > 360 and x < 635 and occupied_7_X == False and occupied_7_O == False and turn_X == True:
        #print("tile 7")
        SCREEN.blit(playerX, tile_7_X)
        occupied_7_X = True
        turn_X = False
        turn_O = True
        pygame.display.update()
#
    if y > 635 and y < 900 and x > 635 and x < 900 and occupied_8_X == False and occupied_8_O == False and turn_X == True:
        #print("tile 8")
        SCREEN.blit(playerX, tile_8_X)
        occupied_8_X = True
        turn_X = False
        turn_O = True
        pygame.display.update()



def check_clicks_forO():
    global occupied_0_O
    global occupied_1_O
    global occupied_2_O
    global occupied_3_O
    global occupied_4_O
    global occupied_5_O
    global occupied_6_O
    global occupied_7_O
    global occupied_8_O
    global turn_O
    global turn_X

    if x > -350 and x < 350 and x > 100 and y < 350 and y > 100 and occupied_0_O == False and occupied_0_X == False and turn_O == True:
        XPOS = pygame.mouse.get_pos()
        print(XPOS)
        #print("tile 0") 
        SCREEN.blit(playerO, tile_0_O)
        occupied_0_O = True
        turn_O = False
        turn_X = True
        pygame.display.update()

    if x > 350 and x < 630 and y < 350 and y > 100 and occupied_1_O == False and occupied_1_X == False and turn_X == False and turn_O == True:
        #print("tile 1")
        SCREEN.blit(playerO, tile_1_O)
        occupied_1_O = True
        turn_O = False
        turn_X = True
        pygame.display.update()

    if x > 630 and x < 900 and y < 350 and y > 100 and occupied_2_O == False and occupied_2_X == False and turn_O == True:
        #print("tile 2")
        SCREEN.blit(playerO, tile_2_O)
        occupied_2_O = True
        turn_O = False
        turn_X = True
        pygame.display.update()
#
    if y > 350 and y < 635 and x > 100 and x < 350 and occupied_3_O == False and occupied_3_X == False and turn_O == True:
        #print("tile 3")
        SCREEN.blit(playerO, tile_3_O)
        occupied_3_O = True
        turn_O = False
        turn_X = True
        pygame.display.update()

    if y > 350 and y < 635 and x > 360 and x < 635 and occupied_4_O == False and occupied_4_X == False and turn_O == True:
        #print("tile 4")
        SCREEN.blit(playerO, tile_4_O)
        occupied_4_O = True
        turn_O = False
        turn_X = True
        pygame.display.update()
        
#
    if y > 350 and y < 635 and x > 635 and x < 900 and occupied_5_O == False and occupied_5_X == False and turn_O == True:
        #print("tile 5")
        SCREEN.blit(playerO, tile_5_O)
        occupied_5_O = True
        turn_O = False
        turn_X = True
        pygame.display.update()

    if y > 635 and y < 900 and x > 100 and x < 350 and occupied_6_O == False and occupied_6_X == False and turn_O == True:
        #print("tile 6")
        SCREEN.blit(playerO, tile_6_O)
        occupied_6_O = True
        turn_O = False
        turn_X = True
        pygame.display.update()

    if y > 635 and y < 900 and x > 360 and x < 635 and occupied_7_O == False and occupied_7_X == False and turn_O == True:
        #print("tile 7")
        SCREEN.blit(playerO, tile_7_O)
        occupied_7_O = True
        turn_O = False
        turn_X = True
        pygame.display.update()
#
    if y > 635 and y < 900 and x > 635 and x < 900 and occupied_8_O == False and occupied_8_X == False and turn_O == True:
        #print("tile 8")
        SCREEN.blit(playerO, tile_8_O)
        occupied_8_O = True
        turn_O = False
        turn_X = True
        pygame.display.update()

#player_X_won = print("player X won")

def did_X_win():
    if occupied_0_X == True and occupied_1_X == True and occupied_2_X == True:
        print("player X won")

    if occupied_3_X == True and occupied_4_X == True and occupied_5_X == True:
        print("player X won")
        

    if occupied_6_X == True and occupied_7_X == True and occupied_8_X == True:
        print("player X won")
        

    if occupied_0_X == True and occupied_3_X == True and occupied_6_X == True:
        print("player X won")
        

    if occupied_1_X == True and occupied_4_X == True and occupied_7_X == True:
        print("player X won")
        

    if occupied_2_X == True and occupied_5_X == True and occupied_8_X == True:
        print("player X won")
        

    if occupied_2_X == True and occupied_4_X == True and occupied_6_X == True:
        print("player X won")
        

    if occupied_0_X == True and occupied_4_X == True and occupied_8_X == True:
        print("player X won")
            

def did_O_win():
    if occupied_0_O == True and occupied_1_O == True and occupied_2_O == True:
        print("player O won")
            

    if occupied_3_O == True and occupied_4_O == True and occupied_5_O == True:
        print("player O won")
        

    if occupied_6_O == True and occupied_7_O == True and occupied_8_O == True:
        print("player O won")
        

    if occupied_0_O == True and occupied_3_O == True and occupied_6_O == True:
        print("player O won")
        

    if occupied_1_O == True and occupied_4_O == True and occupied_7_O == True:
        print("player O won")
        

    if occupied_2_O == True and occupied_5_O == True and occupied_8_O == True:
        print("player O won")
        

    if occupied_2_O == True and occupied_4_O == True and occupied_6_O == True:
        print("player O won")
        

    if occupied_0_O == True and occupied_4_O == True and occupied_8_O == True:
        print("player O won")
    




def draw_window():
    pygame.display.update()
    #SCREEN.blit(bg, (0,0))
    #SCREEN.blit(playerX, (60, 50))
    #pygame.display.update()
    


def main():
    global SCREEN
    
    global x, y

   
    
    
    run = True
    while run:
        
        
        for event in pygame.event.get():
            global x, y
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                x, y = pygame.mouse.get_pos()
                #print(x, y)
                check_clicks_forX()


            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                x, y = pygame.mouse.get_pos()
                check_clicks_forO()

        

        draw_window()
        did_X_win()
        did_O_win()
        draw_lines()

        #is_box_used()

    pygame.quit()
    quit()







main()
