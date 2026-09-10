# extensions/bonus.py
def setup(game):
    print("Bonus extension loaded!")

def on_game_start(game):
    print("A mysterious voice whispers: 'Good luck, adventurer.'")

def on_explore(game):
    print("You found a hidden potion! +5 health")
    game.health += 5
