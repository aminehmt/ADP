mot = input("Veuillez entrer une charne de caractères : ")

largeur_cadre = 30

espaces_totaux = largeur_cadre - len(mot)
espaces_gauche = espaces_totaux // 2
espaces_droite = espaces_totaux - espaces_gauche

print("*" * largeur_cadre) 
print("*" + " " * espaces_gauche + mot + " " * espaces_droite + "*")  # Ligne avec le mot
print("*" * largeur_cadre)  