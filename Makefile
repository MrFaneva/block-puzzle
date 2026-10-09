# Makefile — Block Puzzle / Tetris
PYTHON = python3
VENV   = venv
PIP    = $(VENV)/bin/pip

.PHONY: all install run clean help

all: run

## Créer l'environnement virtuel et installer les dépendances
install:
	@echo "🔧 Création de l'environnement virtuel..."
	$(PYTHON) -m venv $(VENV)
	@echo "📦 Installation des dépendances..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Installation terminée ! Utilise 'make run' pour jouer."

## Lancer le jeu
run:
	@echo "🎮 Lancement du jeu..."
	$(PYTHON) main.py

## Nettoyer les fichiers temporaires
clean:
	@echo "🧹 Nettoyage..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "✅ Nettoyage terminé."

## Afficher l'aide
help:
	@echo "Commandes disponibles :"
	@echo "  make install   → crée le venv et installe les dépendances"
	@echo "  make run       → lance le jeu"
	@echo "  make clean     → supprime les fichiers temporaires"
