import random
import time

class Robot:
    def __init__(self, name, kaomoji, hp, atk, critRate, critDmg):
        self.name = name
        self.kaomoji = kaomoji
        self.hp = hp
        self.atk = atk
        self.critRate = critRate
        self.critDmg = critDmg
    def attack(self, enemy):
        dmg = random.randint(1, self.atk)
        # if attack is crit
        if random.random() < self.critRate:
            dmg = dmg + self.critDmg*dmg
            dmg = int(dmg)
            print("💥", end=" ")
        enemy.hp -= dmg
        print(f"{self.name} attacks {enemy.name} for {dmg} damage!")

class Battle:
    def start_fight(self, robot1, robot2):
        while robot1.hp > 0 and robot2.hp > 0:
            robot1.attack(robot2)
            time.sleep(0.5)
            if robot2.hp <= 0:
                print(f"😞 {robot2.name} is defeated!")
                print(f"🏆 {robot1.name} wins!")
                break
            robot2.attack(robot1)
            time.sleep(0.5)
            if robot1.hp <= 0:
                print(f"😞 {robot1.name} is defeated!")
                print(f"🏆 {robot2.name} wins!")
                break

class Game:
    def __init__(self):
        self.robots = []
    def add_robot(self, robot):
        self.robots.append(robot)
    def start_game(self):
        print("Choose robots for the battle:")
        print("❤️ HP | 🗡️ ATK | ⚡ CRIT RATE | 💥 CRIT DMG")
        for i in range(len(self.robots)):
            print(f"{i+1}. {str(self.robots[i].kaomoji)}", end=" ")
            print(f"{self.robots[i].name} -", end=" ")
            print(f"❤️ {str(self.robots[i].hp)} |", end=" ")
            print(f"🗡️ {str(self.robots[i].atk)} |", end=" ")
            print(f"⚡ {str(self.robots[i].hp)} |", end=" ")
            print(f"💥 {str(self.robots[i].hp)}")
        while True:
            # first robot choice
            while True:
                try:
                    firstRobot = int(input("Select the first robot: "))
                except ValueError:
                    print(f"Choice for Robot 1 must be only a number. Please choose between 1-{len(self.robots)} for Robot 1.")
                    continue
                if (firstRobot<1) or (firstRobot>len(self.robots)) or (len(str(firstRobot)) == 0):
                    if len(str(firstRobot)) == 0:
                        print("Choice can't be empty.", end=" ")
                    print(f"Please choose between 1-{len(self.robots)} for Robot 1.")
                    continue
                break

            # second robot choice
            while True:
                try:    
                    secondRobot = int(input("Select the second robot: "))
                except ValueError:
                    print(f"Choice for Robot 2 must be only a number. Please choose between 1-{len(self.robots)} for Robot 2.")
                    continue
                if (secondRobot<1) or (secondRobot>len(self.robots)) or (len(str(secondRobot)) == 0):
                    if len(str(firstRobot)) == 0:
                        print("Choice can't be empty.", end=" ")
                    print(f"Please choose between 1-{len(self.robots)} for Robot 2.")
                    continue
                break
                
            # if both choices are the same
            if firstRobot == secondRobot:
                print("Robot 1 and Robot 2 can't have the same choice.")
                continue

            # if both choices are valid
            break

        robot1 = self.robots[firstRobot-1]
        robot2 = self.robots[secondRobot-1]

        print("Battle Start!")
        battle = Battle()
        battle.start_fight(robot1, robot2)

game = Game()

robot1 = Robot("RoboOne", "└[∵┌] ", 50, 25, 0.36, 0.5)
game.add_robot(robot1)
robot2 = Robot("RoboTwo", "└|￣皿￣|┘", 68, 17, 0.75, 1.4)
game.add_robot(robot2)
robot3 = Robot("RoboThree", "┌| ﾟдﾟ|/┘", 25, 36, 0.13, 1.1)
game.add_robot(robot3)

game.start_game()