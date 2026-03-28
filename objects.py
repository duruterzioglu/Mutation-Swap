import pygame

class ChromosomePiece():
    def __init__(self, rect, color):
        self.rect = rect
        self.original_color = color
        self.rect_color = color
        self.clicked = False
        self.highlighted = False

class Chromosome():
    def __init__(self, pos_x, heights, colors, interactive= True):
        self.width = 45
        self.pieces = [] 
        self.interactive = interactive   

        for i in range(len(heights)):
            rect = pygame.Rect(pos_x, 0, self.width, heights[i])
            pieces = ChromosomePiece(rect, colors[i])
            pieces.id = i
            self.pieces.append(pieces)
        
        self.reposition()
    
    def draw(self, surface):

        pos = pygame.mouse.get_pos()
        for i, piece in enumerate(self.pieces):
            if self.interactive and piece.rect.collidepoint(pos):
                piece.rect_color = "#BD686D"

                if pygame.mouse.get_pressed()[0] == 1:
                    piece.clicked = True
                elif piece.clicked and (pygame.mouse.get_pressed()[0] == 0) : # ACTIVATES WHEN CLICKED OUTT!!!
                    piece.clicked = False
                    return i
            elif piece.highlighted:
                piece.rect_color = "#BD686D"
                
            else:
                piece.rect_color = piece.original_color
                
            pygame.draw.rect(surface, piece.rect_color, piece.rect, border_radius = 0)

    def clear_highlights(self):
        for piece in self.pieces:
            piece.highlighted = False

    def reposition(self):
        current_y = 140
        for piece in self.pieces:
            piece.rect.y = current_y
            current_y += piece.rect.height

    def deletion(self, index):
        self.pieces.pop(index)
        self.reposition()
    
    def duplication(self, index):
        to_duplicate = self.pieces[index]
        if (self.pieces[-1].rect.top + to_duplicate.rect.height) <= 645:
            copied_rect = to_duplicate.rect.copy()
            copied_colour = to_duplicate.original_color
            new_piece = ChromosomePiece(copied_rect, copied_colour)
            new_piece.id = to_duplicate.id
            self.pieces.insert(index + 1, new_piece)

        self.reposition()
    
    def inversion(self, start_index, end_index):
        start = min(start_index, end_index)
        end = max(start_index, end_index)
        self.pieces[start:end + 1] = self.pieces[start:end + 1][::-1]
        self.reposition()