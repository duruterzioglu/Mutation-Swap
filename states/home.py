import pygame
from elements import ButtonText

class Home:
    def __init__(self):
        self.background_im = pygame.image.load('images/menu.png')
        self.howtoplay = ButtonText("HOW TO PLAY", 360,40,(460,500))
        self.level_list = ["LEVEL: EASY", "LEVEL: MEDIUM", "LEVEL: HARD"]
        self.level_index = 0
        self.level = ButtonText(self.level_list[self.level_index], 360,40,(460,550))
        self.start = ButtonText("START", 360,40,(460,600))
        self.quit = ButtonText("QUIT", 360,40, (460,650))

    def draw(self, surface):
        surface.blit(self.background_im, (0,0)) 
        if self.level.draw(surface):
            self.level_index = (self.level_index + 1) % 3
            self.level = ButtonText(self.level_list[self.level_index], 360,40,(460,550))
        if self.howtoplay.draw(surface):
            return "Intro"
        elif self.start.draw(surface):
            return "MAIN"
        elif self.quit.draw(surface):
            self.running = False
            pygame.quit()
        return None