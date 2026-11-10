import random

def bear_claws(player):
    player.attack += 2

def fox_paws(player):
    player.move_speed *= 1.1

def boar_hide(player):
    player.max_health += 20
    player.health += 20

def wolf_scent(player):
    for weapon in player.weapons:
        weapon.attack_range *= 1.2

def cat_paws(player):
    player.move_speed *= 1.5

UPGRADES = [
    {"name": "Griffes d'ours",  "desc": "+2 attaque",         "apply": bear_claws},
    {"name": "Pattes de renard", "desc": "+10 % de vitesse",  "apply": fox_paws},
    {"name": "Peau de sanglier", "desc": "+20 PV max",        "apply": boar_hide},
    {"name": "Flair du loup",    "desc": "+20 % de portée",   "apply": wolf_scent},
    {"name": "Pattes de chat", "desc": "50% de vitesse", "apply": cat_paws}
]

def random_upgrades():
    return random.sample(UPGRADES, 3)