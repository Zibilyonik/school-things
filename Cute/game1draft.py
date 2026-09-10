from ursina import *
import importlib
import os

class Game(Ursina):
    def __init__(self):
        super().__init__()
        self.player_health = 100
        self.extensions = []

        self.player = Entity(model='cube', color=color.orange, scale=(1,2,1), position=(0,1,0))
        self.ground = Entity(model='plane', scale=(50,1,50), color=color.green)
        
        self.load_extensions()

    def load_extensions(self):
        # Load all extensions from extensions folder
        for file in os.listdir("extensions"):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = file[:-3]
                module = importlib.import_module(f"extensions.{module_name}")
                if hasattr(module, "setup"):
                    self.extensions.append(module)
                    module.setup(self)

    def input(self, key):
        if key == "w":
            self.player.y += 1
        if key == "s":
            self.player.y -= 1
        if key == "a":
            self.player.x -= 1
        if key == "d":
            self.player.x += 1

        for ext in self.extensions:
            if hasattr(ext, "on_input"):
                ext.on_input(self, key)

if __name__ == "__main__":
    game = Game()
    game.run()
