pers = int(input("Combien de personnes ont besoin d'un taxi ? "))
ten = int(input("Combien de personnes peuvent tenir dans un taxi ? "))
if ten <= 0:
    print("Le nombre de personnes par taxi doit être supérieur à 0")


else:
    taxi = pers // ten
    reste=pers%ten
if reste==0:
    print(f"Nombre de taxis nécessaires : {taxi}")
else:
        print(f"Nombre de taxis nécessaires : {taxi+1}")
