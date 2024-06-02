### Jour 3 : Structures de contrôle

#### Objectifs du jour
- Apprendre à utiliser les instructions conditionnelles.
- Comprendre et utiliser les boucles.

#### Contenu

##### Instructions conditionnelles

Les instructions conditionnelles permettent d'exécuter des blocs de code différents en fonction de conditions spécifiques. Elles sont essentielles pour écrire des programmes qui peuvent prendre des décisions.

###### Exemple  : Vérification de l'âge pour voter
En Afrique, de nombreux pays exigent que les citoyens aient au moins 18 ans pour voter. Voici comment nous pourrions utiliser des instructions conditionnelles pour vérifier si une personne est éligible pour voter.

```python
age = 20
if age < 18:
    print("Mineur - Non éligible pour voter")
elif age < 65:
    print("Adulte - Éligible pour voter")
else:
    print("Senior - Éligible pour voter")
```

Dans cet exemple, le programme vérifie l'âge et imprime un message en conséquence. Si l'âge est inférieur à 18 ans, la personne est considérée comme mineure et non éligible pour voter. Si l'âge est entre 18 et 65 ans, la personne est un adulte et éligible pour voter. Si l'âge est supérieur à 65 ans, la personne est un senior et également éligible pour voter.

##### Boucles

Les boucles permettent de répéter des blocs de code plusieurs fois. Il existe deux types principaux de boucles en Python : `for` et `while`.

###### Boucle `for`
La boucle `for` est utilisée pour itérer sur une séquence (liste, tuple, dictionnaire, ensemble ou chaîne de caractères).

###### Exemple : Calcul des prix des fruits sur le marché

Supposons que nous voulons calculer le total des prix des fruits achetés sur un marché local.

```python
fruits = {"banane": 100, "pomme": 200, "orange": 150}
total = 0

for fruit, prix in fruits.items():
    print(f"Le prix de {fruit} est {prix} FC")
    total += prix

print(f"Le coût total est {total} FC")
```

Dans cet exemple, nous avons un dictionnaire de fruits avec leurs prix en FCFA. La boucle `for` itère sur chaque fruit et ajoute le prix au total. Finalement, le coût total des fruits est affiché.

###### Boucle `while`
La boucle `while` continue de s'exécuter tant qu'une condition est vraie.

###### Exemple  : Remplir des seaux d'eau jusqu'à ce qu'ils soient pleins

Imaginons que nous devons remplir des seaux d'eau jusqu'à ce qu'ils soient pleins. Supposons que la capacité d'un seau est de 10 litres.

```python
capacite_seau = 10
litres_ajoutes = 0

while litres_ajoutes < capacite_seau:
    print(f"Ajout de 1 litre d'eau au seau. Total: {litres_ajoutes + 1} litres")
    litres_ajoutes += 1

print("Le seau est plein!")
```

Dans cet exemple, la boucle `while` continue d'ajouter 1 litre d'eau au seau tant que le total des litres ajoutés est inférieur à la capacité du seau. Une fois que le seau est plein (10 litres), la boucle s'arrête et un message est affiché pour indiquer que le seau est plein.

---
