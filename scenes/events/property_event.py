from scenes.events.scene_event import SceneEvent

class PropertyEvent(SceneEvent):
    def __init__(self, scene, player, space):
        super().__init__(scene, player, space)
        # To add entity such as a button or text box:
        # scene.add_entity(Entity: entity)

    def on_land(self):
        """SCENE EVENT: Called when a player lands on this space"""
        # handle property case
        print(f"{self.player.name} landed on a PROPERTY space.")
        print(f"Name: {self.space.property.get_name()} | Value: £{self.space.property.get_value()}")

    def on_pass(self):
        """SCENE EVENT: Called when a player passes this space"""
        pass