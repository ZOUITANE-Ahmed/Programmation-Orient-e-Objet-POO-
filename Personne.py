# Définir une classe simple
class Personne:
    def __init__(self, nom, age):
        self.nom = nom  # Attribut nom
        self.age = age  # Attribut age
    
    def se_presenter(self):  # Méthode pour présenter la personne
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")

# Créer un objet de la classe Personne
personne1 = Personne("Alice", 30)

# Appeler une méthode sur cet objet
personne1.se_presenter()
