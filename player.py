import coordinates as coords
import environment

# creating a class, because functions CAN'T work with variables from global scope normally.
class Player:
    def __init__(self):
        self.position = coords.Vector2(3, 2)

    model: str
    position: coords.Vector2

    # class for handling current location, reason same as was with Player
    class CurLocation:
        position: coords.Vector2 = coords.Vector2(0, 0)
        location: environment.Location

        def update(self, move_direction: coords.Vector2) -> bool:
            if self.position.x + move_direction.x < 0 or self.position.y + move_direction.y < 0:
                return False
            if self.position.x + move_direction.x > environment.locations_pos_limits.x or \
            self.position.y + move_direction.y > environment.locations_pos_limits.y:
                return False
            self.position.x += move_direction.x
            self.position.y += move_direction.y
            self.location = environment.gamemap[environment.locations_position[self.position.y][self.position.x]]
            return True

        def __init__(self):
            self.update(coords.Vector2(0, 1))

        def check_for_collide(self, position: coords.Vector2, one_way_noclip=False) -> bool:
            if self.location.colliders[position.y][position.x] == "#":
                return True
            elif self.location.colliders[position.y][position.x] == "<":
                if one_way_noclip:
                    return False
                else:
                    return True
            else:
                try:
                    self.location.interactables[int(self.location.colliders[position.y][position.x])].activate()
                    return True
                except ValueError:
                    return False

    current_location: CurLocation = CurLocation()

    def check_for_location_ends(self, move_direction: coords.Vector2) -> bool:
        position_save = coords.Vector2(self.position.x, self.position.y)
        if self.position.y + move_direction.y < 0 and move_direction.y == -1:  # w / up
            self.position.y = environment.map_limits.y
        elif self.position.y + move_direction.y > environment.map_limits.y and move_direction.y == 1:  # s / down
            self.position.y = 0

        elif self.position.x + move_direction.x < 0 and move_direction.x == -1:  # a / left
            self.position.x = environment.map_limits.x
        elif self.position.x + move_direction.x > environment.map_limits.x and move_direction.x == 1:  # d / right
            self.position.x = 0
        else:
            return False

        # if update() failed to execute (map end)
        if not self.current_location.update(move_direction):
            self.position = position_save
        # if check_for_collide found a collider inside player (except one_way blocks)
        elif self.current_location.check_for_collide(self.position, one_way_noclip=True):
            self.position = position_save
            self.current_location.update(coords.Vector2(move_direction.x * -1, move_direction.y * -1))

        return True

    def next_position(self, move_direction: coords.Vector2) -> coords.Vector2:
        return coords.Vector2(self.position.x + move_direction.x, self.position.y + move_direction.y)

    def move(self, move_direction: coords.Vector2):
        pos = self.next_position(move_direction)
        if self.check_for_location_ends(move_direction) or self.current_location.check_for_collide(pos):
            return
        self.position = pos

script: Player = Player()