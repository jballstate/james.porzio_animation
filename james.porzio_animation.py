# import pygame
import pygame
# define new function for main
def main():
# initialize pygame
    pygame.init()
# create pygame window
    screen = pygame.display.set_mode((640, 480))
# create window caption
    pygame.display.set_caption("James Games")
# create background 
    background = pygame.Surface(screen.get_size())
    background = background.convert()
# make the background blue
    background.fill("blue")
# add coin image from file
    mycoin = pygame.image.load("coin.png")
    mycoin = mycoin.convert_alpha()
# scale coin to correct size 
    mycoin = pygame.transform.scale(mycoin, (75, 75))
# add background image from file
    backg = pygame.image.load("backgg.png")
    backg = backg.convert_alpha()
# scale background to correct size
    backg = pygame.transform.scale(backg, (640, 500))
# move background to correct position
    backg_x = 0
    backg_y = 0
# move coin to correct position
    mycoin_x = 0
    mycoin_y = 175
# action/assign values to variables
    clock = pygame.time.Clock()
    keepGoing = True
# create while loop
    while keepGoing:
# time is 30 frames per second
        clock.tick(30)
# event handling 
        for event in pygame.event.get():
# if user quits, end game
            if event.type == pygame.QUIT:
                keepGoing = False
# speed of coin image movement
        mycoin_x += 5
# when coin image reaches end of screen, reset position
        if mycoin_x > screen.get_width():
            mycoin_x = 0
# show background color on screen at specific position
        screen.blit(background, (0, 0))
# show background image on screen at specifc position
        screen.blit(backg, (backg_x, backg_y))
# show coin image on screen at specific position
        screen.blit(mycoin, (mycoin_x, mycoin_y))
# refresh display
        pygame.display.flip()
# end the game
    pygame.quit()
# if name is main, call main function to start game
if __name__ == "__main__":
    main()