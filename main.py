from constants import *
from play import *

pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption(ORIGINAL_CAPTION)

BG = pygame.image.load("assets/backgrounds/Background.png")




def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(pos=(SCREEN_WIDTH//10, SCREEN_HEIGHT//12), 
                            text_input="PLAY", font=get_font(32), base_color=WHITE, hovering_color=NAVYBLUE)
        QUIT_BUTTON = Button(pos=(SCREEN_WIDTH//10 * 9, SCREEN_HEIGHT//12), 
                            text_input="QUIT", font=get_font(32), base_color=WHITE, hovering_color=RED)


        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()