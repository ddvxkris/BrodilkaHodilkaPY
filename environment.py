import getpass
import coordinates

class Location:
    frame: list
    colliders: list
    interactables: tuple

    def __init__(self, frame: list, colliders: list, interactables: tuple):
        self.frame = frame
        self.colliders = colliders
        self.interactables = interactables

# displays message to a user.
class Message:
    text: str

    def activate(self):
        # code duplicated from main.render(), but it's most simple way to avoid circular import.
        import os
        os.system("cls||clear")
        print(self.text)
        # using getpass() to hide chars from user
        getpass.getpass("Hit ENTER to continue... ")

    def __init__(self, text: str):
        self.text = text
# displays a location's frame
class CurrentFrame:
    index: int

    def __init__(self, location_index: int):
        self.index = location_index

    def activate(self):
        # code duplicated from main.render(), but it's most simple way to avoid circular import.
        import os
        os.system("cls||clear")
        for element in gamemap[self.index].frame:
            print(element)
        # using getpass() to hide chars from user
        getpass.getpass("Hit ENTER to continue... ")

# edits location by index
class Lever(Message):
    activated: bool
    new_frame: list
    new_colliders: list
    old_frame: list = []
    old_colliders: list = []
    index: int

    def __init__(self, new_frame: list, new_colliders: list, index: int):
        super(Lever, self).__init__("Something clicked...")
        self.new_frame = new_frame
        self.new_colliders = new_colliders
        self.index = index
        self.activated = False

    def activate(self):
        if self.old_colliders == [] or self.old_frame == []:
            self.old_frame = gamemap[self.index].frame
            self.old_colliders = gamemap[self.index].colliders

        if not self.activated:
            self.activated = True
            gamemap[self.index].frame = self.new_frame
            gamemap[self.index].colliders = self.new_colliders
        else:
            self.activated = False
            gamemap[self.index].frame = self.old_frame
            gamemap[self.index].colliders = self.old_colliders
        super(Lever, self).activate()

# indexes to map locations (0 location = player spawn)
locations_position: tuple = (7, 5, 4), \
                            (0, 3, 2), \
                            (1, 2, 6)
# if you are making custom locations, don't forget to change this.
locations_pos_limits: coordinates.Vector2 = coordinates.Vector2(2, 2)
map_limits: coordinates.Vector2 = coordinates.Vector2(6, 4)
gamemap: tuple = (
    Location(
        ["#######", "#     #", "#     #", "#     #", "#######"],  # frame
        ["<<<<<<<", "#     #", "#     #", "#     #", "#     #"],  # colliders
        (  # interactables

        )
    ),
    Location(
        ["#     #", "#      ", "#      ", "#      ", "#######"],
        ["#     #", "#      ", "#      ", "#      ", "#######"],
        (

        )),
    Location(
        ["#     #", "      #", "      #", "      #", "#######"],
        ["#     #", "      #", "      #", "      #", "#######"],
        (

        )),
    Location(
        ["#######", "#  |  #", "#     #", "#     #", "#     #"],
        ["<<<<<<<", "#  0  #", "#     #", "#     #", "#     #"],
        (
            Lever(["#######", "#  /   ", "#      ", "#      ", "#     #"],
                  ["<<<<<<<", "#  0   ", "#      ", "#      ", "#     #"],
                  3),
        )),
    Location(
        ["#######", "      #", "      #", "#     #", "#     #"],
        ["#######", "      #", "      #", "#     #", "#     #"],
        (

        )),
    Location(
        ["#  %  #", "#      ", "#      ", "#  &  #", "#-----#"],
        ["   1  #", "#      ", "#      ", "#  0  #", "#     #"],
        (
            CurrentFrame(3), Lever(["#     #", "      #", "      #", "      #", "#-----#"],
                                   ["#     #", "      #", "      #", "      #", "#     #"], 2),
        )),
    Location(
        ["#     #", "#     #", "#     #", "#  =  #", "#######"],
        ["#     #", "#     #", "#     #", "#  0  #", "#######"],
        (
            Message("You walked through entire game! but only if you found 9th location..."),
        )),
    Location(
        ["+-----+", "|ddvx_|", "|kris.|", "|BH.PY|", "+--#--+"],
        ["######<", "       ", "       ", "       ", "   0   "],
        (
            Message("BrodilkaHodilkaPY by ddvx_kris\nOriginal console game was written in C#, now it's PYthon.\nLearned Python for 3 days before making this\nIt took me 2 days to create this\nYou found 9th location!"),
        )),
)