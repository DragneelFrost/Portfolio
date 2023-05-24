class Mage:
    def __init__(self):
        self.Classe = "Mage"
        self.Vie = 12
        self.Armure = "Toge"
        self.Arme1 = "Magie de l'ether"
        self.Dégats1 = 16
        self.Vitesse1 = 1
        self.Arme2 = "Magie Arcanique"
        self.Dégats2 = 20
        self.Vitesse2 = 0.75
        self.Bouclier = False
        self.Magie = True
    
    def get_name(self):
        self.nom = input("Entrez le nom du Mage : ")