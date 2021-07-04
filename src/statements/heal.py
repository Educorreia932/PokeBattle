class Heal:
    def __init__(self, trainer, item):
        self.trainer = trainer

        if item == "Potion":
            self.level = 1

        elif item == "Super Potion":
            self.level = 2

        elif item == "Hyper Potion":
            self.level = 4
        
        elif item == "Max Potion":
            self.level = 8
