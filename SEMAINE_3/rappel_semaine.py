"""
Bienvenue encore une fois dans notre Bootcamps
    
    """
    
# exercices 1 : manipulation  des dictionnaires soit la liste des dictionnaires ci-dessus

# trouvons le nombre de personnes ressortissants d'une ville donnée

liste_personnes = [ {"nom": "Alice", "age": 30,"ville":"Paris"},
                   {"nom": "Bob", "age": 35.5,"ville":"Lyon"},
                   {"nom": "Charlie", "age": 25,"ville":"Paris"},
                   {"nom": "Djamel", "age": 27,"ville":"Marseille"},
                   {"nom": "Elise", "age": 25,"ville":"Paris"},
                   {"nom": "Fatou", "age": 35,"ville":"Lyon"},
                   {"nom": "Gaston", "age": 28,"ville":"Marseille"},
                   {"nom": "Hector", "age": 32,"ville":"Paris"},
                   {"nom": "Isabelle", "age": 40,"ville":"Lyon"},
                   {"nom": "Jules", "age": 25,"ville":"Marseille"},
                     {"nom": "Karine", "age": 22,"ville":"Paris"},
                     {"nom": "Loic", "age": 35,"ville":"Lyon"},
                     {"nom": "Marie", "age": 26,"ville":"Marseille"},
                     {"nom": "Nadia", "age": 29,"ville":"Paris"},
                     {"nom": "Olivier", "age": 33,"ville":"Lyon"},
                     {"nom": "Philippe", "age": 45,"ville":"Marseille"},
                     {"nom": "Quentin", "age": 27,"ville":"Paris"},
                     {"nom": "Raissa", "age": 28,"ville":"Lyon"},
                     {"nom": "Sylvie", "age": 30,"ville":"Marseille"},
                     {"nom": "Tanguy", "age": 31,"ville":"Paris"},
                     {"nom": "Ursule", "age": 36,"ville":"Lyon"},
                     {"nom": "Victor", "age": 24,"ville":"Marseille"},
                     {"nom": "Willy", "age": 26,"ville":"Paris"},
                     {"nom": "Xavier", "age": 35,"ville":"Lyon"},
                     {"nom": "Yann", "age": 27,"ville":"Marseille"},
                     {"nom": "Zoé", "age": 29,"ville":"Paris"},
                        {"nom": "Amine", "age": 33,"ville":"Lyon"},
                        {"nom": "Babacar", "age": 40,"ville":"Marseille"},
                        {"nom": "Cyril", "age": 28,"ville":"Paris"},
                        {"nom": "Djeneba", "age": 31,"ville":"Lyon"},
                        {"nom": "Eliane", "age": 25,"ville":"Marseille"},
                        {"nom": "Firmin", "age": 26,"ville":"Paris"},
                        {"nom": "Gael", "age": 35,"ville":"Lyon"},
                        {"nom": "Hassan", "age": 27,"ville":"Marseille"},
                        {"nom": "Ines", "age": 29,"ville":"Paris"},
                        {"nom": "Jean", "age": 33,"ville":"Lyon"},
                        {"nom": "Kadiatou", "age": 40,"ville":"Marseille"},
                        {"nom": "Lamine", "age": 28,"ville":"Paris"},
                        {"nom": "Mamadou", "age": 31,"ville":"Lyon"},
                        {"nom": "Nathalie", "age": 25,"ville":"Marseille"},
                        {"nom": "Ousmane", "age": 26,"ville":"Paris"},
                        {"nom": "Pierre", "age": 35,"ville":"Lyon"},
                        {"nom": "Quitterie", "age": 27,"ville":"Marseille"},
                        {"nom": "Romain", "age": 29,"ville":"Paris"},
                        {"nom": "Sylvain", "age": 33,"ville":"Lyon"},
                        {"nom": "Tatiana", "age": 40,"ville":"Marseille"},
                        {"nom": "Ugo", "age": 28,"ville":"Paris"},
                        {"nom": "Violette", "age": 31,"ville":"Lyon"},
                        {"nom": "Wassila", "age": 25,"ville":"Marseille"},
                        {"nom": "Xavier", "age": 26,"ville":"Paris"},
                        {"nom": "Yannick", "age": 35,"ville":"Lyon"},
                        {"nom": "Zoé", "age": 27,"ville":"Marseille"},
                        {"nom": "Amine", "age": 29,"ville":"Paris"},
                        {"nom": "Babacar", "age": 33,"ville":"Lyon"},
                        {"nom": "Cyril", "age": 40,"ville":"Marseille"},
                        {"nom": "Djeneba", "age": 28,"ville":"Paris"},
                        {"nom": "Eliane", "age": 31,"ville":"Lyon"},
                        {"nom": "Firmin", "age": 25,"ville":"Marseille"},
                        {"nom": "Gael", "age": 26,"ville":"Paris"},
                        {"nom": "Hassan", "age": 35,"ville":"Lyon"},
                        {"nom": "Ines", "age": 27,"ville":"Marseille"},
                        {"nom": "Jean", "age": 29,"ville":"Paris"},
                        {"nom": "Kadiatou", "age": 33,"ville":"Lyon"},
                        {"nom": "Lamine", "age": 40,"ville":"Marseille"},
                        {"nom": "Mamadou", "age": 28,"ville":"Paris"},
                        {"nom": "Nathalie", "age": 31,"ville":"Lyon"},
                        {"nom": "Ousmane", "age": 25,"ville":"Marseille"},
                        {"nom": "Pierre", "age": 26,"ville":"Paris"},
                        {"nom": "Quitterie", "age": 35,"ville":"Lyon"},
                        {"nom": "Romain", "age": 27,"ville":"Marseille"},
                        {"nom": "Sylvain", "age": 29,"ville":"Paris"},
                        {"nom": "Tatiana", "age": 33,"ville":"Lyon"},
                        {"nom": "Ugo", "age": 40,"ville":"Marseille"},
                        {"nom": "Violette", "age": 28,"ville":"Paris"},
                        {"nom": "Wassila", "age": 31,"ville":"Lyon"},
                        {"nom": "Xavier", "age": 25,"ville":"Marseille"},
                        {"nom": "Yannick", "age": 26,"ville":"Paris"},
                        {"nom": "Zoé", "age": 35,"ville":"Lyon"},
                        {"nom": "Amine", "age": 27,"ville":"Marseille"},
                        {"nom": "Babacar", "age": 29,"ville":"Paris"},
                        {"nom": "Cyril", "age": 33,"ville":"Lyon"},
                        {"nom": "Djeneba", "age": 40,"ville":"Marseille"},
                        {"nom": "Eliane", "age": 28,"ville":"Paris"},
                        {"nom": "Firmin", "age": 31,"ville":"Lyon"},
                        {"nom": "Gael", "age": 25,"ville":"Marseille"},
                        {"nom": "Hassan", "age": 26,"ville":"Paris"},
                        {"nom": "Ines", "age": 35,"ville":"Lyon"},
                        {"nom": "Jean", "age": 27,"ville":"Marseille"},
                        {"nom": "Kadiatou", "age": 29,"ville":"Paris"},
                        {"nom": "Lamine", "age": 33,"ville":"Lyon"},
                        {"nom": "Mamadou", "age": 40,"ville":"Marseille"},
                        {"nom": "Nathalie", "age": 28,"ville":"Paris"},
                        {"nom": "Ousmane", "age": 31,"ville":"Lyon"},
                        {"nom": "Pierre", "age": 25,"ville":"Marseille"},
                        {"nom": "Quitterie", "age": 26,"ville":"Paris"},
                        {"nom": "Romain", "age": 35,"ville":"Lyon"},
                        {"nom": "Sylvain", "age": 27,"ville":"Marseille"},
                        {"nom": "Tatiana", "age": 29,"ville":"Paris"},
                        {"nom": "Ugo", "age": 33,"ville":"Lyon"},
                        {"nom": "Violette", "age": 40,"ville":"Marseille"},
                        {"nom": "Wassila", "age": 28,"ville":"Paris"},
                        {"nom": "Xavier", "age": 31,"ville":"Lyon"},
                        {"nom": "Yannick", "age": 25,"ville":"Marseille"},
                        {"nom": "Zoé", "age": 26,"ville":"Paris"},
                        {"nom": "Amine", "age": 35,"ville":"Lyon"},
                        {"nom": "Babacar", "age": 27,"ville":"Marseille"},
                        {"nom": "Cyril", "age": 29,"ville":"Paris"},
                        {"nom": "Djeneba", "age": 33,"ville":"Lyon"},
                        {"nom": "Eliane", "age": 40,"ville":"Marseille"},
                        {"nom": "Firmin", "age": 28,"ville":"Paris"},
                        {"nom": "Gael", "age": 31,"ville":"Lyon"},
                        {"nom": "Hassan", "age": 25,"ville":"Marseille"},
                        {"nom": "Ines", "age": 26,"ville":"Paris"},
                        {"nom": "Jean", "age": 35,"ville":"Lyon"},
                        {"nom": "Kadiatou", "age": 27,"ville":"Marseille"},
                        {"nom": "Lamine", "age": 29,"ville":"Paris"},
                        {"nom": "Mamadou", "age": 33,"ville":"Lyon"},
                        {"nom": "Nathalie", "age": 40,"ville":"Marseille"},
                        {"nom": "Ousmane", "age": 28,"ville":"Paris"},
                        {"nom": "Pierre", "age": 31,"ville":"Lyon"},
                        {"nom": "Quitterie", "age": 25,"ville":"Marseille"},
                        {"nom": "Romain", "age": 26,"ville":"Paris"},
                        {"nom": "Sylvain", "age": 35,"ville":"Lyon"},
                        {"nom": "Tatiana", "age": 27,"ville":"Marseille"},
                        {"nom": "Ugo", "age": 29,"ville":"Paris"},
                        {"nom": "Violette", "age": 33,"ville":"Lyon"},
                        {"nom": "Wassila", "age": 40,"ville":"Marseille"},
                        {"nom": "Xavier", "age": 28,"ville":"Paris"},
                        {"nom": "Yannick", "age": 31,"ville":"Lyon"},
                        {"nom": "Zoé", "age": 25,"ville":"Marseille"}  
                   ]
print("Bienvenue dans notre Bootcamps")
print("Nous avons",len(liste_personnes),"participants")

#nous allons chercher à savoir le nombre de participants par ville
def nombre_personnes_ville(ville,liste_personnes):
    nombre = 0
    for personne in liste_personnes:
    #for i in range(len(liste_personnes)):
    #   if liste_personnes[i]['ville']
        if personne["ville"] == ville:
            nombre += 1       
    return nombre
liste_personnes.append({"nom":"fatima","age":34,"ville":"Bamako"})

print("Nous avons",nombre_personnes_ville("Bamako",liste_personnes),"participants de Paris")

print("Nous avons",len(liste_personnes),"participants")



def ajouter_personne(liste_personnes,nom, age, ville):
    liste_personnes.append({"nom": nom, "age": age, "ville": ville})
    return liste_personnes,nom, age, ville
#SOUhaitons la bienvenue à Awa qui vient de Dakar   disons le nombre de participants
nouveaux_participants = ajouter_personne(liste_personnes,"Awa", 23, "Dakar")
print("Nous avons",len(nouveaux_participants[0]),f"participants\n Bienvenue {nouveaux_participants[1]} à qui vient de Dakar")

# changer les infos d'une personne à partir de son ancien nom
def modifier_personne(liste_personnes, ancien_nom, nouveau_nom, nouvel_age, nouvelle_ville):
    """
    Modifie les informations d'une personne dans une liste de personnes.

    Args:
        liste_personnes (list): La liste de personnes.
        ancien_nom (str): Le nom de la personne à modifier.
        nouveau_nom (str): Le nouveau nom de la personne.
        nouvel_age (int): Le nouvel âge de la personne.
        nouvelle_ville (str): La nouvelle ville de la personne......

    Returns:
        list: La liste de personnes mise à jour avec les modifications effectuées.
        None: Si la personne à modifier n'a pas été trouvée dans la liste.
    """
    
    for personne in liste_personnes:
        """" 
        cette façon de faire est plus simple,  car nous accedons directement à  chaque dictionnaire
        qui nous permet de considerer la variable de la boucle comme un dictionnaire
        
        """
        if personne['nom'] == ancien_nom:
            personne['nom'] = nouveau_nom
            personne['age'] = nouvel_age
            personne['ville'] = nouvelle_ville
            return liste_personnes
    return None
#chercher la personne dont le nom est "Amine" et changer son nom en "Aminata"   

liste_personnes = modifier_personne(liste_personnes, "Amine", "Aminata", 35, "Paris")
print("Nous avons",len(liste_personnes),"participants")
for personne in liste_personnes:
    if personne['nom'] == "Aminata":
        print(f"{personne['nom']} a {personne['age']} ans et habite à {personne['ville']}")

                                                                        
                                                                        
                                                

