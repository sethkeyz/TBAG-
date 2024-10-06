from character import Enemy

dave = Enemy("Dave", "A smelly green zombie")

dave.describe()

dave.set_conversation("Hi i'm Dave and i won't eat you")
dave.talk()

dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input("Enter item here: ")
dave.fight(fight_with)





