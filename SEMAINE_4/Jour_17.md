# Manipulation des Fichiers avec Python | Lecture et écriture de fichiers.

La manipulation des fichiers est une compétence essentielle en programmation, permettant de lire, écrire et gérer des données stockées sur le disque. Python fournit plusieurs méthodes pour manipuler les fichiers de manière efficace. Nous allons le découvrir ensemble dans cette semaine consacrée à la manipulation des fichiers.

## Table des Matières

1. [Comprendre les Bases](#comprendre-les-bases)
   - [Ouverture et Fermeture des Fichiers](#ouverture-et-fermeture-des-fichiers)
   - [Lecture de Fichiers](#lecture-de-fichiers)
   - [Écriture dans les Fichiers](#écriture-dans-les-fichiers)
2. [Utiliser les Contextes](#utiliser-les-contextes)
   - [Gestion des Contextes avec `with`](#gestion-des-contextes-avec-with)

## Comprendre les Bases

### Ouverture et Fermeture des Fichiers

Avant de pouvoir lire ou écrire dans un fichier, vous devez l'ouvrir en utilisant la fonction intégrée `open()`. Cette fonction retourne un objet fichier que vous pouvez utiliser pour interagir avec le fichier. Voici les modes les plus courants pour ouvrir un fichier :

- `'r'`: Il ouvre le fchier en mode `lecture seule`. En un terme plus technique, c'est le mode `read`
- `'w'`: Il ouvre le fichier en mode `Écriture seule` (Cette manipulation écrase le fichier existant ou en crée un nouveau). En un terme plus technique, c'est le mode `write`
- `'a'`: Il ouvre le fichier en mode `Ajout` (Cette manipulation permet de faire une écriture à la fin du fichier). En un terme plus technique, c'est le mode `append`
- `'b'`: Il ouvre le fchier en mode `binaire`
- `'t'`: Il ouvre le fchier en mode `texte` (C'est le mode par défaut pour chaque fichier ouvert)

#### Exemple

```python
# Ouverture d'un fichier en lecture seule
fichier = open('nom_fichier_texte.txt', 'r')

# Fermeture du fichier
fichier.close()
```

### Lecture de Fichiers

Il existe plusieurs méthodes pour lire le contenu d'un fichier en Python :

- `read()`: Cette manipulation lit tout le contenu du fichier
- `readline()`: Cette manipulation lit une seule ligne du fichier
- `readlines()`: Cette manipulation lit toutes les lignes et retourne une liste

#### Exemple

```python
# Lecture de tout le contenu
with open('nom_fichier_texte.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)

"""
La manipulation ci-haut est la même que:

fichier = open('nom_fichier_texte.txt', 'r')
contenu = fichier.read()
print(contenu)
fichier.close()

L'instruction with s'emploi pour lire les fichiers de manière sécuritaire. On y reviendra un peu plus tard

"""

# Lecture ligne par ligne
with open('nom_fichier_texte.txt', 'r') as fichier:
    for ligne in fichier:
        print(ligne, end='')
```

### Écriture dans les Fichiers

On écrit dans un fichier en utilsant les méthodes `write()` et `writelines()`.

#### Exemple

```python
# Écriture dans un fichier
with open('om_fichier_texte.txt', 'w') as fichier:
    fichier.write("Quatrième semaine du Python bootcamp .\n")

# Ajout à un fichier existant
with open('exemple.txt', 'a') as fichier:
    fichier.write("Organiser par GDSC UCB.\n")
```

## Utiliser les Contextes

### Gestion des Contextes avec `with`

Utiliser l'instruction `with` pour ouvrir et fermer les fichiers est recommandé. Elle garantit que le fichier est correctement fermé même si une erreur survient pendant les opérations sur le fichier.

#### Exemple

```python
# Utilisation de with pour gérer automatiquement la fermeture du fichier
with open('exemple.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)
```

## Conclusion

ça été beau tout ça mais il nous faut un peu de pratique pour bien assimiler tout ce que nous avons ici du coup, je nous laisse un petit défi:

`Faire un petit script qui demandera à l'utilisateur d'entrer le nom d'un fichier ensuite le script genère les tables de multiplication de 1 à 12 dans le fichiers choisi par l'utilisateur. J'aimerai qu'on traite le cas où le nom du fichier choisi par l'utilisateur existe déjà, que le script demande de choisir un autre nom jusqu'à ce qu'on en choisisse un qui soit different.`

`ENJOY IT! 😊`
