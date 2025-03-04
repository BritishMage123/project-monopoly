from scenes.events.scene_event import SceneEvent

class TaxesEvent(SceneEvent):
    def __init__(self, scene, player, space):
        super().__init__(scene, player, space)

    def on_land(self):
        """SCENE EVENT: Called when a player lands on this space"""
        print(f"{self.player.name} landed on a TAXES space.")
        print(f"{self.player.name} just lost ${self.space.pass_reward}")
        lost_amt = -1 * self.space.pass_reward

    def on_pass(self):
        """SCENE EVENT: Called when a player passes this space"""
        pass