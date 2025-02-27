from ui.ui_element import UIElement

class TextLabel(UIElement):
    def __init__(self, x, y, text, width=200, height=50, font_size=32, centered=True):
        super().__init__(x, y, width, height, text=text, font_size=font_size, centered=centered)

    def render(self, screen):
        """Only renders text, no borders or background."""
        self.render_text(screen)
