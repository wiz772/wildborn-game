# 🐾 Wildborn

**Wildborn** est un jeu vidéo 2D développé en Python avec Pygame. Le joueur doit survivre à des vagues successives d'animaux hostiles dans un environnement en vue de dessus (*top-down*).

Au fil de la partie, il affronte des ennemis de plus en plus nombreux, élimine des adversaires pour gagner de l'expérience et débloque des améliorations afin de prolonger sa survie.

# 🌍 Génération procédurale du monde

Wildborn dispose de son propre système de génération procédurale de monde, développé à partir d'une bibliothèque personnelle de bruit de Perlin : https://github.com/wiz772/py-perlin-noise

Cette bibliothèque permet de générer des cartes de bruit utilisées pour construire les environnements et répartir les différents types de terrains.

L'objectif est de produire des environnements cohérents et variés de manière procédurale, sans avoir à concevoir chaque carte manuellement.

## 🎮 Gameplay

- **Survie par vagues** : affronter des vagues d'animaux hostiles.
- **Combat** : utiliser différentes armes pour éliminer les ennemis.
- **Progression** : gagner de l'expérience et débloquer des améliorations.
- **Upgrades** : améliorer les statistiques du joueur et ses capacités.
- **Armes** : débloquer et améliorer différents types d'armes.
- **Score** : enregistrer ses performances et tenter de battre son meilleur temps.

## ⚔️ Système de progression

Le joueur peut obtenir différentes améliorations au cours de sa partie :

| Amélioration | Effet |
|---|---|
| Griffes d'ours | Augmente les dégâts |
| Pattes de renard | Augmente la vitesse |
| Peau de sanglier | Augmente les points de vie |
| Flair du loup | Augmente la portée des armes |
| Carapace de tortue | Augmente la défense |
| Sang de phénix | Restaure une partie des PV |

De nouvelles armes peuvent également être débloquées, comme l'arc ou l'aura.

## 🛠️ Technologies

- **Python** — Langage principal.
- **Pygame** — Gestion du jeu, des événements, du rendu et des collisions.
- **JSON** — Persistance locale des scores et des données.

## 📂 Architecture

Le projet est organisé en plusieurs modules afin de séparer les responsabilités :

- `entities/` : entités du jeu, joueurs et ennemis.
- `weapons/` : logique des armes et système d'attaque.
- `effects/` : effets visuels et animations.
- `world/` : génération et gestion de l'environnement.
- `rendering/` : affichage du jeu et interface utilisateur.
- `persistence/` : sauvegarde et chargement des données.
- `utils/` : fonctions utilitaires.

## 🚀 Installation

### Prérequis

- Python 3
- pip

### Installation

Cloner le dépôt :

```bash
git clone <repository-url>
cd Wildborn
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer le jeu :

```bash
python main.py
```

## 🎮 Contrôles

| Touche | Action |
|---|---|
| Z / Q / S / D | Déplacement |
| Entrée | Valider / commencer |
| Échap | Pause / retour |
| & / é / " (1,2,3) | Choix d'upgrade

## 📈 Objectifs techniques

Ce projet a notamment pour objectif de mettre en pratique :

- La programmation orientée objet (POO).
- La séparation des responsabilités et la modularité.
- La gestion des événements et de la boucle de jeu.
- La gestion du temps avec le delta time.
- La détection des collisions et des distances.
- La génération procédurale d'environnements.
- La gestion des états du jeu.
- La persistance des données en JSON.

---

*Wildborn — Survive the wild.*