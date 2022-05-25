import pygame
from item import Item
from ecrire_log import ecrire_log

class Centrale_charbon:

    def __init__(self):
        self.image = pygame.image.load('image/charbon.jpg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.pose = False
        self.vitesse = 5
        self.produire_ou = "joueur"

    def MouvementDroite(self):
        if self.rect.x <= 1030:
            self.rect.x += self.vitesse

    def MouvementGauche(self):
        if self.rect.x >= 0:
            self.rect.x -= self.vitesse

    def MouvementHaut(self):
        if self.rect.y >= 0:
            self.rect.y -= self.vitesse

    def MouvementBas(self):
        if self.rect.y <=  650:
            self.rect.y += self.vitesse

    def produire(self, joueur, boite):
        ecrire_log.ecrire_log(self=ecrire_log, texte=" info : centrale charbon produit")
        if self.produire_ou == "joueur":
            if joueur.verifie_puis_enleve("charbon......40"):
                joueur.ajoute_inventer("électricité......10", 40)
        elif self.produire_ou == "boite":
            if boite.verifi_apartenance("charbon......40"):
                boite.items.append(Item(0, "électricité......10", 30, 10))
                boite.enlever("charbon......40")
        elif self.produire_ou == "vendre":
            if boite.verifi_apartenance("charbon......40"):
                boite.enlever("charbon......40")
                joueur.argent += 20
