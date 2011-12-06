#!/usr/bin/env python3

import sys
import math

from gi.repository import Clutter

class MyScript(Clutter.Script):
    def __init__(self, path):
        Clutter.Script.__init__(self)

        self.load_from_file(path)
        self.connect_signals(self)

    def on_button_press(self, actor, event):
        print("Button pressed!")

if __name__ == "__main__":
    if not Clutter.VERSION_S == "1.9.3":
        print("This example will not work until you're using Clutter 1.9.3+")

        sys.exit(0)

    stage = Clutter.Stage()

    stage.set_title("State Script")
    stage.set_user_resizable(True)
    stage.connect("destroy", Clutter.main_quit)

    script = MyScript("../data/test-script-signals.json")
    
    stage.add_actor(script.get_object("button"))
    stage.show_all()

    Clutter.main()

