#!/usr/bin/env python3

from gi.repository import Clutter

def key_press_cb(self, event):
    state = event.get_state()
    keyval = event.get_key_symbol()

    shift_pressed = False
    ctrl_pressed = False
    if state & Clutter.ModifierType.SHIFT_MASK:
        shift_pressed = True
    if state & Clutter.ModifierType.CONTROL_MASK:
        ctrl_pressed = True

    if keyval == Clutter.KEY_Up:
        if shift_pressed and ctrl_pressed:
            print("Up and shift and control pressed")
        elif shift_pressed:
            print("Up and shift pressed")
        elif ctrl_pressed:
            print("Up and control pressed")
        else:
            print("Up pressed")
        return True

    return False

def stage_key_press_cb(self, event):
    print("Something else pressed")

stage = Clutter.Stage()
stage.connect("destroy", Clutter.main_quit)

rect = Clutter.Rectangle()
rect.set_size(100, 100)
rect.set_color(Clutter.Color.from_string("black"))
rect.connect("key-press-event", key_press_cb)

stage.set_key_focus(rect)
stage.connect("key-press-event", stage_key_press_cb)

stage.add(rect)
stage.show()

Clutter.main()
