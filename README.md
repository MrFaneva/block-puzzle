# 🎮 Block Puzzle / Tetris

Un petit jeu de type Tetris multi-joueurs (1 ou 2 joueurs) codé en Python avec Pygame.

## ✨ Fonctionnalités

- 🕹️ Mode **solo** ou **multijoueur** (2 joueurs côte à côte)
- 🧱 7 pièces classiques (I, O, T, S, Z, J, L)
- 📊 Système de score et de niveaux (la vitesse augmente avec le niveau)
- ⏸️ Pause (`P`)
- 🎨 Rendu simple avec contours des cellules
- 🏁 Détection de Game Over par joueur

## 🎯 Contrôles

### Joueur 1
| Action      | Touche |
|-------------|--------|
| Gauche      | `Q`    |
| Droite      | `D`    |
| Descendre   | `S`    |
| Rotation    | `Z`    |

### Joueur 2
| Action      | Touche  |
|-------------|---------|
| Gauche      | `←`     |
| Droite      | `→`     |
| Descendre   | `↓`     |
| Rotation    | `↑`     |

### Global
| Action | Touche     |
|--------|------------|
| Pause  | `P`        |
| Menu   | `1` / `2` puis `Entrée` |

## 🚀 Installation

### Prérequis
- Python **3.8+**
- pip

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/MrFaneva/block-puzzle.git
cd block-puzzle

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer le jeu
python main.py ou python3 main.py

🛠️ Makefile

Un Makefile est fourni pour simplifier les commandes :

make install   # installe les dépendances
make run       # lance le jeu
make clean     # nettoie les fichiers __pycache__

📁 Structure du projet

.
├── main.py          # Point d'entrée du jeu
├── game.py          # Gestion des joueurs et de la boucle de jeu
├── player.py        # Logique d'un joueur (grille, pièce, score)
├── piece.py         # Définition des pièces Tetris
├── grid.py          # Grille de jeu et détection de collisions
├── score.py         # Système de score et de niveaux
├── settings.py      # Constantes (taille, FPS, dimensions)
├── colors.py        # Palette de couleurs
├── sound.py         # Gestion des sons (optionnel)
├── storage.py       # Sauvegarde des scores (JSON)
├── requirements.txt
├── Makefile
└── README.md
