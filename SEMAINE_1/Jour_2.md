### Jour 2 : Variables, types de données et opérateurs

#### Objectifs du jour
- Comprendre les variables et les différents types de données en Python.
- Apprendre à utiliser les opérateurs.

#### Contenu

##### Variables
- Déclaration et affectation :
  ```python
  x = 5
  y = "Bonjour"
  ```
- Nommage des variables : commencez par une lettre ou un underscore (_), suivi de lettres, chiffres ou underscores.

##### Types de données
- Numériques : `int`, `float`
  ```python
  age = 25       # int
  pi = 3.14      # float
  ```
- Chaînes de caractères : `str`
  ```python
  nom = "Alice"
  ```
- Booléens : `bool`
  ```python
  is_active = True
  ```
- Listes, tuples, dictionnaires :
  ```python
  fruits = ["pomme", "banane", "cerise"]  # liste
  coordonnees = (10.0, 20.0)              # tuple
  personne = {"nom": "Alice", "age": 25}  # dictionnaire
  ```

##### Opérateurs

Les opérateurs en Python permettent d'effectuer des opérations sur des variables et des valeurs. Ils peuvent être classés en plusieurs catégories :

###### Opérateurs arithmétiques
Ces opérateurs sont utilisés pour effectuer des opérations mathématiques courantes :

- Addition (`+`): Additionne deux nombres.
  ```python
  somme = 10 + 5  # somme vaut 15
  ```
- Soustraction (`-`): Soustrait un nombre d'un autre.
  ```python
  difference = 10 - 5  # difference vaut 5
  ```
- Multiplication (`*`): Multiplie deux nombres.
  ```python
  produit = 4 * 3  # produit vaut 12
  ```
- Division (`/`): Divise un nombre par un autre.
  ```python
  division = 10 / 2  # division vaut 5.0
  ```
- Modulo (`%`): Renvoie le reste d'une division.
  ```python
  reste = 10 % 3  # reste vaut 1
  ```
- Exponentiation (`**`): Élève un nombre à la puissance d'un autre.
  ```python
  puissance = 2 ** 3  # puissance vaut 8
  ```
- Division entière (`//`): Divise deux nombres et renvoie la partie entière du résultat.
  ```python
  division_entiere = 10 // 3  # division_entiere vaut 3
  ```

###### Opérateurs de comparaison
Ces opérateurs comparent deux valeurs et renvoient un résultat booléen (`True` ou `False`):

- Égal à (`==`): Vérifie si deux valeurs sont égales.
  ```python
  est_egal = (5 == 5)  # est_egal vaut True
  ```
- Différent de (`!=`): Vérifie si deux valeurs sont différentes.
  ```python
  est_different = (5 != 3)  # est_different vaut True
  ```
- Plus grand que (`>`): Vérifie si une valeur est plus grande qu'une autre.
  ```python
  est_plus_grand = (10 > 7)  # est_plus_grand vaut True
  ```
- Plus petit que (`<`): Vérifie si une valeur est plus petite qu'une autre.
  ```python
  est_plus_petit = (7 < 10)  # est_plus_petit vaut True
  ```
- Plus grand ou égal à (`>=`): Vérifie si une valeur est plus grande ou égale à une autre.
  ```python
  est_plus_grand_ou_egal = (10 >= 10)  # est_plus_grand_ou_egal vaut True
  ```
- Plus petit ou égal à (`<=`): Vérifie si une valeur est plus petite ou égale à une autre.
  ```python
  est_plus_petit_ou_egal = (7 <= 8)  # est_plus_petit_ou_egal vaut True
  ```

###### Opérateurs logiques
Ces opérateurs sont utilisés pour combiner des expressions booléennes :

- `and`: Renvoie `True` si les deux expressions sont `True`.
  ```python
  a = True
  b = False
  resultat = a and b  # resultat vaut False
  ```
- `or`: Renvoie `True` si au moins une des expressions est `True`.
  ```python
  resultat = a or b  # resultat vaut True
  ```
- `not`: Renvoie l'inverse de l'expression.
  ```python
  resultat = not a  # resultat vaut False
  ```

---

Ces explications devraient fournir une base solide pour comprendre comment utiliser les opérateurs en Python. N'hésitez pas à expérimenter avec ces opérateurs pour vous familiariser avec leur comportement.
