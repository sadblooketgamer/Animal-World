# my pfp is fire
from scroll import Scroll
scroll = Scroll()
class Shop:
    def __init__(self, stats):
        self.stats = stats

    def merchant(self):
        scroll.slow_print(f"Hello there, {self.stats.Name}, Welcome to my shop.")
        scroll.slow_print(f"I can sell you armor, weapons, and potions.")

        scroll.slow_print(f"What do you want to buy? Armor for {self.stats.Armor * 2 + 10} Gold, "
              "a small healing potion for 200 Gold (Shealing), a large healing potion for 500 gold (Lhealing), "
              f"or a better weapon for {self.stats.Attack * 2 + 10} Gold? If you don't want anything, type no.")

        while True:
            buy = input("What do you want?: ")
            if buy in {"armor", "Armor"}:
                if self.stats.gold >= self.stats.Armor * 5 + 10:
                    self.stats.Armor += 10
                    self.stats.gold -= self.stats.Armor * 5 + 10
                    scroll.slow_print(f"Armor upgraded to {self.stats.Armor}. Remaining gold: {self.stats.gold}")
                else:
                    scroll.slow_print("You don't have enough gold for armor upgrade.")
            elif buy in {"Shealing", "SHealing", "shealing", "sHealing"}:
                count = int(input("How many? "))
                if self.stats.gold >= count * 200:
                    self.stats.spotsHeal += count
                    self.stats.gold -= count * 200
                    scroll.slow_print(f"Bought {count} small healing potions. Remaining gold: {self.stats.gold}")
                else:
                    scroll.slow_print("You don't have enough gold for small healing potions.")
            elif buy in {"Lhealing", "LHealing", "lhealing", "lHealing"}:
                count = int(input("How many? "))
                if self.stats.gold >= count * 500:
                    self.stats.lpotsHeal += count
                    self.stats.gold -= count * 500
                    scroll.slow_print(f"Bought {count} large healing potions. Remaining gold: {self.stats.gold}")
                else:
                    scroll.slow_print("You don't have enough gold for large healing potions.")
            elif buy.lower() == "no":
                scroll.slow_print("Then why are you wasting my time?")
            else:
                scroll.slow_print("Invalid input or you can't afford anything.")

            while True:
                continue_shopping = input("Do you want to continue shopping? (yes/no): ").lower()
                if continue_shopping == "no":
                    scroll.slow_print("Then why are you wasting my time?")
                    return
                elif continue_shopping == "yes":
                    break
                else:
                    scroll.slow_print("You didn't choose anything.")
#This is where the hometown goes lol
