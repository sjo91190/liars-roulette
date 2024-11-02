import os
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.slots = 0
        self.load = [True] + [False for i in range(5)]

    def show_name(self):
        return self.name

    def roll(self):
        result = random.choice(self.load)
        self.slots += 1
        if not result:
            del self.load[1]
        else:
            self.alive = False

        return result

    def show_slots(self):
        return f"{self.slots}/6"


def create(player_list):
    player_obj = []
    for item in player_list:
        player_obj.append(Player(name=item))

    return dict(zip(player_list, player_obj))


def img_builder(dir):
    img_list =[]
    for file in os.listdir(dir):
        img_list.append(file)

    return img_list
