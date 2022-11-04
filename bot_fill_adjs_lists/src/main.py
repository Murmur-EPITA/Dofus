from os.path import exists
from ast import literal_eval
from re import match
from pynput.keyboard import Listener
from pynput.mouse import Controller
from time import sleep
import sys
from fileinput import input

from src.utils.CONSTANTS import *
from src.utils.ClickMouse import ClickMouse
from src.utils.Player import Player
from src.utils.WindowManagement import WindowManagement
from src.utils.tKinter import ask_pos
from src.utils.DIRECTION import Direction

from src.utils.write_resources import adjs, get_adjs

global x, y


class Main:
    direction: Direction = None
    adjsDir: str = 'adjs/adjs.py'

    def parse_adjs_file(self, line: str):
        if line == "":
            return
        # {'0,0': [(0, -1), (1, 0), None, (-1, 0)]}
        string = "^\t{ ('[0-9-]+,[0-9-]+'): (\[.*\]) }"
        lol = match(string, line)
        id = lol.group(1)
        liste = lol.group(2)
        res = literal_eval(liste)
        adjs[id] = res

    def write_adj(self, direction_to_disable: Direction):
        id = self.player.get_id()
        # new pos
        if id not in adjs.keys():
            adjs[id] = get_adjs(self.player.posX.pos, self.player.posY.pos)
            adjs[id][direction_to_disable] = None
            string = "\t{ '" + id + "': [" + str(adjs[id][0]) + ", " + str(adjs[id][1]) + ", " + str(adjs[id][2]) + \
                     ", " + str(adjs[id][3]) + "] }\n"
            if exists(self.adjsDir):
                print("New pos written to adjs file.")
                with open(self.adjsDir, 'a') as file:
                    file.write(string)
            else:
                print("Creating adjs file.")
                with open(self.adjsDir, 'w') as file:
                    file.write(string)
        # pos already written
        else:
            str_to_replace = "\t{ '" + id + "': "
            if adjs[id][direction_to_disable]:
                adjs[id][direction_to_disable] = None
                string = "\t{ '" + id + "': [" + str(adjs[id][0]) + ", " + str(adjs[id][1]) + ", " + str(adjs[id][2]) + \
                         ", " + str(adjs[id][3]) + "] }\n"

                text = open(self.adjsDir).read()
                new_text = '\n'.join(string if line.startswith(str_to_replace) else line for line in text.splitlines())
                open(self.adjsDir, 'w').write(new_text)
            else:
                tmp: list[str] = get_adjs(self.player.posX.pos, self.player.posY.pos)
                adjs[id][direction_to_disable] = tmp[direction_to_disable]
                string = "\t{ '" + id + "': [" + str(adjs[id][0]) + ", " + str(adjs[id][1]) + ", " + str(adjs[id][2]) + \
                         ", " + str(adjs[id][3]) + "] }\n"

                text = open(self.adjsDir).read()
                new_text = '\n'.join(string if line.startswith(str_to_replace) else line for line in text.splitlines())
                open(self.adjsDir, 'w').write(new_text)

    def __init__(self):
        def on_press(key: KeyCode | Key):
            if key == UP_ARROW:
                if self.direction == Direction.UP:
                    self.player.posY.pos -= 1
                self.click_thread.go_up(self.windowManagement.window.size, self.direction)
                self.direction = Direction.UP

            elif key == RIGHT_ARROW:
                if self.direction == Direction.RIGHT:
                    self.player.posX.pos += 1
                self.click_thread.go_right(self.windowManagement.window.size, self.direction)
                self.direction = Direction.RIGHT

            elif key == DOWN_ARROW:
                if self.direction == Direction.DOWN:
                    self.player.posY.pos += 1
                self.click_thread.go_down(self.windowManagement.window.size, self.direction)
                self.direction = Direction.DOWN

            elif key == LEFT_ARROW:
                if self.direction == Direction.LEFT:
                    self.player.posX.pos -= 1
                self.click_thread.go_left(self.windowManagement.window.size, self.direction)
                self.direction = Direction.LEFT

            elif key == BUTTON_POS:
                self.player.posX.pos, self.player.posY.pos = ask_pos()

            elif key == ADD_UP:
                self.write_adj(Direction.UP)

            elif key == ADD_RIGHT:
                self.write_adj(Direction.RIGHT)

            elif key == ADD_DOWN:
                self.write_adj(Direction.DOWN)

            elif key == ADD_LEFT:
                self.write_adj(Direction.LEFT)

            # here exit method is called and when
            # key is pressed it terminates auto clicker
            elif key == TERMINATE:
                listener.stop()

        if exists(self.adjsDir):
            with open(self.adjsDir, 'r') as file:
                line = file.readline()
                self.parse_adjs_file(line)

        self.windowManagement = WindowManagement()
        sleep(2)
        x, y = ask_pos()

        self.mouse = Controller()
        self.click_thread = ClickMouse(self.mouse)
        self.click_thread.start()

        self.player = Player(self.windowManagement, self.click_thread, x, y)

        with Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == '__main__':
    instance = Main()
