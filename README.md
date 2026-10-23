# Devine le nombre

Deux petits programmes Python autour d'un jeu : un jeu où le joueur devine un nombre entre 1 et 100, et un algorithme de **recherche binaire** qui trouve n'importe quel nombre en 7 essais au maximum.

## Fonctionnalités
- `jeu.py` : le joueur devine, le programme répond « Plus grand » ou « Plus petit » et compte les essais.
- `devine.py` : la fonction `deviner(secret)` trouve le secret par recherche binaire et renvoie le nombre d'essais.
- `pire_cas()` mesure le nombre maximal d'essais sur tous les secrets possibles.

## Installation
Testé avec Python 3.14. Aucune bibliothèque externe pour jouer.
Pour les tests : `py -m pip install pytest`

## Utilisation
```
py jeu.py
py devine.py
```

## Pourquoi la recherche binaire ?

Par ce que sans aucune méthode il n'y a pas de maximum d'essais : à chaque essais, on coupe l'intervalle en deux pour trouver n'importe quel nombre entre 1 et 100 en 7 essais et 10 essais pour 1000 nombres. 

## Tests
Depuis la racine du projet : `py -m pytest`

## Structure
- `jeu.py` : le jeu interactif
- `devine.py` : la recherche binaire et sa mesure
- `test_devine.py` : tests automatiques

## Limites connues
- `jeu.py` accepte les nombres hors 1 à 100 et les compte comme des essais.
- `jeu.py` n'est pas testé automatiquement, parce que la logique est mêlée aux `input` et aux `print`.
- La recherche binaire est une simulation: le secret est donné à la fonction.

## Améliorations futures
- Refuser les nombres hors intervalle dans le jeu.
- Séparer la logique du jeu pour pouvoir la tester.
- Option `--max` pour jouer sur un intervalle plus grand.
- Mode interactif où l'ordinateur devine un nombre pensé par l'utilisateur.