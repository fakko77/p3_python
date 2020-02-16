import pygame
from pygame.locals import *
from constantes import *
from classes import *


#initialisation
pygame.init()

#affichage 
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
pygame.display.set_caption(titre_fenetre)
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)


#ecran d'acceuil
fond = pygame.image.load(image_acceuil).convert()
fenetre.blit(fond, (0,0))
mur = pygame.image.load(image_mur).convert_alpha()
position_mur = mur.get_rect()
fenetre.blit(mur, position_mur)
mc = Perso("perso_arriere","perso_face","perso_gauche","perso_droite")
pygame.display.flip()

#perso creation
#perso = pygame.image.load(image_acceuil).convert_alpha()
#position_perso = perso.get_rect()
#fenetre.blit(perso, position_perso)


pygame.key.set_repeat(400, 30)
continuer = 1
#BOUCLE INFINIE
while continuer:

        
        for event in pygame.event.get():
                if event.type == K_ESCAPE:
                        continuer = 0
                if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                                mc.deplacement('bas')
                                #position_perso = position_perso.move(0,3)
                                #perso = pygame.image.load(perso_face).convert_alpha()
                        if event.key == K_UP:
                                mc.deplacement('haut')
                                
                                #position_perso = position_perso.move(0,-3)
                                #perso = pygame.image.load(perso_arriere).convert_alpha()
                                
                        if event.key == K_RIGHT:
                                mc.deplacement('droite')
                                #position_perso = position_perso.move(3,0)
                                #perso = pygame.image.load(perso_droite).convert_alpha()
                        if event.key == K_LEFT:
                                mc.deplacement('gauche')
                                #position_perso = position_perso.move(-3,0)
                                #perso = pygame.image.load(perso_gauche).convert_alpha()
                        fond = pygame.image.load(image_fond).convert()
                       
                        
                                
                                
                        
                        
                                 



#Re-collage
        fenetre.blit(fond, (0,0))
        fenetre.blit(mc.direction, (mc.x , mc.y))
        fenetre.blit(mur, position_mur )
        #Rafraichissement
        
        pygame.display.flip()

        
        


