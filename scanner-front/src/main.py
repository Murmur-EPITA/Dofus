from pynput.mouse import Controller
from src.HDV.HDV import start_hdv

# launch dofus launcher
# click on hdv

if __name__ == '__main__':
    mouse = Controller()
    start_hdv(mouse)
