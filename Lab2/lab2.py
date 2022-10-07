
import keyboard
import sys
sys.path.append(
    "C:/Users/Aicha/Desktop/Lab2/Lab2/x64/Release")

import Lab2

quitter = False


def stop():
    Lab2.Quitter()
    global quitter
    quitter = True


keyboard.on_press_key("q", lambda _: stop())
keyboard.on_press_key("p", lambda _: Lab2.Play_Pause_video())
keyboard.on_press_key("r", lambda _: Lab2.Repeat())
keyboard.on_press_key("a", lambda _: Lab2.Accelerate())

Lab2.Start("", "C:/Users/Aicha/Desktop/Lab2/Lab2/Example.avi")

while(not quitter):
    pass


keyboard.unhook_all()