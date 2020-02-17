import pygame
from pygame.locals import *
from constantes import *
from classes import *
import random

'#initialisation'
pygame.init()

'#affichage'
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
pygame.display.set_caption(titre_fenetre)
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
pts = 0
pygame.key.set_repeat(400, 30)
continuer = 1
etat = 0
'#BOUCLE INFINIE'
while continuer:
    if etat == 0:
        pygame.time.Clock().tick(30)
        fond = pygame.image.load(image_acceuil).convert()
        fenetre.blit(fond, (0, 0))
        pygame.display.flip()
        continuer_accueil = 1
        continuer_jeu = 1
        while continuer_accueil:

            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == 13:
                        choix = 1
                        continuer_accueil = 0
    elif etat == 2:
        pygame.time.Clock().tick(30)
        fond = pygame.image.load(victoire).convert()
        fenetre.blit(fond, (0, 0))
        pygame.display.flip()
        continuer_accueil = 1
        continuer_jeu = 1
        while continuer_accueil:

            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    '#Lancement du niveau 1'
                    if event.key == 13:
                        choix = 1
                        continuer_accueil = 0
    elif etat == 3:
        pygame.time.Clock().tick(30)
        fond = pygame.image.load(defaite).convert()
        fenetre.blit(fond, (0, 0))
        pygame.display.flip()
        continuer_accueil = 1
        continuer_jeu = 1
        while continuer_accueil:

            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    '#Lancement du niveau 1'
                    if event.key == 13:
                        choix = 1
                        continuer_accueil = 0
    if choix == 1:
        fond = pygame.image.load(image_fond).convert()
        niveau = Niveau("n1")
        niveau.generer()
        niveau.afficher(fenetre)
        nombreAléatoire1 = random.randint(1, 108)
        etherposition = niveau.case(nombreAléatoire1)
        ether = Objet(ether, etherposition[0], etherposition[1])
        nombreAléatoire2 = random.randint(1, 108)
        seringueposition = niveau.case(nombreAléatoire2)
        seringue = Objet(seringue, seringueposition[0], seringueposition[1])
        nombreAléatoire3 = random.randint(1, 108)
        armeposition = niveau.case(nombreAléatoire3)
        arme = Objet(arme, armeposition[0], armeposition[1])
        mc = Perso(perso_arriere, perso_face, perso_gauche, perso_droite, niveau)

    while continuer_jeu:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == K_ESCAPE:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    mc.deplacement('bas')
                if event.key == K_UP:
                    mc.deplacement('haut')
                if event.key == K_RIGHT:
                    mc.deplacement('droite')
                if event.key == K_LEFT:
                    mc.deplacement('gauche')
        if (mc.x, mc.y) == (ether.x, ether.y):
            ether = Objet("ressource\ether.png", 0, 270)
            pts = pts + 1

        if (mc.x, mc.y) == (seringue.x, seringue.y):
            seringue = Objet("ressource\seringue.png", 0, 300)
            pts = pts + 1

        if (mc.x, mc.y) == (arme.x, arme.y):
            arme = Objet("ressource/arme.png", 0, 330)
            pts = pts + 1

        if (mc.x, mc.y) == (420, 420):
            if pts == 3:
                continuer_jeu = 0
                etat = 2
            else:
                continuer_jeu = 0
                etat = 3

        fenetre.blit(fond, (0, 0))
        niveau.afficher(fenetre)
        fenetre.blit(mc.direction, (mc.x, mc.y))
        fenetre.blit(ether.direction, (ether.x, ether.y))
        fenetre.blit(seringue.direction, (seringue.x, seringue.y))
        fenetre.blit(arme.direction, (arme.x, arme.y))
        pygame.display.flip()
