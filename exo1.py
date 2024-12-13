nom=input("Veuillez saisir votre nom:")
if nom=="VIP":
    print("Profitez du spectacle gratuitement !")
else:
    nbr=int(input("Combien de billets veuillez acheter ?"))
    prix=15.5
    tot=nbr*prix
    print(f"Le cout totale:{tot}")