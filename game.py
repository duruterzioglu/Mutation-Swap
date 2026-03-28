import pygame
from states.home import Home
from states.info_screens import DNAinfo, DNAinfo2, Deletion, Duplication, Inversion, ToolInfo, Aim, Intro, CSLink, Vaccines
from states.main import Main

screen_size_x = 1280
screen_size_y = 720

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_size_x ,screen_size_y))
        pygame.display.set_caption("Home")
        self.states = {
            "HOME": Home(),
            "Intro": Intro(),
            "DNAinfo": DNAinfo(),
            "DNAinfo2": DNAinfo2(),
            "Deletion": Deletion(),
            "Inversion": Inversion(),
            "Duplication": Duplication(),
            "ToolInfo": ToolInfo(),
            "Aim": Aim(),
            "CSLink": CSLink(),
            "Vaccines": Vaccines(),
            "MAIN": Main()
        }
        self.current_state = self.states["HOME"]
        self.running= True
    
    def run(self):
        while self.running:                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            next_state = self.current_state.draw(self.screen)
            if next_state:
                if next_state == "MAIN":
                    difficulty = self.current_state.level_index
                    self.states["MAIN"].new_game(difficulty)
                self.current_state = self.states[next_state]
            pygame.display.update()
    
if __name__ == "__main__":
    my_game = Game()
    my_game.run()