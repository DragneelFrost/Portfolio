from Guerrier import Guerrier
from Assassin import Assassin
from Rodeur import Rodeur
from Mage import Mage

class MyApplication:
    def __init__(self):
        print("Bonjour et bienvenue dans ce MMORPG, nous allons à présent créer votre personnage")
        self.main_menu()

    def main_menu(self):
        classe_perso = 0
        print("Entrez la valeur de la classe de personnage que vous voulez incarner :")
        print("1-Guerrier, 2-Assassin, 3-Rodeur, 4-Mage, 5-quit")

        classe_perso = int(input("Choix : "))

        if classe_perso == 1:
            self.warrior_adventure()
        elif classe_perso == 2:
            self.rogue_adventure()
        elif classe_perso == 3:
            self.hunter_adventure()
        elif classe_perso == 4:
            self.wizard_adventure()
        elif classe_perso == 5:
            self.quit()
        else:
            print("Choix invalide. Veuillez choisir un nombre entre 1 et 5.")

    def warrior_adventure(self):
        perso = Guerrier()
        perso.get_name()
        print("Classe :", perso.Classe)
        print("Vie :", perso.Vie)
        print("Armure :", perso.Armure)

        print("Arme 1 :", perso.Arme1)
        print("Dégâts de l'arme 1 :", perso.Dégats1)
        print("Vitesse de l'arme 1 :", perso.Vitesse1)

        print("Arme 2 :", perso.Arme2)
        print("Dégâts de l'arme 2 :", perso.Dégats2)
        print("Vitesse de l'arme 2 :", perso.Vitesse2)

        print("Bouclier :", perso.Bouclier)
        print("Magie :", perso.Magie)

        arme_choisie = int(input("Choisissez votre arme (1- épée longue ou 2- hache) : "))

        if arme_choisie == 1:
            arme = perso.Arme1
        elif arme_choisie == 2:
            arme = perso.Arme2
        else:
            print("Choix invalide. Vous utilisez maintenant l'arme par défaut.")
            arme = perso.Arme1

        print("Vous utilisez l'arme :", arme)

    def rogue_adventure(self):
        perso = Assassin()
        perso.get_name()
        print("Classe :", perso.Classe)
        print("Vie :", perso.Vie)
        print("Armure :", perso.Armure)

        print("Arme 1 :", perso.Arme1)
        print("Dégâts de l'arme 1 :", perso.Dégats1)
        print("Vitesse de l'arme 1 :", perso.Vitesse1)

        print("Arme 2 :", perso.Arme2)
        print("Dégâts de l'arme 2 :", perso.Dégats2)
        print("Vitesse de l'arme 2 :", perso.Vitesse2)

        print("Bouclier :", perso.Bouclier)
        print("Magie :", perso.Magie)

        arme_choisie = int(input("Choisissez votre arme (1- épée courte ou 2- double dague) : "))

        if arme_choisie == 1:
            arme = perso.Arme1
        elif arme_choisie == 2:
            arme = perso.Arme2
        else:
            print("Choix invalide. Vous utilisez maintenant l'arme par défaut.")
            arme = perso.Arme1

        print("Vous utilisez l'arme :", arme)

    def hunter_adventure(self):
        perso = Rodeur()
        perso.get_name()
        print("Classe :", perso.Classe)
        print("Vie :", perso.Vie)
        print("Armure :", perso.Armure)

        print("Arme 1 :", perso.Arme1)
        print("Dégâts de l'arme 1 :", perso.Dégats1)
        print("Vitesse de l'arme 1 :", perso.Vitesse1)

        print("Arme 2 :", perso.Arme2)
        print("Dégâts de l'arme 2 :", perso.Dégats2)
        print("Vitesse de l'arme 2 :", perso.Vitesse2)

        print("Bouclier :", perso.Bouclier)
        print("Magie :", perso.Magie)

        arme_choisie = int(input("Choisissez votre arme (1- Arc ou 2- Arbalette) : "))

        if arme_choisie == 1:
            arme = perso.Arme1
        elif arme_choisie == 2:
            arme = perso.Arme2
        else:
            print("Choix invalide. Vous utilisez maintenant l'arme par défaut.")
            arme = perso.Arme1

        print("Vous utilisez l'arme :", arme)

    def wizard_adventure(self):
        perso = Mage()
        perso.get_name()
        print("Classe :", perso.Classe)
        print("Vie :", perso.Vie)
        print("Armure :", perso.Armure)

        print("Arme 1 :", perso.Arme1)
        print("Dégâts de l'arme 1 :", perso.Dégats1)
        print("Vitesse de l'arme 1 :", perso.Vitesse1)

        print("Arme 2 :", perso.Arme2)
        print("Dégâts de l'arme 2 :", perso.Dégats2)
        print("Vitesse de l'arme 2 :", perso.Vitesse2)

        print("Bouclier :", perso.Bouclier)
        print("Magie :", perso.Magie)

        arme_choisie = int(input("Choisissez votre arme (1- Magie de l'éther ou 2- Magie Arcanique) : "))

        if arme_choisie == 1:
            arme = perso.Arme1
        elif arme_choisie == 2:
            arme = perso.Arme2
        else:
            print("Choix invalide. Vous utilisez maintenant l'arme par défaut.")
            arme = perso.Arme1

        print("Vous utilisez l'arme :", arme)

    def quit(self):
        print("Au revoir !")

if __name__ == "__main__":
    my_app = MyApplication()
