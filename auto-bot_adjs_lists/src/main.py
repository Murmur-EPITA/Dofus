from os.path import exists
from ast import literal_eval
from re import match
from pynput.keyboard import Listener
from pynput.mouse import Controller
from time import sleep

from src.graph.graph import GraphMap
from src.utils.CONSTANTS import *
from src.utils.ClickMouse import ClickMouse
from src.utils.Player import Player
from src.utils.WindowManagement import WindowManagement
from src.tkinter_frames.position import ask_pos
from src.utils.DIRECTION import Direction
from src.graph.MAP import dofusMaps

from src.utils.write_resources import adjs, get_adjs

global x, y


class Main:
    adjsDir: str = 'adjs/adjs.py'

    def parse_adjs_file(self, line: str):
        if line == "":
            return
        # {'0,0': [(0, -1), (1, 0), None, (-1, 0)]}
        string = "^\t{ '([0-9-]+,[0-9-]+)': (\[.*\]) },"
        lol = match(string, line)
        id = lol.group(1)
        liste = lol.group(2)
        res = literal_eval(liste)
        adjs[id] = res

    def write_adj(self, direction_to_disable: Direction):
        id = self.player.get_id()
        # new pos
        print('adjs writ_ajd', adjs)
        print('keys', adjs.keys())
        if id not in adjs.keys():
            adjs[id] = get_adjs(self.player.posX.pos, self.player.posY.pos)
            adjs[id][direction_to_disable] = None
            string = "\t{ '" + id + "': [" + str(adjs[id][0]) + ", " + str(adjs[id][1]) + ", " + str(adjs[id][2]) + \
                     ", " + str(adjs[id][3]) + "] },\n"
            if exists(self.adjsDir):
                print("New pos ({id}) written to adjs file.".format(id=id))
                with open(self.adjsDir, 'a') as file:
                    file.write('\n' + string)
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
                         ", " + str(adjs[id][3]) + "] },"

                text = open(self.adjsDir).read()
                new_text = '\n'.join(string if line.startswith(str_to_replace) else line for line in text.splitlines())
                open(self.adjsDir, 'w').write(new_text)
            else:
                tmp: list[str] = get_adjs(self.player.posX.pos, self.player.posY.pos)
                adjs[id][direction_to_disable] = tmp[direction_to_disable]
                string = "\t{ '" + id + "': [" + str(adjs[id][0]) + ", " + str(adjs[id][1]) + ", " + str(adjs[id][2]) + \
                         ", " + str(adjs[id][3]) + "] },"

                text = open(self.adjsDir).read()
                new_text = '\n'.join(string if line.startswith(str_to_replace) else line for line in text.splitlines())
                open(self.adjsDir, 'w').write(new_text)

    def __init__(self):
        def on_press(key: KeyCode | Key):

            if key == UP_ARROW:
                self.click_thread.go_up(self.windowManagement.window.size, self.player)

            elif key == RIGHT_ARROW:
                self.click_thread.go_right(self.windowManagement.window.size, self.player)

            elif key == DOWN_ARROW:
                self.click_thread.go_down(self.windowManagement.window.size, self.player)

            elif key == LEFT_ARROW:
                self.click_thread.go_left(self.windowManagement.window.size, self.player)

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

            elif key == MOVE_WINDOW:
                self.windowManagement.move()

            elif key == TERMINATE:
                # self.click_thread.exit()
                listener.stop()

        if exists(self.adjsDir):
            print("Parsing existing adjs file.")
            with open(self.adjsDir, 'r') as file:
                for line in file.readlines():
                    self.parse_adjs_file(line)

        self.windowManagement = WindowManagement()
        sleep(1)
        x, y = ask_pos()

        self.mouse = Controller()
        self.click_thread = ClickMouse(self.mouse)
        # self.click_thread.start()

        self.player = Player(self.windowManagement, self.click_thread, GraphMap(maps=dofusMaps), x, y)

        with Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == '__main__':
    instance = Main()
