from random import randint
from pokemon import Pokemon

pokemon1 = Pokemon("Squirtle", "water")
pokemon2 = Pokemon("Gengar", "ghost", 23, xp=50)
enemy_pokemon1 = Pokemon("Abra", "psychic", 12)
enemy_pokemon2 = Pokemon("Bulbasaur", "grass")

won_battle = False  # Switch to True if battle is won
choice = ""

# Player chooses Pokemon
while choice != "1" and choice != "2":
    print(choice)
    print("Choose your Pokemon!")
    print(f"1) {pokemon1.name}")
    print(f"2) {pokemon2.name}\n")
    choice = input("(1 or 2) -> ")

    if choice == "1":
        player_pokemon = pokemon1
    elif choice == "2":
        player_pokemon = pokemon2
    else:
        print("Invalid, try again.")
    
print(f"\nYou chose {player_pokemon.name}!")

# Enemy chooses Pokemon
random_choice = randint(1, 2)

if random_choice == 1:
    enemy_pokemon = enemy_pokemon1
else:
    enemy_pokemon = enemy_pokemon2

print(f"Sleepy Mortimer chooses {enemy_pokemon.name}!\n")

# Begin Match
print(f"----- Match: {player_pokemon.name} vs. {enemy_pokemon.name}! -----\n")

while player_pokemon.hp > 0 and enemy_pokemon.hp > 0:
    print("*************")
    print(f"{player_pokemon.name}: {player_pokemon.hp}hp")
    print(f"{enemy_pokemon.name}: {enemy_pokemon.hp}hp\n")
    print("1) Attack")
    print("2) Rest")
    print("*************")
    choice = input("-> ").lower()

    # Player Turn
    if choice == "1" or choice == "attack":
        damage = player_pokemon.attack()
        print(f"{player_pokemon.name} does {damage} damage!")

        enemy_pokemon.hp -= damage

        if enemy_pokemon.hp <= 0:
            print(f"{enemy_pokemon.name} fainted!")
            won_battle = True
    elif choice == "2" or choice == "rest":
        player_pokemon.rest()
        print(f"{player_pokemon.name} rested and now has {player_pokemon.hp}hp.")
    else:
        print(
            f"You gave {player_pokemon.name} an incorrect command. They hesitate and lose a turn!")

    # Enemy Turn - They can only attack if they haven't fainted
    if enemy_pokemon.hp > 0:
        random_choice = randint(1, 4)  # 75% chance attack, 25% chance rest

        if random_choice <= 3:
            damage = enemy_pokemon.attack()
            print(f"{enemy_pokemon.name} does {damage} damage!")

            player_pokemon.hp -= damage

            if player_pokemon.hp <= 0:
                print(f"{player_pokemon.name} fainted!")
        else:
            enemy_pokemon.rest()
            print(f"{enemy_pokemon.name} rested and now has {enemy_pokemon.hp}hp.")

# See who won the battle
if won_battle:
    gained_xp = randint(5, 10)
    player_pokemon.xp += gained_xp
    print(f"You win! {pokemon1.name} gained {gained_xp}xp!")
else:
    print("You lose!")
