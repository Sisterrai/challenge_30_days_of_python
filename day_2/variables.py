#Jour2: 30 Days of Python Programming
# Exercice 1
prenom = "Raïnatou"
nom_de_famille = "BAWAH"
nom_complet = "Raïnatou BAWAH"
pays = "Bénin"
annee = 2025
est_marrie = False
is_true = True
is_light_on = True
autre_nom , age , pays = "Chrisbella", 12 , "Togo"

# Exercice 2
print(type(prenom))
print(type(nom_de_famille))
print(type(nom_complet))
print(type(pays))
print(type(annee))
print(type(est_marrie))
print(type(is_true))
print(type(is_light_on))
print(type(autre_nom))
print(type(age))
print(type(pays))

print('la longueur de', prenom ,'est:',len(prenom))
print('la longueur de', nom_de_famille ,'est:',len(nom_de_famille))
#len(prenom) > len(nom_de_famille)

num_one = 5
num_two = 4
variable_total = num_one + num_two
print("la somme de ",num_one," et ", num_two, " = " ,variable_total)
variable_diff = num_two -num_one
print("la différence de ",num_one," et ", num_two, " = " ,variable_diff)
variable_product = num_one * num_two
print("la multiplication de ",num_one," et ", num_two, " = " ,variable_product)
variable_division = num_one / num_two
print("la division de ",num_one," et ", num_two, " = " ,variable_division)
variable_remainder = num_one % num_two
print("la reste de la division de ",num_one," et ", num_two, " = " ,variable_remainder)
variable_exp = num_one ** num_two
print("la puissance de ",num_one," et ", num_two, " = " ,variable_exp)
variable_floor_div = num_one // num_two
print("la division au sol ",num_one," et ", num_two, " = " ,variable_floor_div)

rayon_du_cercle = 30
aire_du_cercle = 3.14*rayon_du_cercle*rayon_du_cercle
print("l'aire du cercle est :",aire_du_cercle)

rayon = int(input("Entrez le rayon de votre cercle : "))
perimetre = (rayon *2) * 3.14
print("le périmètre de votre cercle est : ", perimetre)


votre_prenom = input("Entrez votre prénom : ")
print("Votre prénom est : ", votre_prenom)
votre_nom = input("Entrez votre nom de famille: ")
print("Votre nom de famille est : ", votre_nom)
votre_age = int(input("Entrez votre âge : "))
print("Votre age est : ", votre_age)