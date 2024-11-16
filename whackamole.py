import pygame

'''def grid_lines():
    for i in range(1, 32):
        for j in range(1, 32):
            pygame.draw.line(screen, "black", (0, i*0.625), (640, i*0.625))'''

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        #pygame.draw.line(screen, "black", (0, 20), (640, 20), 10)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")

            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))

            '''for i in range(1, 32):
                for j in range(1, 32):
                    pygame.draw.line(screen, "black", (0, i * 20), (640, i * 20), 10)'''

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
