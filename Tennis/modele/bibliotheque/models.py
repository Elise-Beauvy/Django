from django.db import models


"""class Pays(models.Model):
    Pays = models.CharField(max_length=100)

    def __str__(self):
        return self.Pays
"""

# Create your models here.
class JoueurModel(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    Nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    Prenom = models.CharField(max_length = 100)
    Naissance = models.DateField(blank=True, null = True) # champs de type date, pouvant être null ou ne pas être rempli
    Nationalite = models.CharField(max_length =100)
    date_debut_circuit= models.CharField(max_length=4) # champs de type entier devant être obligatoirement rempli

    def __str__(self):
        chaine = f"{self.Prenom} {self.Nom} est un joueur de tennis né en {self.Nationalite}. Il est arrivé sur le circuit professionnel en {self.date_debut_circuit}."
        return chaine

    def dico(self):
        return {"Nom" : self.Nom, "Prenom" : self.Prenom, "Naissance" : self.Naissance, "Nationalite" : self.Nationalite, "date des débuts sur le circuit" : self.date_debut_circuit }


