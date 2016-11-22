# Monster.py
# Thorin Schmidt
# 11/16/2016

''' Monster Package '''
from character import *
from random import randint, choice

class Monster(Character):
    ''' generic monster class '''
    def __init__(self,
                 name = "Generic Foe",
                 maxHealth = 10,
                 speed = 25,
                 stamina = 25,
                 strength = 8,
                 dexterity = 8,
                 constitution = 10,
                 intelligence = 8,
                 wisdom = 10,
                 charisma = 10,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 50,
                 awareness = 50,
                 fear = 50):
        super(Monster, self).__init__(name, maxHealth, speed, stamina,
                                      strength, dexterity, constitution,
                                      intelligence, wisdom, charisma,
                                      numberOfPotions, inventory)
        self.aggression = aggression
        self.awareness = awareness
        self.fear = fear  #indicates cowardice level

    def combat_choice(self):
        ''' combat AI

            returns a, h, or f.  Based on aggression, awareness, morale
            
            '''
        attackValue = randint(1,100) + self.aggression
        healValue = randint(1,100) + self.awareness
        fleeValue = randint(1,100) + self.fear

        if attackValue >= healValue and attackValue >= fleeValue:
            return "a"
        elif healValue >= attackValue and healValue >= fleeValue:
            if self.health != self.maxHealth:
                return "h"
            else:
                return "a"
        elif fleeValue >= attackValue and fleeValue >= healValue:
            return "f"
        else:
            return "AI_error"

class Orc(Monster):
    ''' generic Orc class

        this class '''
    def __init__(self, name = "Dorque da Orc"):
        orcName = name
        maxHealth = randint(1,8)
        speed = 25
        stamina = 25
        strength = randint(8,10)
        dexterity = randint(10,12)
        constitution = 10
        intelligence = 8
        wisdom = 10
        charisma = 10
        numberOfPotions = 2
        inventory = []
        aggression = 80
        awareness = 30
        fear = 20
        super(Orc, self).__init__(orcName, maxHealth, speed, stamina, strength,
                                  dexterity, constitution, intelligence,
                                  wisdom, charisma, numberOfPotions,
                                  inventory, aggression, awareness, fear)

class Brownie(Monster):
    """Generic Brownie class"""
    def __init__(self,
                 name = "Chcolate Brownie",
                 maxHealth = 6,
                 speed = 20,
                 stamina = 25,
                 strength = 7,
                 intelligence = 14,
                 dexterity = 18,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 50,
                 awareness = 70,
                 fear = 90):
        super(Brownie, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)

class Troll(Monster):
    """ generic Troll class """
    def __init__(self,
                 name = "Internet Troll",
                 maxHealth = 63,
                 speed = 30,
                 stamina = 50,
                 strength = 21,
                 intelligence = 6,
                 dexterity = 14,
                 numberOfPotions = 1,
                 inventory = [],
                 aggression = 100,
                 awareness = 0,
                 fear = -100):
        super(Troll, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)
    def get_damage(self, damage):
        self.health -= damage
        self.health += randint(1, 8)

class Cloud_Giant(Monster):
    """ generic cloud giant class """
    def __init__(self,
                 name = "Cloud 9",
                 maxHealth = 168,
                 speed = 50,
                 stamina = 50,
                 strength = 35,
                 intelligence = 12,
                 dexterity = 13,
                 numberOfPotions = 1,
                 inventory = [],
                 aggression = 50,
                 awareness = 50,
                 fear = 25):
        super(Cloud_Giant, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)


class Guardian_Dragon(Monster):
    """ generic guardian dragon class """
    def __init__(self,
                 name = "Igneel",
                 maxHealth = 529,
                 speed = 50,
                 stamina = 75,
                 strength = 38,
                 intelligence = 15,
                 dexterity = 13,
                 numberOfPotions = 0,
                 inventory = [],
                 aggression = 100,
                 awareness = 75,
                 fear = 0):
        super(Guardian_Dragon, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)
    @property
    def AC(self):
        return 30 + self.dexBonus + self.armor.defense


def random_monster():
    '''generate a monster at random

    create an instance of each monster here, then add that instance to
    the listOfMonsters.  The function will pick a random instance out of
    the list, then return it to the caller.'''
    
    monster = Monster()
    orc = Orc()
    brownie = Brownie()
    troll = Troll()
    cloudGiant = Cloud_Giant()
    guardianDragon = Guardian_Dragon()
    
    listOfMonsters = [orc, brownie, troll, cloudGiant, guardianDragon]
    return choice(listOfMonsters)


if __name__ == "__main__":

    Grr = Orc(name = "Freddy")
    #Randy = random_monster()
    #print(Randy.name)


    
