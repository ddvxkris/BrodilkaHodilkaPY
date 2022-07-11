# point in 2D space, base for all coordinated objects
class Vector2:
    x: int
    y: int

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# direction for movement, must be summed at using.
move_direction: dict = {
    "Up": Vector2(0, -1),
    "Down": Vector2(0, 1),
    "Left": Vector2(-1, 0),
    "Right": Vector2(1, 0),
}