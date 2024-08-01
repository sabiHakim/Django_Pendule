from django.db import models
# Create your models here.
class Facile:
    @staticmethod
    def process_file(file, lf):
        with open(file, 'r', encoding='utf-8') as fichier:
            for ligne in fichier:
                # print(ligne.strip("\n"))
                lf.append(ligne.strip())
        return lf

class Difficile:
    @staticmethod
    def process_file(file, lf):
        with open(file, 'r', encoding='utf-8') as fichier:
            for ligne in fichier:
                lf.append(ligne.strip())
        return lf