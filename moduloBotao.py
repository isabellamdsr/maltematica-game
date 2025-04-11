import pygame

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.pos = pygame.Vector2(pos)
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))
        self.text_rect = self.text.get_rect(center=(self.pos.x, self.pos.y))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, pos):
        if (self.rect.left <= pos[0] < self.rect.right and
            self.rect.top <= pos[1] < self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            print("teste print botão")
            return True
        return False
                                                                                 
    def changeColor(self, pos):
        if (self.rect.left <= pos[0] < self.rect.right and
            self.rect.top <= pos[1] < self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)