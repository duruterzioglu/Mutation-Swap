import pygame
from elements import Button

class Intro:
    def __init__(self):
        self.background_image = pygame.image.load('images/Intro.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)

    def draw(self, surface):
        surface.blit(self.background_image, (0,0))
        if self.next_button.draw(surface):
            return "DNAinfo"
        elif self.back_button.draw(surface):
            return "HOME"
        elif self.home_button.draw(surface):
            return "HOME"
        return None
    
class DNAinfo:
    def __init__(self):
        self.background_image = pygame.image.load('images/Info_screen.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)

    def draw(self, surface):
        surface.blit(self.background_image, (0,0))
        if self.next_button.draw(surface):
            return "DNAinfo2"
        elif self.back_button.draw(surface):
            return "Intro"
        elif self.home_button.draw(surface):
            return "HOME"
        return None

class DNAinfo2:
    def __init__(self):
        self.background_image = pygame.image.load('images/Info_screen2.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)

    def draw(self, surface):
        surface.blit(self.background_image, (0,0))
        if self.next_button.draw(surface):
            return "Deletion"
        elif self.back_button.draw(surface):
            return "DNAinfo"
        elif self.home_button.draw(surface):
            return "HOME"
        return None
    
class Deletion:
    def __init__(self):
        self.background_image = pygame.image.load('images/Deletion.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)
        
    def draw(self, surface):
        surface.blit(self.background_image, (0,0)) 
        if self.next_button.draw(surface):
            return "Duplication"
        elif self.back_button.draw(surface):
            return "DNAinfo2"
        elif self.home_button.draw(surface):
            return "HOME"
        return None

class Duplication:
    def __init__(self):
        self.background_image = pygame.image.load('images/Duplication.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)   
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)

    def draw(self, surface):
        surface.blit(self.background_image, (0,0)) 
        if self.next_button.draw(surface):
            return "Inversion"
        elif self.back_button.draw(surface):
            return "Deletion"
        elif self.home_button.draw(surface):
            return "HOME"
        
        return None
    
class Inversion:
    def __init__(self):
        self.background_image = pygame.image.load('images/Inversion.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)

    def draw(self, surface):
        surface.blit(self.background_image, (0,0)) 
        if self.next_button.draw(surface):
            return "ToolInfo"
        elif self.back_button.draw(surface):
            return "Duplication"
        elif self.home_button.draw(surface):
            return "HOME"
        
class ToolInfo:

    def __init__(self):
        self.background_image = pygame.image.load('images/Tool_info.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.deletion_image = pygame.image.load('images/deletionicon.png')
        self.duplication_image = pygame.image.load('images/duplicationicon.png')
        self.inversion_image = pygame.image.load('images/inversionicon.png')
        #self.restart_image = pygame.image.load('images/restart.png')
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)

    def draw(self, surface):
        surface.blit(self.background_image, (0,0)) 

    
        font = pygame.font.SysFont("georgiapro", 35, bold = True) 
        self.tools_text = font.render(f"TOOLS", True , '#2B2b2b')
        self.tools_text_rect = self.tools_text.get_rect(center = (134, 90))
        pygame.draw.rect(surface, (255,255,255), pygame.Rect((50,50),(168,620)), border_radius=15)
        pygame.draw.rect(surface, (43,43,43), pygame.Rect((50,50),(168,620)), border_radius=15, width = 8)
        
        surface.blit(self.tools_text, self.tools_text_rect)
        surface.blit(self.deletion_image, (70, 139))
        surface.blit(self.duplication_image,(70, 316))
        surface.blit(self.inversion_image, (70, 493))
        #surface.blit(self.restart_image, (1191, 150))

        if self.next_button.draw(surface):
            return "Aim"
        elif self.back_button.draw(surface):
            return "Inversion"
        elif self.home_button.draw(surface):
            return "HOME"
        
class Aim():
    def __init__(self):
        self.background_image = pygame.image.load('images/Aim.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)

    def draw(self, surface):
        surface.blit(self.background_image, (0,0)) 
        if self.next_button.draw(surface):
            return "CSLink"
        elif self.back_button.draw(surface):
            return "ToolInfo"
        elif self.home_button.draw(surface):
            return "HOME"

class CSLink():
    def __init__(self):
        self.background_image = pygame.image.load('images/CSLink.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)

    def draw(self, surface):
        surface.blit(self.background_image, (0,0)) 
        if self.next_button.draw(surface):
            return "Vaccines"
        elif self.back_button.draw(surface):
            return "Aim"
        elif self.home_button.draw(surface):
            return "HOME"

class Vaccines():
    def __init__(self):
        self.background_image = pygame.image.load('images/Vaccines.png')
        self.arrow_image = pygame.image.load('images/arrow.png').convert_alpha()
        self.arrow_image_hover = pygame.image.load('images/arrowhover.png').convert_alpha()
        self.home_image = pygame.image.load('images/home.png').convert_alpha()
        self.home_image_hover = pygame.image.load('images/homehover.png').convert_alpha()
        self.next_button = Button(1191, 606, self.arrow_image, self.arrow_image_hover)
        self.home_button = Button(1191, 36, self.home_image, self.home_image_hover)
        self.backarrow_image = pygame.image.load('images/arrowback.png').convert_alpha()
        self.backarrow_image_hover = pygame.image.load('images/arrowhoverback.png').convert_alpha()
        self.back_button = Button(1110, 606, self.backarrow_image, self.backarrow_image_hover)

    def draw(self, surface):
        surface.blit(self.background_image, (0,0)) 
        if self.next_button.draw(surface) or self.home_button.draw(surface):
            return "HOME"
        elif self.back_button.draw(surface):
            return "CSLink"