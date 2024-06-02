### Jour 4 : Fonctions et leurs arguments

#### Objectifs du jour
- Comprendre ce qu'est une fonction.
- Apprendre à définir et utiliser des fonctions.

#### Contenu

##### Définition et appel de fonctions

Les fonctions en Python sont des blocs de code réutilisables qui effectuent une tâche spécifique. Elles permettent de structurer le code de manière modulaire, facilitant ainsi la maintenance et la réutilisation.

###### Définir une fonction

Pour définir une fonction, utilisez le mot-clé `def` suivi du nom de la fonction, de parenthèses et d'un deux-points. Ensuite, écrivez le corps de la fonction avec un retrait (indentation).

```python
def dire_bonjour():
    print("Bonjour")
```

###### Appeler une fonction

Pour appeler une fonction, écrivez son nom suivi de parenthèses.

```python
dire_bonjour()  # Affiche "Bonjour"
```

Dans cet exemple, la fonction `dire_bonjour` est définie pour afficher "Bonjour" à chaque fois qu'elle est appelée.

##### Arguments de fonctions

Les fonctions peuvent accepter des paramètres (ou arguments) pour personnaliser leur comportement.

###### Exemple : Saluer quelqu'un

Supposons que nous souhaitons créer une fonction qui salue une personne en mentionnant son nom.

```python
def saluer(nom):
    print(f"Bonjour, {nom}")
saluer("Alice")  # Affiche "Bonjour, Alice"
saluer("Boubacar")  # Affiche "Bonjour, Boubacar"
```

Dans cet exemple, la fonction `saluer` prend un argument `nom` et affiche un message de salutation personnalisé.

##### Valeur de retour

Les fonctions peuvent également renvoyer des valeurs en utilisant le mot-clé `return`.

###### Exemple : Calculer le total des prix des fruits

Supposons que nous souhaitons créer une fonction qui additionne deux nombres et renvoie le résultat.

```python
def addition(a, b):
    return a + b
resultat = addition(3, 4)
print(resultat)  # Affiche 7
```

Dans cet exemple, la fonction `addition` prend deux arguments `a` et `b`, calcule leur somme et renvoie le résultat. Le résultat est ensuite stocké dans la variable `resultat` et affiché.

##### Arguments par défaut et nommés

Les fonctions peuvent avoir des arguments par défaut, ce qui permet de les appeler sans spécifier ces arguments.

###### Exemple : Salutation avec message par défaut

Supposons que nous souhaitons créer une fonction de salutation avec un message par défaut, mais que nous pouvons personnaliser si nécessaire.

```python
def salutation(nom, message="Bonjour"):
    print(f"{message}, {nom}")
salutation("Alice")  # Affiche "Bonjour, Alice"
salutation("Bob", "Salut")  # Affiche "Salut, Bob"
```

Dans cet exemple, la fonction `salutation` a deux arguments : `nom` et `message`. Si aucun message n'est spécifié lors de l'appel de la fonction, le message par défaut "Bonjour" est utilisé. Sinon, le message spécifié est utilisé.
