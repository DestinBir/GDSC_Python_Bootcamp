### Jour 4 : Fonctions et leurs arguments

#### Objectifs du jour
- Comprendre ce qu'est une fonction.
- Apprendre à définir et utiliser des fonctions.

#### Contenu

##### Définition et appel de fonctions
- Définir une fonction :
  ```python
  def dire_bonjour():
      print("Bonjour")
  ```
- Appeler une fonction :
  ```python
  dire_bonjour()
  ```

##### Arguments de fonctions
- Avec arguments :
  ```python
  def saluer(nom):
      print(f"Bonjour, {nom}")
  saluer("Alice")
  ```

##### Valeur de retour
- Utiliser `return` pour renvoyer une valeur :
  ```python
  def addition(a, b):
      return a + b
  resultat = addition(3, 4)
  print(resultat)
  ```

##### Arguments par défaut et nommés
  ```python
  def salutation(nom, message="Bonjour"):
      print(f"{message}, {nom}")
  salutation("Alice")
  salutation("Bob", "Salut")
  ```

