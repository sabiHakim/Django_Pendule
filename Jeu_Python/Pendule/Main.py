import os
from Facile import  Facile


class Main:
    def __init__(self):
        print("constructeur")

    def main(self):
        print("main func")


if __name__ == "__main__":

    tf = []
    chemin_fichier = './faciles.txt'
    # Vérifier le répertoire de travail courant
    # print(f"Répertoire de travail courant : {os.getcwd()}")
    # Vérifier les fichiers dans le répertoire courant
    # print(f"Fichiers dans le répertoire courant : {os.listdir('.')}")
    # Vérifier si le fichier existe
    if not os.path.exists(chemin_fichier):
        print(f"Le fichier {chemin_fichier} n'existe pas.")
    else:
        try:
            ff = Facile.process_file(chemin_fichier,tf)
        except FileNotFoundError:
            print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")
    for i in tf:
        print(i)