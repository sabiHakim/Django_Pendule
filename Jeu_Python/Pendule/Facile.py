class Facile:
    @staticmethod
    def process_file(file, lf):
        with open(file, 'r', encoding='utf-8') as fichier:
            for ligne in fichier:
                # print(ligne.strip("\n"))
                lf.append(ligne.strip())
        return lf