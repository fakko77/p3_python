import pygame
from pygame.locals import *
from constantes import *


class Level:
    """Class to create a level"""

    def __init__(self, file_lvl):
        self.file_lvl = file_lvl
        self.structure = 0

    def generer(self):
        """Method for generating the level according to the file.
        A general list is created, containing a list per line to be displayed"""
        
        with open(self.file_lvl, "r") as file_lvl:
            structure_niveau = []
            
            for ligne in file_lvl:
                ligne_niveau = []

                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
         
                structure_niveau.append(ligne_niveau)
         
            self.structure = structure_niveau

    def display(self, fenetre):
        """Method for displaying the level according to
        of the structure list returned by generer()"""
        mur = pygame.image.load(image_mur).convert()
        depart = pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()

        num_ligne = 0
        for ligne in self.structure:
            '# On parcourt les listes de lignes'
            num_case = 0
            for sprite in ligne:
                '# On calcule la position réelle en pixels'
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':  # m = Mur
                    fenetre.blit(mur, (x, y))
                elif sprite == 'd':  # d = Départ
                    fenetre.blit(depart, (x, y))
                elif sprite == 'a':  # a = Arrivée
                    fenetre.blit(arrivee, (x, y))
                num_case += 1
            num_ligne += 1

    def random(self, num):
        """allows you to retrieve available x y values """
        num_ligne = 0
        cpt = 0
        for ligne in self.structure:

            num_case = 0
            for sprite in ligne:

                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == '0':
                    cpt += 1
                    if cpt == num:
                        return (x, y)
                num_case += 1
            num_ligne += 1


class character:
    """Class to create a character"""

    def __init__(self, up, down, left, right, niveau):

        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.right = pygame.image.load(right).convert_alpha()
        self.niveau = niveau
        '# Position du personnage en cases et en pixels'
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.direction = self.right

    def move(self, direction):
        """Class allowing to move the character """

        if direction == 'right':
            if self.case_x < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y][self.case_x + 1] != 'm':
                    self.case_x += 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.right

        '# Déplacement vers la left'
        if direction == 'left':
            if self.case_x > (0):
                if self.niveau.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.left

        '# Déplacement vers le up'
        if direction == 'up':
            if self.case_y > (0):
                if self.niveau.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.up

        '# Déplacement vers le down'
        if direction == 'down':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.down


class Objet:
    """Class to create a character"""

    def __init__(self, objet, x, y):
        '# Sprites du personnage'
        self.objet = pygame.image.load(objet).convert_alpha()
        '# Position du personnage en cases et en pixels'
        self.x = x
        self.y = y
        self.direction = self.objet
