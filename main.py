import os
import time
import coordinates
import player
import keyboard

def render(frame: tuple):
    os.system("cls||clear")
    for element in frame:
        print(element)
print("Welcome! It's a simple console game made in Python. Recommend you to move inside all block that specific to environment")
while True:
    playermodel = input("Enter playermodel: ")
    if len(playermodel) > 1 or len(playermodel) < 1:
        os.system("cls||clear")
        print("Must be only 1 symbol!")
        continue
    player.script.model = playermodel
    break
while True:
    frame = list(player.script.current_location.location.frame)
    player_line = list(frame[player.script.position.y])
    player_line[player.script.position.x] = player.script.model
    frame[player.script.position.y] = ""
    for char in player_line:
        frame[player.script.position.y] += char
    render(tuple(frame))
    print("wasd to move")
    time.sleep(0.1)
    while True:
        if keyboard.is_pressed("w"):
            player.script.move(coordinates.move_direction["Up"])
        elif keyboard.is_pressed("s"):
            player.script.move(coordinates.move_direction["Down"])
        elif keyboard.is_pressed("a"):
            player.script.move(coordinates.move_direction["Left"])
        elif keyboard.is_pressed("d"):
            player.script.move(coordinates.move_direction["Right"])
        else:
            continue
        break