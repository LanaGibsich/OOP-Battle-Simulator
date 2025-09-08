import random
from goblin import Goblin
from hero import Hero
from boss import Boss


def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("SkibidiRizzlerOmegaAlphaSlayer!!!")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "pink") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0


    # Battle Loop 
    round = 0
    total=0


    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        round +=1
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        total += damage
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                total += damage
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    print("BOSS TIME!!!!!")
    #Create Boss
    boss = Boss("Skibidi Toilet", "red")
    while hero.is_alive() and boss.is_alive:
        damage = hero.strike()
        boss.take_damage(damage)
        damage = boss.attack()
        hero.receive_damage(damage)

        if hero.is_alive:
            print("WE BEAT THE BOSS")
        else:
            print("Your LOSE LOSER!!!")
        


    # Final tally of goblins defeated
    print("total Summary")
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print("Total Damage: " + str(damage))
    print("Rounds Cleared: " + str(round))

if __name__ == "__main__":
    main()
