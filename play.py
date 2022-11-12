from constants import *

SCREEN = pygame.display.set_mode(SCREEN_SIZE)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(NAVYBLUE)

        PLAY_PAUSE = Button(pos=(SCREEN_WIDTH//10 * 9, SCREEN_HEIGHT//12), 
                            text_input="PAUSE", font=get_font(32), base_color=BLACK, hovering_color=NAVYBLUE)
        PLAY_QUIT = Button(pos=(SCREEN_WIDTH//10 * 9, (SCREEN_HEIGHT//12)*2), 
                            text_input="QUIT", font=get_font(32), base_color=BLACK, hovering_color=RED)
                            
        BALLOON = pygame.transform.scale(pygame.image.load("assets/imgs/balloon.png"), (100,80))
        BALLOON_TESTE = Baloon(image=BALLOON, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2), name="1", gender="M", material="stone", speed=3, weigh=4, health=10 )
        BALLOON_TESTE.update(SCREEN)
        PLAY_PAUSE.changeColor(PLAY_MOUSE_POS)
        PLAY_PAUSE.update(SCREEN)
        PLAY_QUIT.changeColor(PLAY_MOUSE_POS)
        PLAY_QUIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_PAUSE.checkForInput(PLAY_MOUSE_POS):
                    paused()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BALLOON_TESTE.ballonClick(PLAY_MOUSE_POS):
                    print("balao")


            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_QUIT.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def paused():
    while True:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        PAUSE_TEXT = get_font(45).render("PAUSED", True, BLACK)
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        SCREEN.blit(PAUSE_TEXT, PAUSE_RECT)

        PAUSE_RESUME = Button(pos=(SCREEN_WIDTH//2, (SCREEN_HEIGHT//10 )*6), 
                            text_input="RESUME", font=get_font(32), base_color=BLACK, hovering_color=BLUE)
        
        PAUSE_QUIT = Button(pos=(SCREEN_WIDTH//2, (SCREEN_HEIGHT//10 )*7), 
                            text_input="QUIT", font=get_font(32), base_color=BLACK, hovering_color=RED)

        PAUSE_RESUME.changeColor(PAUSE_MOUSE_POS)
        PAUSE_RESUME.update(SCREEN)
        PAUSE_QUIT.changeColor(PAUSE_MOUSE_POS)
        PAUSE_QUIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE_RESUME.checkForInput(PAUSE_MOUSE_POS):
                    play()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE_QUIT.checkForInput(PAUSE_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()