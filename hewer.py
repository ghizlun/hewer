import pygame
import random

#test

FENETRE_LARGEUR = 800
FENETRE_HAUTEUR = 700

TURQUOISE           = (37, 253, 233)
MARRON              = (143, 89,  34)
JAUNE               = (252, 220, 18)
BLEU                = (38,  196, 236)

VIDE = 0
TERRE = 1
OR = 2
DIAMANT = 3

#---------- Fontions

def joueur():
    return {
        'position'  : [0, 0],
        'vitesse'   : [0, 0],
        'accel'     : [0, 0],
        'sprite'    : None,
        'animation' : None,
    }

def position(objet):
    return objet['position']

def scene_to_fenetre(pos):
    global scene
    ligne   = pos[0]
    colonne = pos[1]
    x = (FENETRE_LARGEUR / len(scene[0])) * colonne
    y = (FENETRE_HAUTEUR / len(scene)) * ligne
    return [x, y]

#_ Définition des blocs

def new_bloc():
    return {
        'type'      : VIDE,
        'resistance': 0,
        'couleur'   : None,
        'position'  : [0, 0],
    }

def type_bloc(objet, type):
    objet['type'] = type
    if objet['type'] == TERRE:
        objet['resistance'] = 1
        objet['couleur'] = MARRON
    if objet['type'] == OR:
        objet['resistance'] = 5
        objet['couleur'] = JAUNE
    if objet['type'] == DIAMANT:
        objet['resistance'] = 10
        objet['couleur'] = TURQUOISE


def place_bloc(objet, x, y):
    objet['position'][0] = x
    objet['position'][1] = y

def afficher_bloc(objet):
    pygame.draw.rect(fenetre, objet['couleur'], ((objet['position']), (dimension_bloc, dimension_bloc)))

def new_scene():
    global scene
    for ligne in range(len(scene)-2, len(scene)):
        for colonne in range(0, len(scene[ligne])):
            scene[ligne][colonne] = random.randint(0, 3)

def maj_scene():
    
    pass



def dessiner_scene():
    global scene

    bloc = new_bloc()
    for ligne in range(0, len(scene)):
        for colonne in range(0, len(scene[ligne])):
            if scene[ligne][colonne] != VIDE:
                pos = [ligne, colonne]
                type_bloc(bloc, scene[ligne][colonne])
                x = scene_to_fenetre(pos)[0]
                y = scene_to_fenetre(pos)[1]
                place_bloc(bloc, x, y)
                afficher_bloc(bloc)



#__Scène

random.seed()

scene =            [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]]
new_scene()

#---------- Paramamètres

dimension_bloc = FENETRE_LARGEUR // len(scene[0])

#---------- Boucle de jeu principale


pygame.init()

fenetre_taille = (FENETRE_LARGEUR, FENETRE_HAUTEUR)
fenetre = pygame.display.set_mode(fenetre_taille)
pygame.display.set_caption('Hewer')

running = True
temps = pygame.time.Clock()

while running:
    now = pygame.time.get_ticks()
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            running = False

    fenetre.fill(BLEU)
    dessiner_scene()
    pygame.display.flip()
    temps.tick(50)

pygame.display.quit()
pygame.quit()
exit()

