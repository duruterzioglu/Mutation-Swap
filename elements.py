import pygame

class ButtonText():
    def __init__(self, text, width, height, pos):
        # rectangle
        self.rect = pygame.Rect(pos, (width,height))
        self.rect_color = "#D69B9D"

        # text
        font = pygame.font.SysFont("georgiapro",30, bold = True)
        self.text = font.render(text, True , '#251A2C')
        self.text_rect = self.text.get_rect(center = self.rect.center)
        
        self.clicked = False

    def draw(self,surface):
        pygame.draw.rect(surface, self.rect_color, self.rect, border_radius=10)
        surface.blit(self.text, self.text_rect)
        return self.check_click()
    
    def check_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.rect_color = "#BD686D"
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
            else:
                if self.clicked == True:
                    self.clicked = False
                    action = True
        else:
            self.rect_color = "#D69B9D"

        return action
    

class Button():
    def __init__(self, x, y, image,image_hover):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self,surface):
        self.display_image = self.image
        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.display_image = self.image_hover
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
            else:
                if self.clicked == True:
                    self.clicked = False
                    action = True

        surface.blit(self.display_image, (self.rect.x, self.rect.y))

        return action
    

class Tools():
    """
    Almost identical to button class, with the only difference being that if activated it enters a different state and the hover image is fixed to show the user it is being clicked.
    """ 
    def __init__(self, x, y, image,image_hover):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.activated = False

    def draw(self,surface):
        if self.activated:
            self.display_image = self.image_hover
        else:
            self.display_image = self.image
        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.display_image = self.image_hover
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
            else:
                if self.clicked == True:
                    self.clicked = False
                    action = True

        surface.blit(self.display_image, (self.rect.x, self.rect.y))

        return action