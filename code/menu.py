#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # -1 for play endless

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Mountain', COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], (255, 255, 255), ((WIN_WIDTH / 2), 180 + (i * 20)))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # Adicionado para encerrar o loop corretamente ao sair

    def menu_text(self, text_size: int, text: str, tex_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name='lucida Sans Typewriter', size=text_size)
        # Correção aplicada abaixo: removendo os keyword arguments
        text_surf: Surface = text_font.render(text, True, tex_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(text_surf, text_rect)

