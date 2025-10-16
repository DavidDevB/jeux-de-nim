# Jeux de Nim 

### Ce programme permet de jouer à 2 variantes du jeu de Nim: 
#### * Variante simple
#### * Variante de Marienbad

#### 👨‍💻 Installation
- Installez Python 3 sur votre machine
- Téléchargez le fichier nim_games.py (ou ses variantes)
- Lancez le script correspondant à partir du terminal

### Fichier nim_games.py PvP (variante simple):
  
- 2 joueurs
- Permet de faire une partie du jeu de Nim contre un adversaire humain

#### 🛠️ Fonctionnalités:

- Entrer les noms de joueurs
- Choix aléatoire du joueur commençant
- Choix du nombre d'allumettes à prendre
- Affichage du nombre d'allumettes restantes
- Affichage du gagnant

#### 🧬 Structure du code
- get_user_name(player)
- get_first_player()
- play()

### Fichier nim_games.py PvE (variante simple):

- 1 joueur
- Permet de faire une partie de jeu de Nim contre l'ordinateur

#### 🛠️ Fonctionnalités:

- Entrer le nom du joueur.
- Choix aléatoire du joueur commençant.
- Choix du nombre d'allumettes à prendre.
- L'ordinateur choisit un nombre "5 - k" d'allumettes où "k" est le nombre d'allumettes précédemment choisi par le joueur.
- Affichage du nombre d'allumettes restantes.
- Affichage du gagnant.

#### 🧬 Structure du code
- get_user_name()
- get_first_player(player)
- play()

### Fichier nim_games_marienbad_pvp.py PvP (variante Marienbad):
  
- 2 joueurs
- Permet de faire une partie du jeu de Nim variante Marienbad contre un adversaire humain

#### 🛠️ Fonctionnalités:

- Entrer le nom de chaque joueur.
- Choix aléatoire du joueur commençant.
- Choix de la pile.
- Choix du nombre d'allumettes à prendre.
- Affichage du nombre d'allumettes restantes dans chaque pile.
- Affichage du gagnant.

#### Structure du code
- get_user_name()
- get_first_player()
- play()
- 
### Fichier nim_games_marienbad_pvp.py PvP (variante Marienbad):
  
- 2 joueurs
- Permet de faire une partie du jeu de Nim variante Marienbad contre un adversaire humain

#### 🛠️ Fonctionnalités:

- Entrer le nom du joueur.
- Choix aléatoire du joueur commençant.
- Choix de la pile.
- Choix du nombre d'allumettes à prendre.
- Affichage du nombre d'allumettes restantes dans chaque pile.
- Affichage du gagnant.

#### 🧬 Structure du code
- get_user_name()
- get_first_player()
- player_turn(matches)
- computer_turn(matches)
- play()