import pygame
import time
from entities.entity import Entity
from corporation import Corporation

class GameAgent(Entity, Corporation):
    def __init__(self, name, starting_space, token_path):
        self.current_space = starting_space
        starting_pos = starting_space.get_coordinates()
        Entity.__init__(self, starting_pos[0][0], starting_pos[0][1], 60, 60, override_offsets=True)
        Corporation.__init__(self, name)

        # Load player token image
        self.token = pygame.image.load(token_path)

        # Movement animation variables
        self.moving = False
        self.move_path = []  # List of spaces to jump through
        self.move_delay = 200  # Time in ms between jumps
        self.last_move_time = 0  # Track time between jumps

    def get_current_space(self):
        if self.moving:
            return self.move_path[-1] # if middle of animation, return the final destination
        return self.current_space

    def set_current_space(self, space):
        self.current_space = space

    def jump_spaces(self, num=1):
        self.move_path = []  # Clear any existing path
        next_space = self.current_space
        
        for _ in range(num):
            next_space = next_space.next_space
            self.move_path.append(next_space)  # Store space objects
        
        self.moving = True  # Start movement animation
        self.last_move_time = pygame.time.get_ticks()  # Reset move timer

        return self.get_current_space()

    def update(self):
        # Teleports the player from space to space at a set time interval. 
        if self.moving and self.move_path:
            now = pygame.time.get_ticks()
            
            if now - self.last_move_time >= self.move_delay:
                # Move to the next space in the path
                next_space = self.move_path.pop(0)
                
                # Update space
                self.set_current_space(next_space)

                self.last_move_time = now  # Reset timer

            # If finished moving, stop animation
            if not self.move_path:
                self.moving = False

    def render(self, screen):
        """Draws the player's token."""
        pos = self.current_space.get_coordinates()
        super().set_pos(pos[2][0], pos[2][1])
        self.token = pygame.transform.scale(self.token, (self.rect.width, self.rect.height))
        screen.blit(self.token, self.rect)