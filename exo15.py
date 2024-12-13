chaine = input("Veeuillez saisir  une chaîne : ")

voyelles = ['a', 'e', 'o']

for voyelle in voyelles:
    if voyelle in chaine:
        print(f"La voyelle '{voyelle}' est présente dans la chaîne.")
    else:
        print(f"La voyelle '{voyelle}' n'est pas présente dans la chaîne.")