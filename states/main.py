import pygame
from elements import Button, Tools
from objects import ChromosomePiece, Chromosome
import random

class Main():
    home_image = pygame.image.load('images/home.png')
    home_image_hover = pygame.image.load('images/homehover.png')
    new_image = pygame.image.load('images/new.png')
    new_image_hover = pygame.image.load('images/newhover.png')
    restart_image = pygame.image.load('images/restart.png')
    restart_image_hover = pygame.image.load('images/restarthover.png')
    deletion_image = pygame.image.load('images/deletionicon.png')
    deletion_image_hover = pygame.image.load('images/deletioniconhover.png')
    duplication_image = pygame.image.load('images/duplicationicon.png')
    duplication_image_hover = pygame.image.load('images/duplicationiconhover.png')
    inversion_image = pygame.image.load('images/inversionicon.png')
    inversion_image_hover = pygame.image.load('images/inversioniconhover.png')
    

    def __init__(self):
        self.home_button = Button(1191, 56, self.home_image, self.home_image_hover)
        self.new_button = Button(1191, 150, self.new_image, self.new_image_hover)
        self.restart_button = Button(1191, 244, self.restart_image, self.restart_image_hover)
        self.deletion_button = Tools(70, 139, self.deletion_image, self.deletion_image_hover)
        self.duplication_button = Tools(70, 316, self.duplication_image, self.duplication_image_hover)
        self.inversion_button = Tools(70, 493, self.inversion_image, self.inversion_image_hover)
        self.selected_index = None
        self.selected_chromosome = None
        self.selected_tool = None   
        self.font = pygame.font.SysFont("georgiapro", 30, bold = True) 
        self.won_sound = pygame.mixer.Sound("images/correct.wav")
        self.lost_sound = pygame.mixer.Sound("images/wrong.wav")
        self.sound_played = False
        self.init_heights = []
        self.init_colors = []
        self.level_index = 0
        
        self.new_game(self.level_index)
        self.update_counter()
        
    def new_game(self, difficulty=None):
        self.selected_tool = None
        self.first_index2 = None
        self.sound_played = False
        if self != None:
            self.max_move = 1

        if difficulty != None:
            self.level_index = difficulty

        self.level_index = difficulty        

        self.init_heights = []
        self.init_colors = []

        for i in range(10):
            height_rand = random.randint(15,55)
            self.init_heights.append(height_rand)

        start_val = 255
        self.init_colors = []
        for i in range(10):
            val = start_val - (i * 28)
            self.init_colors.append((val, val, val))
        
        self.chromosome1 = Chromosome(649, self.init_heights, self.init_colors, interactive= False)
        self.chromosome2 = Chromosome(710, self.init_heights, self.init_colors)
        self.mutate()
        self.counter = self.max_move
        self.update_counter()

        self.chromosome2.clear_highlights()
        self.first_index1 = None
        self.first_index2 = None
        self.deletion_button.activated = False
        self.duplication_button.activated = False
        self.inversion_button.activated = False
        
    def restart_level(self):
        self.selected_tool = None
        self.first_index2 = None
        self.sound_played = False
        self.counter = self.max_move
        
        self.chromosome2 = Chromosome(710, self.init_heights, self.init_colors)
        
        self.deletion_button.activated = False
        self.duplication_button.activated = False
        self.inversion_button.activated = False
        self.update_counter()

    def update_counter(self):
        self.text = self.font.render(f"{self.counter}", True , '#2B2b2b')
        self.text_rect = self.text.get_rect(center = (1222, 652))

        if self.counter <= 0:
            return True
        return False

    
    def mutate(self):
        mutation_no = 0
        if self.level_index == 0:
            mutation_no = random.randint(2, 4)
            self.max_move = mutation_no + 3
        elif self.level_index == 1:
            mutation_no = random.randint(3, 5)
            self.max_move = mutation_no
        elif self.level_index == 2:
            mutation_no = random.randint(9, 11)
            self.max_move = mutation_no
        
        for _ in range(mutation_no):
            if len(self.chromosome1.pieces) == 0:
                break
            mutation_type = random.choice(["del", "dup", "inv"])
            idx = random.randint(0, len(self.chromosome1.pieces) - 1)
            if mutation_type == "del":
                self.chromosome1.deletion(idx)
            elif mutation_type == "dup":
                self.chromosome1.duplication(idx)
            elif mutation_type == "inv":
                end_idx = random.randint(0, len(self.chromosome1.pieces) - 1)
                self.chromosome1.inversion(idx, end_idx)
    
    def check(self):
        original_seq = []
        for i in self.chromosome1.pieces:
            original_seq.append(i.id)

        mutated_seq = []
        for i in self.chromosome2.pieces:
            mutated_seq.append(i.id)
        
        if original_seq == mutated_seq:
            return True
        return False


    def draw(self, surface):
        surface.fill((243,213,212))

        pygame.draw.rect(surface, (255,255,255), pygame.Rect((50,50),(168,620)), border_radius=15)
        pygame.draw.rect(surface, (43,43,43), pygame.Rect((50,50),(168,620)), border_radius=15, width = 8)
        
        pygame.draw.rect(surface, "#D69B9D", pygame.Rect((252,50),(450,620)),border_radius=15)
        pygame.draw.rect(surface, "#D69B9D", pygame.Rect((692,50),(10,620)))
        pygame.draw.rect(surface, "#2B2B2B", pygame.Rect((252,50),(900,620)), border_radius=15, width = 8)
        
        font = pygame.font.SysFont("georgiapro", 20, bold = True) 
        self.move_count_text = font.render(f"MOVES", True , '#2B2b2b')
        self.move_count_text_rect = self.move_count_text.get_rect(center = (1222, 597))
        self.move_count_text1 = font.render(f"LEFT :", True , '#2B2b2b')
        self.move_count_text_rect1 = self.move_count_text1.get_rect(center = (1222, 620))
        self.move_count_text_rect1 = self.move_count_text1.get_rect(center = (1222, 620))
        font = pygame.font.SysFont("georgiapro", 35, bold = True) 
        self.original_text = font.render(f"ORIGINAL", True , '#2B2b2b')
        self.original_text_rect = self.original_text.get_rect(center = (370, 90))
        self.mutated_text = font.render(f"MUTATED", True , '#2B2b2b')
        self.mutated_text_rect = self.mutated_text.get_rect(center = (1034, 90))
        self.tools_text = font.render(f"TOOLS", True , '#2B2b2b')
        font = pygame.font.SysFont("georgiapro", 18, bold = True) 
        self.level_list = ["LEVEL: EASY", "LEVEL: MEDIUM", "LEVEL: HARD"]
        self.level_difficulty_text = font.render(self.level_list[self.level_index], True , '#2B2b2b')
        self.level_difficulty_rect = self.level_difficulty_text.get_rect(center = (134, 25))
        self.tools_text_rect = self.tools_text.get_rect(center = (134, 90))
        
        surface.blit(self.move_count_text1, self.move_count_text_rect1)
        surface.blit(self.move_count_text, self.move_count_text_rect)
        surface.blit(self.original_text, self.original_text_rect)
        surface.blit(self.mutated_text, self.mutated_text_rect)
        surface.blit(self.level_difficulty_text, self.level_difficulty_rect)
        surface.blit(self.tools_text, self.tools_text_rect)

        surface.blit(self.text, self.text_rect)
        
        game_won = self.check()
        game_lost = self.counter <= 0 and not game_won

        self.chromosome2.interactive = not (game_lost or game_won)
        

        index1 = self.chromosome1.draw(surface) 
        index2 = self.chromosome2.draw(surface)
        
        # VERY IMPORTANT: if you do 
        # if self.chromosome1.draw(surface):
        #    index = self.chromosome1.draw(surface)
        # it will rerun the function after it is clicked and therefore the output will be None, learned it the hard way...
        
        if self.home_button.draw(surface):
            return "HOME"
        if self.new_button.draw(surface):
            self.new_game(self.level_index)    
        if self.restart_button.draw(surface):
            self.restart_level()           
        if self.deletion_button.draw(surface):
            if self.first_index2 is not None:
                self.chromosome2.pieces[self.first_index2].highlighted = False
                self.first_index2 = None
            if self.selected_tool == "deletion":
                self.selected_tool = None
                self.deletion_button.activated = False
            else:
                self.selected_tool = "deletion"
                self.deletion_button.activated = True
                self.duplication_button.activated = False
                self.inversion_button.activated = False
        if self.duplication_button.draw(surface):
            if self.first_index2 is not None:
                self.chromosome2.pieces[self.first_index2].highlighted = False
                self.first_index2 = None
            if self.selected_tool == "duplication":
                self.selected_tool = None
                self.duplication_button.activated = False
            else:
                self.selected_tool = "duplication"
                self.duplication_button.activated = True
                self.deletion_button.activated = False
                self.inversion_button.activated = False
        if self.inversion_button.draw(surface):
            if self.selected_tool == "inversion":
                self.selected_tool = None
                self.inversion_button.activated = False
                self.first_index2 = None
            else:
                self.selected_tool = "inversion"
                self.inversion_button.activated = True
                self.deletion_button.activated = False
                self.duplication_button.activated = False
        

        if index2 is not None and self.chromosome2.interactive:
            self.selected_index = index2
            self.selected_chromosome = 2
            if self.selected_tool == "deletion":
                self.chromosome2.deletion(index2)
                self.counter -= 1
                self.update_counter()
            elif self.selected_tool == "duplication":

                self.chromosome2.duplication(index2)
                self.counter -= 1
                self.update_counter()
            elif self.selected_tool == "inversion":
                if self.first_index2 == None:
                    self.first_index2 = index2
                    self.chromosome2.pieces[index2].highlighted = True
                else:
                    self.chromosome2.inversion(self.first_index2, index2)
                    self.chromosome2.clear_highlights()
                                        
                    self.first_index2 = None
                    self.counter -= 1
                    self.update_counter()

            if self.counter <= 0 and not self.check():
                if not self.sound_played:
                    pygame.mixer.Sound.play(self.lost_sound)
                    self.sound_played = True
            if self.check():
                if not self.sound_played:
                    pygame.mixer.Sound.play(self.won_sound)
                    self.sound_played = True

        pygame.draw.circle(surface, (50,50,50), (702,220), 25, width=0)

        if game_won:
            self.congrats_text = self.font.render(f"Puzzle Solved!", True , "#7c7bac")
            self.congrats_rect = self.congrats_text.get_rect(center = (702, 695))
            surface.blit(self.congrats_text, self.congrats_rect)
            
        if game_lost:
            self.gameover_text = self.font.render(f"Maximum Moves Reached!", True , "#7a0000")
            self.gameover_rect = self.gameover_text.get_rect(center = (702, 695))
            surface.blit(self.gameover_text, self.gameover_rect)
    