# Jour 6-7 : Les listes et les tuples

## Structures de données
### C'est quoi les structures de données ?
Les structures de données sont des outils essentiels qui nous permettent d'organiser, de stocker et de gérer des informations de manière efficace. Elles permettent de manipuler et d'accéder aux données de façon structurée et cohérente.

### Les fonctionnalités des structures de données
- **Organisation et stockage de données :** Elles permettent de stocker des données de différents types, par exemple des nombres, des chaînes de caractères, des booléens, etc.
- **Accès et manipulation des données :** Chaque type de structure de données offre des méthodes spécifiques pour accéder aux éléments qu'elle contient. Ces méthodes permettent d'ajouter, de supprimer, de modifier et de rechercher des éléments dans la structure de données.
- **Autres fonctionnalités :** Gestion de la mémoire, optimisation des performances, etc.

## Types de structures de données

### 1. Les listes - Collections flexibles
Les listes sont des collections qui permettent de stocker une multitude de valeurs, peu importe leur type (int, string, bool, ...). Les listes sont spéciales grâce à leur flexibilité :

- **Mutables :** Les listes permettent de modifier leur contenu après leur création. Ajouter, supprimer ou remplacer des éléments sont les qualités des listes.
- **Hétérogènes :** Une liste peut contenir des éléments de types différents.
- **Accès ordonné :** Les éléments d'une liste sont conservés dans l'ordre d'insertion, ce qui facilite leur accès par position.

#### Illustration
```python
# Création d'une liste à 3 éléments
fruits = ["banane", "pomme", "orange"]

# Accès à un élément par son index
premier_fruit = fruits[0]  # premier élément dans la variable fruits est "banane"

# Modification d'un élément
fruits[1] = "poire"  # La pomme est remplacée par une poire

# Ajout d'un élément
fruits.append("épices")  # "épices" est ajouté à la fin de la liste

# Suppression d'un élément
fruits.remove("orange")  # "orange" est supprimé de la liste

# Longueur de la liste
nombre_fruits = len(fruits)  # la longueur est le nombre des éléments dans les fruits
```

### Création d'une liste
Pour créer une liste vide, il suffit de créer une variable et de l'initialiser avec des crochets `[]`. Pour initialiser une liste avec des éléments, on entre les éléments directement entre les crochets, séparés par des virgules. Par exemple, pour créer une liste de noms :

```python
# Création d'une liste vide
ma_liste = []

# Création d'une liste avec des valeurs initiales
personnes = ["Faustin", "Joseph", Bienvenue", "David"]

# Autres exemples de création de listes
nombres = [1, 2, 3, 4, 5]
melange = ["pomme", 10, True]

print(personnes, melange, nombres)
# ['Faustin', 'Joseph', 'Bienvenue', 'David'] ['pomme', 10, True] [1, 2, 3, 4, 5]
```

### Accès aux éléments d'une liste
Pour accéder ou récupérer un élément spécifique d'une liste, on utilise son index entre crochets `[]`. L'indexation commence à 0.

```python
# Accéder au premier élément de la liste personnes
premier_personne = personnes[0]  # premier_personne = "Faustin"

# Accéder au dernier élément de la liste personnes
dernier_personne = personnes[-1]  # dernier_personne = "David"

# Accéder à un élément par son index négatif
avant_dernier_personne = personnes[-2]  # avant_dernier_personne = "Bienvenue"
print(avant_dernier_personne)  # Bienvenue
```

### Opération et manipulation
Modifier le contenu d'une liste

```python
personnes[1] = "Bienfait"  # Remplace "Joseph" par "Bienfait" à l'index 1 de la liste personnes
personnes.append("Gabriel")  # Ajoute "Gabriel" à la fin de la liste personnes
personnes.remove("David")  # Supprime "David" de la liste personnes
personnes.pop(2)  # Supprime l'élément à l'index 2 (le troisième élément qui est Bienvenue)
personnes.insert(1, "Janvier")  # Insère "Janvier" avant "Bienfait" (index 1)
personnes.reverse()  # Renverser les éléments de la liste
print(personnes)  # ['Gabriel', 'Bienfait', 'Janvier', 'Faustin']
```

### Parcourir une liste
Pour parcourir chaque élément d'une liste et effectuer des actions sur eux, on utilise une boucle `for` :

```python
numero = 1
for personne in personnes:
    print(f"Personne N°{numero}", personne)  # Affiche chaque personne de la liste
    numero += 1
# Personne N°1 Gabriel
# Personne N°2 Bienfait
# Personne N°3 Janvier
# Personne N°4 Faustin
```

### Quelques fonctions intégrées pour manipuler les listes
- `len(liste)`: Renvoie la longueur de la liste.
- `min(liste)`: Trouve le plus petit élément de la liste.
- `max(liste)`: Trouve le plus grand élément de la liste.
- `sum(liste)`: Calcule la somme des éléments de la liste (uniquement pour les nombres).
- `sorted(liste)`: Trie la liste en ordre croissant.
- `reversed(liste)`: Inverse l'ordre des éléments de la liste.
- `liste.count(x)`: Compte combien de fois x est dans la liste.
- `liste.sort()`: Trie les éléments de la liste.
- `liste.index(x)`: Trouve l'index de l'élément.

### Utilisations de la liste comme pile
Les méthodes `append()` et `pop()` permettent d'utiliser très facilement une liste comme une pile (LIFO : Last In, First Out).

```python
nombres_premiers = [1, 3, 5, 7]

# Ajouter des éléments à la fin de la liste
nombres_premiers.append(11)
print(nombres_premiers)  # [1, 3, 5, 7, 11]
nombres_premiers.append(13)
print(nombres_premiers)  # [1, 3, 5, 7, 11, 13]

# Supprimer les derniers éléments de la liste
nombres_premiers.pop()
print(nombres_premiers)  # [1, 3, 5, 7, 11]
nombres_premiers.pop()
print(nombres_premiers)  # [1, 3, 5, 7]
nombres_premiers.pop()
print(nombres_premiers)  # [1, 3, 5]
```

### Utilisations des listes comme files
Les listes ne sont pas efficaces pour les files (FIFO : First In, First Out). Pour utiliser une file, il est préférable d'utiliser la bibliothèque `collections` :

```python
from collections import deque

nombres_premiers = deque([1, 3, 5, 7])

# Ajouter des éléments à la fin de la liste
nombres_premiers.append(11)
print(nombres_premiers)  # deque([1, 3, 5, 7, 11])
nombres_premiers.append(13)
print(nombres_premiers)  # deque([1, 3, 5, 7, 11, 13])

# Supprimer les premiers éléments de la liste
nombres_premiers.popleft()
print(nombres_premiers)  # deque([3, 5, 7, 11, 13])
nombres_premiers.popleft()
print(nombres_premiers)  # deque([5, 7, 11, 13])
nombres_premiers.popleft()
print(nombres_premiers)  # deque([7, 11, 13])
```

### Exemples sur la manipulation des listes
Ces exemples vont nous permettre de pratiquer nos connaissances déjà acquises dans la manipulation des listes.

1. Créer un programme qui gère une liste de courses et permet d'ajouter, supprimer et marquer des articles comme achetés.
2. Développer un programme qui calcule la moyenne et la médiane d'une liste de nombres.
3. Implémenter un jeu de devinettes où le joueur doit trouver un nombre caché dans une liste.

#### Résolution de certains de ces exemples

```python
# Premier exemple

def afficher_liste(liste_articles):
    if not liste_articles:
        print("\nLa liste d'articles est vide.")
    else:
        for item in liste_articles:
            print(f"- {item}")

def ajouter_article(liste_articles):
    article = input("Quel article souhaitez-vous ajouter ? : ")
    liste_articles.append(article)
    print(f"{article} ajouté à la liste.")

def supprimer_article(liste_articles):
    if not liste_articles:
        print("\nLa liste d'articles est vide.")
    afficher_liste(liste_articles)
    index = int(input("Entrez le numéro de

 l'article à supprimer : "))
    if 0 <= index < len(liste_articles):
        article = liste_articles.pop(index)
        print(f"{article} supprimé de la liste.")
    else:
        print("Numéro invalide.")

def marquer_achete(liste_articles):
    if not liste_articles:
        print("\nLa liste d'articles est vide.")
    afficher_liste(liste_articles)
    index = int(input("Entrez le numéro de l'article acheté : "))
    if 0 <= index < len(liste_articles):
        liste_articles[index] += " (acheté)"
        print(f"Article {liste_articles[index]} marqué comme acheté.")
    else:
        print("Numéro invalide.")

def liste_courses():
    liste_articles = []
    while True:
        print("\n1. Afficher la liste des articles")
        print("2. Ajouter un article")
        print("3. Supprimer un article")
        print("4. Marquer un article comme acheté")
        print("5. Quitter")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            afficher_liste(liste_articles)
        if choix == "2":
            ajouter_article(liste_articles)
        if choix == "3":
            supprimer_article(liste_articles)
        if choix == "4":
            marquer_achete(liste_articles)
        if choix == "5":
            print("Merci d'avoir utilisé notre programme.")
            break

liste_courses()
```

### Exercices pratiques
1. Créez une liste de nombres. Ajoutez, supprimez et modifiez des éléments de cette liste en utilisant les différentes méthodes vues.
2. Écrivez un programme qui parcourt une liste de chaînes de caractères et affiche chaque chaîne en majuscules.
3. Implémentez une fonction qui prend une liste de nombres en entrée et retourne la somme des carrés de chaque nombre.

---

### 2. Les tuples - Collections immuables
Les tuples sont similaires aux listes, mais ils sont immuables, ce qui signifie que leur contenu ne peut pas être modifié après leur création. Ils sont souvent utilisés pour stocker des collections d'éléments qui ne doivent pas changer.

#### Illustration
```python
# Création d'un tuple
mon_tuple = (1, 2, 3)

# Accès aux éléments
premier_element = mon_tuple[0]  # premier_element = 1

# Longueur du tuple
longueur = len(mon_tuple)  # longueur = 3
```

### Différence principale entre les listes et les tuples
- **Listes :** Mutables (modifiable) et définies par des crochets `[]`.
- **Tuples :** Immuables (non modifiable) et définies par des parenthèses `()`.

### Créer un tuple
Pour créer un tuple, il suffit de placer les éléments entre parenthèses, séparés par des virgules. Pour un seul élément, il faut ajouter une virgule après l'élément.

```python
# Création d'un tuple vide
mon_tuple_vide = ()

# Création d'un tuple avec un seul élément
mon_tuple_un_element = (5,)

# Création d'un tuple avec plusieurs éléments
mon_tuple = (1, 2, "trois", True)
print(mon_tuple_un_element)  # (5,)
print(mon_tuple)  # (1, 2, "trois", True)
```

### Accès aux éléments d'un tuple
Comme pour les listes, on accède aux éléments d'un tuple en utilisant l'index.

```python
# Accéder au premier élément du tuple
premier = mon_tuple[0]  # premier = 1

# Accéder au dernier élément du tuple
dernier = mon_tuple[-1]  # dernier = True
```

### Opérations avec les tuples
Bien que les tuples soient immuables, on peut effectuer des opérations similaires à celles sur les listes, sauf celles qui modifient le tuple.

```python
# Concaténation de tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
concat_tuple = tuple1 + tuple2  # concat_tuple = (1, 2, 3, 4)

# Répétition de tuples
repete_tuple = tuple1 * 3  # repete_tuple = (1, 2, 1, 2, 1, 2)

# Vérification d'appartenance
existe = 2 in tuple1  # existe = True
print(existe)  # True
```

### Utilité des tuples
Les tuples sont souvent utilisés pour représenter des données fixes ou constantes, comme des coordonnées géographiques (latitude, longitude), des points dans l'espace (x, y, z), ou pour renvoyer plusieurs valeurs depuis une fonction.

```python
# Représentation d'un point dans un plan 2D
point = (3, 5)

# Représentation de coordonnées géographiques
lieu = (48.8566, 2.3522)  # Latitude et longitude de Paris

# Retourner plusieurs valeurs depuis une fonction
def donnees_personnelles():
    nom = "Faustin"
    age = 30
    pays = "RDCongo"
    return nom, age, pays

personne = donnees_personnelles()
print(personne)  # ("Faustin", 30, "RDCongo")
```

### Conversion entre listes et tuples
On peut facilement convertir une liste en tuple et vice versa en utilisant les fonctions `list()` et `tuple()`.

```python
# Conversion d'une liste en tuple
ma_liste = [1, 2, 3]
mon_tuple = tuple(ma_liste)  # mon_tuple = (1, 2, 3)

# Conversion d'un tuple en liste
mon_tuple = (1, 2, 3)
ma_liste = list(mon_tuple)  # ma_liste = [1, 2, 3]
```

### Exercices pratiques sur les tuples
1. Créez un tuple de coordonnées (x, y, z) représentant un point dans l'espace. Accédez à chaque coordonnée individuellement.
2. Écrivez une fonction qui prend une liste de tuples représentant des points 2D (x, y) et retourne une liste de ces points triés par l'ordonnée (y).
3. Implémentez un programme qui prend une phrase et retourne un tuple contenant le nombre de mots, le nombre de caractères et le nombre de voyelles dans la phrase.

```python
# Premier exercice
point_3d = (10, 20, 30)
x, y, z = point_3d
print(f"x = {x}, y = {y}, z = {z}")  # x = 10, y = 20, z = 30

# Deuxième exercice
def trier_points(points):
    return sorted(points, key=lambda point: point[1])

points_2d = [(3, 5), (1, 4), (2, 2), (5, 3)]
points_tries = trier_points(points_2d)
print(points_tries)  # [(2, 2), (5, 3), (1, 4), (3, 5)]
```

Les listes et les tuples sont des outils puissants pour organiser et manipuler des données en Python. En comprenant leurs différences et en pratiquant leur utilisation, vous serez en mesure de choisir la structure de données la plus appropriée pour vos besoins spécifiques.
```
