"""
Ce module contient des fonctions pour vérifier si un nombre est premier et 
pour afficher les nombres premiers de 1 à 100.

Fonctions:
- isprime(p): Vérifie si un nombre est premier.
- main(): Affiche les nombres premiers de 1 à 100.
"""

from math import sqrt

#### Fonction secondaire

def isprime(p):
    """
    Vérifie si un nombre est premier.

    Args:
        p (int): Le nombre à vérifier.

    Returns:
        bool: True si p est un nombre premier, False sinon.
    """
    if p in (0, 1):  # Vérifie si p est 0 ou 1
        return False
    for i in range(2, int(sqrt(p) + 1)):  # Vérifie la divisibilité jusqu'à la racine carrée de p
        if p % i == 0:
            return False
    return True


#### Fonction principale

def main():
    """
    Fonction principale pour afficher les nombres premiers de 1 à 100.
    Appelle la fonction isprime pour vérifier chaque nombre.
    """
    for n in range(100):  # Affiche les nombres premiers de 1 à 100
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
