import random

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.defense = 5
        self.exp = 0
        self.exp_to_next_level = 20
    
    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack += 5
        self.defense += 3
        self.exp = 0
        self.exp_to_next_level *= 1.5
        print(f"\n{self.name} leveled up! Now at level {self.level}!\n")

class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = random.randint(20, 50) + (level * 10)
        self.attack = random.randint(5, 10) + (level * 2)
        self.defense = random.randint(2, 5) + (level * 1)

def combat(player, monster):
    print(f"\nA wild {monster.name} appears! Level {monster.level}")
    while player.health > 0 and monster.health > 0:
        # Player turn
        damage = max(player.attack - monster.defense, 0)
        monster.health -= damage
        print(f"\n{player.name} attacks {monster.name} for {damage} damage!")
        
        if monster.health <= 0:
            print(f"{monster.name} is defeated!")
            exp_gain = monster.level * 10
            player.exp += exp_gain
            print(f"You gained {exp_gain} EXP!")
            if player.exp >= player.exp_to_next_level:
                player.level_up()
            return True

        # Monster turn
        damage = max(monster.attack - player.defense, 0)
        player.health -= damage
        print(f"{monster.name} attacks {player.name} for {damage} damage!")
        
        if player.health <= 0:
            print(f"{player.name} has been defeated! Game Over.")
            return False

def game_loop():
    print("Welcome to the Combat Game!")
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    while player.health > 0:
        monster_level = random.randint(1, player.level + 1)
        monster_name = random.choice(["Goblin", "Orc", "Wolf", "Skeleton", "Zombie"])
        monster = Monster(monster_name, monster_level)
        
        if not combat(player, monster):
            break

        # Rest and heal the player slightly after each fight
        player.health = min(player.max_health, player.health + 10)
        print(f"\n{player.name} rests and recovers some health.")

    print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    game_loop()
