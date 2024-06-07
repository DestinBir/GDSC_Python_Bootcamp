### Jour 5 : Exercices pratiques

#### Objectifs du jour
- Mettre en pratique les concepts appris.
- Créer une application de calculatrice basique.

#### Contenu

##### Projet : Calculatrice basique

##### Exigences
- Créer une application capable d'effectuer les opérations d'addition, de soustraction, de multiplication et de division.

##### Étapes de développement
1. Demandez à l'utilisateur d'entrer deux nombres.
2. Demandez à l'utilisateur de choisir une opération (addition, soustraction, multiplication, division).
3. Effectuez l'opération choisie et affichez le résultat.

##### Exemple de code
```python
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : Division par zéro"
    return a / b

def calculatrice():
    print("Bienvenue dans la calculatrice basique!")
    num1 = float(input("Entrez le premier nombre: "))
    num2 = float(input("Entrez le deuxième nombre: "))
    operation = input("Choisissez une opération (+, -, *, /): ")

    if operation == "+":
        print("Résultat:", addition(num1, num2))
    elif operation == "-":
        print("Résultat:", soustraction(num1, num2))
    elif operation == "*":
        print("Résultat:", multiplication(num1, num2))
    elif operation == "/":
        print("Résultat:", division(num1, num2))
    else:
        print("Opération invalide")

calculatrice()
```
### une implémentation pro

```python
import tkinter as tk
# Fonction pour évaluer l'expression
def evaluer_expression(expression):
    try:
        resultat = str(eval(expression))
        return resultat
    except Exception as e:
        return "Erreur"

# Fonction pour mettre à jour le champ d'entrée
def mettre_a_jour_expression(texte):
    texte_courant = entree.get()
    entree.delete(0, tk.END)
    entree.insert(0, texte_courant + texte)

# Fonction pour effacer le champ d'entrée
def effacer_expression():
    entree.delete(0, tk.END)

# Initialiser la fenêtre principale
fenetre = tk.Tk()
fenetre.title("La calculatrice de Destin")
fenetre.configure(bg="#1F1F2E")  # Fond bleu marine

# Définir le widget d'entrée
entree = tk.Entry(fenetre, font=("Helvetica", 24), justify="right", bg="#1F1F2E", fg="#FFFFFF", bd=10, relief="flat")
entree.grid(row=0, column=0, columnspan=4, sticky="we", padx=10, pady=10)

# Définir les boutons et leurs positions
boutons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("(", 5, 1), (")", 5, 2)
]

for (texte, ligne, col) in boutons:
    if texte == "=":
        bouton = tk.Button(fenetre, text=texte, command=lambda: entree.insert(tk.END, "=" + evaluer_expression(entree.get())), bg="#D3D3D3", fg="#1F1F2E", font=("Helvetica", 18), relief="flat", bd=10)
    elif texte == "C":
        bouton = tk.Button(fenetre, text=texte, command=effacer_expression, bg="#D3D3D3", fg="#1F1F2E", font=("Helvetica", 18), relief="flat", bd=10)
    else:
        bouton = tk.Button(fenetre, text=texte, command=lambda t=texte: mettre_a_jour_expression(t), bg="#D3D3D3", fg="#1F1F2E", font=("Helvetica", 18), relief="flat", bd=10)
    bouton.grid(row=ligne, column=col, sticky="nsew", padx=5, pady=5)

# Configurer les lignes et colonnes pour qu'elles se redimensionnent
for i in range(6):
    fenetre.grid_rowconfigure(i, weight=1)
for i in range(4):
    fenetre.grid_columnconfigure(i, weight=1)

# Démarrer la boucle principale
fenetre.mainloop()
```


##### Testez votre application
- Exécutez le script et testez les différentes opérations pour vous assurer que tout fonctionne correctement.

---
