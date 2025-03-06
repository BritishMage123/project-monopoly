from scenes.events.scene_event import SceneEvent
from ui.text_label import TextLabel
from ui.button import Button
import time

"""
BUYING PROPERTIES:
Whenever you land on an unowned property you may buy that property from the Bank at its printed price.
If you do not wish to buy the property, the Bank sells it through auction to the highest bidder.
The high bidder pays the Bank the amount of the bid in cash and receives the property.

Any player, including the one who declined the option to buy it at the printed price, may bid.
Bidding may start at any price.
"""

class PropertyEvent(SceneEvent):
    def __init__(self, scene, player, space):
        super().__init__(scene, player, space)

        self.property = self.space.property

        self.property_name = TextLabel(scene.screen_width * 0.5, scene.screen_height * 0.3, space.text)
        self.property_value = TextLabel(scene.screen_width * 0.5, scene.screen_height * 0.35,
                                        f"£{self.property.get_value()}")
        self.query = TextLabel(scene.screen_width * 0.5, scene.screen_width * 0.4,
                               f"{player.name}, what do you want to do?")
        self.buy_button = Button(scene.screen_width * 0.38, scene.screen_height * 0.5,
                                 "BUY", self.buy_property, width=100, button_color="GREEN")
        self.auction_button = Button(scene.screen_width * 0.6, scene.screen_height * 0.5,
                                 "SEND TO AUCTION", self.auction_property, width=230)
        if self.property.owner:
            self.tax_query = TextLabel(scene.screen_width * 0.5, scene.screen_height * 0.4,
                                f"{self.property.owner.name} owns this property.")
        else:
            self.tax_query = None
        self.tax_button = Button(scene.screen_width * 0.5, scene.screen_height * 0.5,
                                 "PAY TAX", self.pay_tax)

    def on_land(self):
        """SCENE EVENT: Called when a player lands on this space"""
        self.scene.add_entity(self.property_name)

        if not self.property.owner:
            self.scene.add_entity(self.query)
            self.scene.add_entity(self.buy_button)
            self.scene.add_entity(self.auction_button)
            self.scene.add_entity(self.property_value)
        else:
            self.scene.add_entity(self.tax_query)
            self.scene.add_entity(self.tax_button)

    def on_pass(self):
        """SCENE EVENT: Called when a player passes this space"""
        pass

    def pay_tax(self):
        self.clear_ui()

        self.scene.next_turn()
    
    def auction_property(self):
        # Remove the UI
        self.clear_ui()

        # Trigger next turn
        self.scene.next_turn() # ALWAYS NEED TO DO THIS ONCE DONE

    def buy_property(self):
        # Set ownership
        self.property.owner = self.player

        # Remove the UI
        self.clear_ui()

        # Trigger next turn
        self.scene.next_turn() # ALWAYS NEED TO DO THIS ONCE DONE

    def clear_ui(self):
        self.scene.remove_entity(self.property_name)
        self.scene.remove_entity(self.property_value)
        self.scene.remove_entity(self.query)
        self.scene.remove_entity(self.buy_button)
        self.scene.remove_entity(self.tax_query)
        self.scene.remove_entity(self.tax_button)
        self.scene.remove_entity(self.auction_button)