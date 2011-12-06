#!/usr/bin/env python3

from gi.repository import Clutter, GObject

def move_up_cb():
    print("Up pressed")

def move_up_shift_control_cb():
    print("Up and shift and control pressed")

def key_press_cb(actor, event):
    pool = Clutter.BindingPool.find(GObject.type_name(actor))
    return pool.activate(event.get_key_symbol(), event.get_state(), actor)


stage = Clutter.Stage()
stage.connect("destroy", Clutter.main_quit)

stage.connect("key-press-event", key_press_cb)

# WARNING: the original cookbook example uses here Clutter.BindingPool.get_for_class()
# which is not yet working in PyGObject
binding_pool = Clutter.BindingPool.new(GObject.type_name(stage))

binding_pool.install_action("move-up",        # indentifier
                            Clutter.KEY_Up,   # up arrow pressed
                            0,                # no modifiers pressed
                            move_up_cb,
                            None)

binding_pool.install_action("move-up-shift-control",
                            Clutter.KEY_Up,
                            Clutter.ModifierType.SHIFT_MASK | Clutter.ModifierType.CONTROL_MASK,
                            move_up_shift_control_cb,
                            None)

stage.show()

Clutter.main()
