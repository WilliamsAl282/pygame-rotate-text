import pygame
import sys
import config # Import the config Module
import random
import shapes


def init_game():
    pygame.init()

    pygame.font.init()
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
# def show_name(first_name, last_name, middle_name = None):
#             if middle_name:
#                 output = f"{first_name}{middle_name}{last_name}"
#             else:
#                  output = f"{first_name}{last_name}"
#             return output
# print(show_name("John","Jenkins"))
# print(show_name("John","Jenkins","Micheal"))

def draw_text(screen,text,font_name,font_size, color,position, anti_aliased = True, italic = False, bold = False, rotation = 0):
    pygame.font.init()
    if font_name:
         font = pygame.font.Font(font_name,font_size)
    else:
         font = pygame.font.Font(None, font_size)

    font.set_bold(bold)
    font.set_italic(italic)

    text_surface = font.render(text, True, color)

    if rotation != 0:
        text_surface = pygame.transform.rotate(text_surface,rotation)

    text_rect = text_surface.get_rect(center =(position))

    screen.blit(text_surface, position)
    




def main():
    screen = init_game()
    running = True
    clock = pygame.time.Clock() # Initialize the clock here
    

    font_name = "FreeMono.ttf"
    font_color1 = config.RED
    font_color2 = config.PURPLE
    font_color3 = config.ORANGE
    font_size_normal = 36
    font_size_bold_italic = 30
    font_size_custom = 48

    custom_font_name = 'LiberationMono-Italic (1).ttf'

    text_position_1 = [50,50]
    text_position_2 = [225,135]
    text_position_3 = [220,370]

    



    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
    

        draw_text(screen,"Hello,Pygame!", font_name, font_size_normal, font_color1,text_position_1,italic=True)

        draw_text(screen, "This is bold and italic text",font_name, font_size_bold_italic,font_color2,text_position_2,italic = True, bold = True)


        draw_text(screen, "Cool Text",custom_font_name,font_size_normal,font_color3,text_position_3, rotation = 50)

        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()