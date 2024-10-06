from room import Room
from character import Enemy
from character import Friend
from item import Item
from room import Door

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

dave = Enemy("Dave", "Dave is a smelly zombie.")

dave.set_conversation("Hi i'm Dave and i won't eat you")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

st_pierre = Enemy("St-Pierre", "St-Pierre is the best fighter in the game.")

st_pierre.set_conversation("Hi, I am St-Pierre, and i am the most complete fighter you'll see.")
st_pierre.set_weakness("sword")
ballroom.set_character(st_pierre)

john = Friend("John", "John is my best friend", 10)

john.set_conversation("Hello mate, so good to see you.")
kitchen.set_character(john)


kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom.set_description("A glass room with a shiny wooden floor.")
dining_hall.set_description("A large room with a long table and decorations.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

key = Item()
key.set_name("key")
key.set_description("Key that unlocks the door.")

kitchen.set_item(key)

inventory = []

door = Door()
ballroom.set_door(door)




current_room = dining_hall

while True:
    print("\n")
    current_room.get_details()
    
    if hasattr(current_room, 'item') and current_room.get_item() is not None:
        item = current_room.get_item()
        print(f"There is a {item.get_name()} here.")
        take_item = input(f"Do you want to take the {item.get_name()}? (yes/no): ").lower()
        if take_item == 'yes':
            inventory.append("key")
            print(f"You picked up the {item.get_name()}.")
            current_room.set_item(None)  # Remove the item from the room after collection
        else:
            print(f"You left the {item.get_name()} in the room.")

    if hasattr(current_room, 'door') and current_room.get_door() is not None:
        print(f"The door to the {current_room.name} is locked.")
        open_door = input("Would you like to unlock the door? (yes/no)   ").lower()
        if open_door == "yes":
            if "key" in inventory:
                print("You have unlocked the door.")
            else:
                print("You don't have they key to unlock the door. Game Over.")
                break
        elif open_door == "no":
            print("Game over.")
            break
            





    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        
    
    command = input("Which way would you like to go (or type 'talk', 'fight', 'sleep', 'hug', or 'quit'):  ").lower()

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            print("Hello, who goes there?")
            print(inhabitant.talk())
        else:
            print("There is no one here to talk to.")

    elif command == "fight":
        if inhabitant is not None:
            combat_item = input("What item would you like to fight with?   ").lower()
            fight_result = inhabitant.fight(combat_item)
            print(fight_result)
            if fight_result == False:
                break
        else:
            print("There is no one here to fight.")

                #  and current_room.door.is_locked
        
    elif command == "sleep":
        if inhabitant is not None:
            inhabitant.sleep()
        else: 
            print("There is no one here to put to sleep.")

    elif command == 'hug':
        if inhabitant is not None:
            inhabitant.hug()
        else:
            print("There is no one here to hug.")
        
    else:
        if command == "quit":
            break







    

            

 
            






    







    
    








