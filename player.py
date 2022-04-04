import pygame

# Création de mon joueur et de ses caractéristiques

class Player(pygame.sprite.Sprite) :

    def __init__(self):
        
        super().__init__()
        self.health = 3
        self.max_health = 3
        self.sword_attack = 2
        self.gun_attack = 5
        self.velocity = 5
        self.image = pygame.image.load("assets/Player/explorer.png").convert_alpha()
        self.numImages = 16
        self.current = 0
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 350
    
    def update(self, start, end) :

        if (self.current == end) or (self.current >= self.numImages - 1) :
            self.current = start
        else :
            pygame.time.delay(50)
            self.current += 1

    
    
    def render(self, screen) : 
        screen.blit(self.image, (self.rect.x, self.rect.y), (self.current * 32, 0, 32, 32))


    def move_right(self) :
        self.rect.x += self.velocity
        self.update(0, 7)

    def move_left(self) :
        self.rect.x -= self.velocity
        self.update(8, 16)

    def jump(self) :
        pass



