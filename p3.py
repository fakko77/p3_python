import pygame
from pygame.locals import *
from constantes import *
from classes import *
import random

'#initialization'
pygame.init()

'#display'
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
pygame.display.set_caption(titre_fenetre)
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
'#initialization variables'
pts = 0
continuer = 1
state = 0
pygame.key.set_repeat(400, 30)
'#BOUCLE INFINIE'
while continuer:

    if state == 0:
        pygame.time.Clock().tick(30)
        '#picture of menu'
        background = pygame.image.load(image_acceuil).convert()
        fenetre.blit(background, (0, 0))
        pygame.display.flip()
        continue_home = 1
        ccontinue_game = 1
        while continue_home:

            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == 13:
                        choose = 1
                        continue_home = 0

    elif state == 2:
        pygame.time.Clock().tick(30)
        background = pygame.image.load(victoire).convert()
        fenetre.blit(background, (0, 0))
        pygame.display.flip()
        continue_home = 1
        ccontinue_game = 1
        while continue_home:

            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    '#Lancement du Level 1'
                    if event.key == 13:
                        choose = 1
                        continue_home = 0

    elif state == 3:
        pygame.time.Clock().tick(30)
        background = pygame.image.load(defaite).convert()
        fenetre.blit(background, (0, 0))
        pygame.display.flip()
        continue_home = 1
        ccontinue_game = 1
        while continue_home:

            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    '#run level 1'
                    if event.key == 13:
                        choose = 1
                        continue_home = 0
    if choose == 1:
        background = pygame.image.load(image_fond).convert()
        Level_ingame = Level("n1")
        Level_ingame.generer()
        Level_ingame.display(fenetre)
        '#creation and random placement of object '
        nombreAléatoire1 = random.randint(1, 108)
        etherposition = Level_ingame.random(nombreAléatoire1)
        ether = Objet(etherObj, etherposition[0], etherposition[1])
        nombreAléatoire2 = random.randint(1, 108)
        syringeposition = Level_ingame.random(nombreAléatoire2)
        syringe = Objet(seringueObj, syringeposition[0], syringeposition[1])
        nombreAléatoire3 = random.randint(1, 108)
        weaponposition = Level_ingame.random(nombreAléatoire3)
        weapon = Objet(armeObj, weaponposition[0], weaponposition[1])
        mc = character(perso_down, perso_front, perso_left, perso_right, Level_ingame)

    while ccontinue_game:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == K_ESCAPE:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    mc.move('down')
                if event.key == K_UP:
                    mc.move('up')
                if event.key == K_RIGHT:
                    mc.move('right')
                if event.key == K_LEFT:
                    mc.move('left')
        if (mc.x, mc.y) == (ether.x, ether.y):
            ether = Objet(etherObj, 0, 270)
            pts = pts + 1

        if (mc.x, mc.y) == (syringe.x, syringe.y):
            syringe = Objet(seringueObj, 0, 300)
            pts = pts + 1

        if (mc.x, mc.y) == (weapon.x, weapon.y):
            weapon = Objet(armeObj, 0, 330)
            pts = pts + 1

        if (mc.x, mc.y) == (420, 420):
            if pts == 3:
                ccontinue_game = 0
                pts = 0
                state = 2
            else:
                ccontinue_game = 0
                pts = 0
                state = 3

        fenetre.blit(background, (0, 0))
        Level_ingame.display(fenetre)
        fenetre.blit(mc.direction, (mc.x, mc.y))
        fenetre.blit(ether.direction, (ether.x, ether.y))
        fenetre.blit(syringe.direction, (syringe.x, syringe.y))
        fenetre.blit(weapon.direction, (weapon.x, weapon.y))
        pygame.display.flip()
