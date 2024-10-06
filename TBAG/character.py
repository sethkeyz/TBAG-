class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room.")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def get_conversation(self):
        return self.conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name}] says: {self.conversation}")
            return True
        else:
            print(f"{self.name} doesn't want to talk to you")
            return False

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight you")
        return True
    

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}.")
            return True
        else:
            print(f"{self.name} crushes you!")
            return False 
        
    def sleep(self):
        print(f"You have sent {self.name} to sleep.")

    def hug(self):
        print(f"{self.name} is your enemy, you can't hug him.")


class Friend(Character):

    def __init__(self, char_name, char_description, friendship_level):
        super().__init__(char_name, char_description)
        self.friendship_level = friendship_level
        

    def hug(self):
        if self.friendship_level >= 8:
            print(f"{self.name} gives you a warm hug back")
        elif 5 <= self.friendship_level < 8:
            print(f"{self.name} gives you a light hug.")
        else:
            print(f"{self.name} gives you an awkward hug.")

    def sleep(self):
        print(f"You can't put your friend {self.name} to sleep, that is not friend-like.")







        

        


        
    
    



