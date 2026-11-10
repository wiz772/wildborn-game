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

def turtle_shell(player):
    player.defense += 3

def viper_fangs(player):
    player.attack += 3

def bison_heart(player):
    player.max_health += 15
    player.health += 15

def eagle_sight(player):
    for weapon in player.weapons:
        weapon.attack_range *= 1.3

def phoenix_blood(player):
    player.health = min(
        player.max_health,
        player.health + int(player.max_health * 0.5)
    )

UPGRADES = [
    {"name": "Griffes d'ours",  "desc": "+2 attaque",         "apply": bear_claws},
    {"name": "Pattes de renard", "desc": "+10 % de vitesse",  "apply": fox_paws},
    {"name": "Peau de sanglier", "desc": "+20 PV max",        "apply": boar_hide},
    {"name": "Flair du loup",    "desc": "+20 % de portée",   "apply": wolf_scent},
    {"name": "Pattes de chat", "desc": "50% de vitesse", "apply": cat_paws},
    {"name": "Carapace de tortue", "desc": "+3 défense", "apply": turtle_shell},
    {"name": "Crocs de vipère", "desc": "+3 attaque", "apply": viper_fangs},
    {"name": "Cœur de bison", "desc": "+15 PV max", "apply": bison_heart},
    {"name": "Regard d'aigle", "desc": "+30 % de portée", "apply": eagle_sight},
    {"name": "Sang de phénix", "desc": "Restaure 50 % des PV max", "apply": phoenix_blood},
]

def random_upgrades():
    return random.sample(UPGRADES, 3)