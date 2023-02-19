import pygame

class Ship:

    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('./img/ship.bmp')
        # self.image = pygame.transform.scale(pygame.image.load('./img/ship.bmp'), (100, 70))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    

    # Update the ship's position bases on movements flags
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
        # if self.moving_right:
            # self.rect.x += 1
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
        # if self.moving_left:
            # self.rect.x -= 1
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
      

    def blitme(self):
        self.screen.blit(self.image, self.rect)



