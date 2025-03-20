
class SceneEvent():
    # the parrent class for  what happens when a player lands on a place on the board and when the player passes it
    def __init__(self, scene, player, space):
        self.scene = scene
        self.player = player
        self.space = space

    def on_land(self):
        pass

    def on_pass(self):
        pass