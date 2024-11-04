import os
import random


class Player:
    def __init__(self, name, alive=True, slots=0, load=None):
        self.name = name
        self.alive = alive
        self.slots = slots
        self.load = load if load is not None else [True] + [False for _ in range(5)]

    def show_name(self):
        return self.name

    def show_slots(self):
        return f"{self.slots}/6"

    def roll(self):
        result = random.choice(self.load)
        self.slots += 1
        if not result:
            del self.load[1]
        else:
            self.alive = False

        return result

    def to_dict(self):
        dict_data = {
            'name': self.name,
            'alive': self.alive,
            'slots': self.slots,
            'load': self.load
        }

        return dict_data

    @classmethod
    def from_dict(cls, data):
        reload_data = cls(name=data['name'], alive=data['alive'], slots=data['slots'], load=data['load'])
        return reload_data


def img_builder(directory):
    img_list = []
    for file in os.listdir(directory):
        img_list.append(file)

    return img_list
