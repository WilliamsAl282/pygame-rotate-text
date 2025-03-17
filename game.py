import pygame
import sys
import config # Import the config Module
import random
import shapes


def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constanst from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    screen = init_game()
    running = True
    clock = pygame.time.Clock() # Initialize the clock her
    shapes_list = []
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        shape_type = random.randrange(3)

        if shape_type == 0:

            new_shape = {
                'type': 'circle',
                'color': (random.randrange(255),random.randrange(255),random.randrange(255)),
                'position': (random.randrange(config.WINDOW_WIDTH),random.randrange(config.WINDOW_HEIGHT)),
                'radius': 50
            }

        elif shape_type == 1:
            new_shape = {
               'type': 'rectangle',
                'color': (random.randrange(255),random.randrange(255),random.randrange(255)),
                'position': (random.randrange(config.WINDOW_WIDTH-100),random.randrange(config.WINDOW_HEIGHT-100)),
                'width': 100,
                'height': 100 
            }

        elif shape_type == 2:
            new_shape = {
               'type': 'line',
                'color': (random.randrange(255),random.randrange(255),random.randrange(255)),
                'start_pos': (random.randrange(config.WINDOW_WIDTH-100),random.randrange(config.WINDOW_HEIGHT-100)),
                'end_pos': (random.randrange(config.WINDOW_WIDTH-100),random.randrange(config.WINDOW_HEIGHT-100)),
                'width': 10
            }

        shapes_list.append(new_shape)


        for shape in shapes_list:
            if shape['type'] == 'circle':
                shapes.draw_circle(screen,shape)
            elif shape['type'] == 'rectangle':
                shapes.draw_rect(screen,shape)
            elif shape['type'] == 'line':
                shapes.draw_line(screen,shape)

        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()