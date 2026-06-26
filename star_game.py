import pygame
import sys
from settings import Settings
from star import Star
from random import randint

class GameStar:
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.setting.screen_width,
                                               self.setting.screen_height,
                                               ))
        pygame.display.set_caption("Star Game")
        self.stars = pygame.sprite.Group()

        self._create_constellation()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip() 
    
    def _create_star(self, position_x, position_y):
        new_star = Star(self)

        random_offset_x = randint(-30, 30)
        random_offset_y = randint(-30, 30)

        new_star.rect.x = position_x + random_offset_x
        new_star.rect.y = position_y + random_offset_y

        new_star.x = float(new_star.rect.x)
        self.stars.add(new_star)

    def _create_constellation(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = star_width, star_height

        while current_y < (self.setting.screen_height - 2 * star_height):

            while current_x < (self.setting.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width
            current_x = star_width
            current_y +=  2 * star_height

if __name__ == '__main__':
    st = GameStar()
    st.run_game()
    