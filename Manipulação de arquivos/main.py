#os = blibioteca "universal"?
# as file == abrindo txt como arquivo
#fil.write .
#/n igual puffar uma linha nova
#lines = file . Readlines ()
#strip corta a linha

import os
import random

def read_heroes(file_path):
    heroes = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            name, health, attack = line.strip().split(",")
            hero = Heroi(name, int(health), int(attack))
            heroes.append(hero)
    return heroes

def read_dragons(file_path):
    dragons = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            name, health, attack = line.strip().split(",")
            dragon = Dragao(name, int(health), int (attack))
            dragons.append(dragon)
    return dragons

os.makedirs("heroes", exist_ok=True)
os.makedirs("dragons", exist_ok=True)

with open("heroes/heroes.txt", "w") as file:
    file.write("LordPuff,100,50\npufantudo,120,40\n")

with open("dragons/dragons.txt", "w") as file:
    file.write("MiniCinthia,150,60\npinchbull,130,70\n")

class Character:
    def __init__(self, name, health, attack,):
        self.name = name
        self.health = health
        self.attack = attack

class Heroi(Character):
    def __str__(self):
        return f"Hero: {self.name}, Health: {self.health}, Attack: {self.attack}"
class Dragao(Character):
    def __str__(self):
        return f"Dragon: {self.name}, Health: {self.health}, Attack: {self.attack}"

heroes = read_heroes("heroes/heroes.txt")
dragons = read_dragons("dragons/dragons.txt")

random_hero = random.choice(heroes)
random_dragon = random.choice(dragons)

def run_tournament():
    random_hero = random.choice(heroes)
    random_dragon = random.choice(dragons)
    if random_hero.attack > random_dragon.attack:
        print(f"{random_hero.name} venceu {random_dragon.name}!")
    else:
        print(f"{random_dragon.name} derrotou {random_hero.name}!")

run_tournament()
#DOOM PUFFE SEGUNDO PRINCIPE DO REINO PUFOSO ELE GOVERNADA E REINAVA SENDO O MAIS FORTE DAS BATALHAS DE PUFFS,ENTRE ANOS
# ANOS PASSANDO O DOM PUFFE FOI GANHANDO ALUNOS