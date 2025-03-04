from scenes.events.scene_event import SceneEvent

class JailEvent(SceneEvent):
    def __init__(self, scene, player, space):
        # Add entities here with self.scene.add_entity()
        super().__init__(scene, player, space)

    def on_land(self):
        """SCENE EVENT: Called when a player lands on this space"""
        # handle jail case
        print(f"{self.player.name} landed on a JAIL space.")

    def on_pass(self):
        """SCENE EVENT: Called when a player passes this space"""
        pass