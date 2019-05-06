from models import *

class Solution:
    def run(self, first_strike_army_name, no_of_dragons, no_of_white_lords):
        seven_kingdoms_army = []
        white_walker_army = []
        self.round = 0

        for i in range(no_of_dragons):
            dragon = Dragon()
            seven_kingdoms_army.append(dragon)
        for j in range(5000):
            infantry = Soldier()
            seven_kingdoms_army.append(infantry)

        for i in range(no_of_white_lords):
            white_lord = WhiteLord()
            white_walker_army.append(white_lord)
        for j in range(10000):
            walkers = Walker()
            white_walker_army.append(walkers)

        while len(seven_kingdoms_army) and len(white_walker_army) is not 0:
            if first_strike_army_name == "Seven Kingdom Army":
                self.fight(seven_kingdoms_army, white_walker_army)
                first_strike_army_name = "White walker Army"
            elif first_strike_army_name == "White walker Army":
                self.fight(white_walker_army,  seven_kingdoms_army)
                first_strike_army_name = "Seven Kingdom Army"

        if len(seven_kingdoms_army) <= 0:
            result = (f"White Walker Army|{self.round}")
        elif len(white_walker_army) <= 0:
            result = (f"Seven Kingdom Army|{self.round}")

        return result

    def fight(self, attacker, victim):
        a = len(attacker)
        b = len(victim)
        if a == 0 or b == 0:
            return self.round

        unit = 0

        for unit in range(len(attacker)):
            no_of_victims = len(victim)
            if no_of_victims is 0:
                break
            i = 0

            while (attacker[unit].damage) is not 0:
                self.attack(attacker[unit], victim, victim[i])
                
                no_of_victims = len(victim)
                if len(victim) == 0:
                    break
            
        if len(victim) > 0:
            for x in range(len(victim)):
                victim[x].replenish()

        self.round += 1



    def attack(self, attack_unit, victim, victim_unit):
        temp = attack_unit.damage
        attack_unit.damage -= victim_unit.defense
        victim_unit.defense = victim_unit.defense - temp

        if attack_unit.damage < 0:
            attack_unit.damage = 0
        if victim_unit.defense <= 0:
            victim.remove(victim_unit)
            

def main():
    print("hello world")
    test = Solution()
    res = test.run("Seven Kingdom Army", 4, 1)
    print(res)


if __name__ == "__main__":
    main()