#!/usr/bin/env python3

from gi.repository import Clutter, Pango

def pointer_enter_cb(self, event, state):
    state.set_state("fade-in")
    return True

def pointer_leave_cb(self, event, state):
    state.set_state("fade-out")
    return True


stage = Clutter.Stage()
stage.set_color(Clutter.Color.from_string("#333355"))
stage.set_title("btn")
stage.connect("destroy", Clutter.main_quit)

layout = Clutter.BinLayout.new(Clutter.BinAlignment.FILL, Clutter.BinAlignment.FILL)

box = Clutter.Box()
box.set_layout_manager(layout)
box.set_position(25, 25)
box.set_reactive(True)
box.set_size(100, 30)

# background for the button
rect = Clutter.Rectangle()
rect.set_color(Clutter.Color.from_string("#aa9900"))
box.add_actor(rect)

# text for the button
text = Clutter.Text.new_full("Sans 10pt", "Hover me", Clutter.Color.from_string("white"))
text.set_line_alignment(Pango.Alignment.CENTER)

# NB don't set the height, so the actor assumes the height of the text;
# then when added to the bin layout, it gets centred on it;
# also if you don't set the width, the layout goes gets really wide;
# the 10pt text fits inside the 30px height of the rectangle
text.set_width(100)
layout.add(text, Clutter.BinAlignment.CENTER, Clutter.BinAlignment.CENTER)

# animations
transitions = Clutter.State()
transitions.set_key(None, "fade-out",
                    box, "opacity", Clutter.AnimationMode.LINEAR, 180)

# NB you can't use an easing mode where alpha > 1.0 if you're
# animating to a value of 255, as the value you're animating
# to will possibly go > 255
transitions.set_key(None, "fade-in",
                    box, "opacity", Clutter.AnimationMode.LINEAR, 255)

transitions.set_duration(None, None, 200)
transitions.warp_to_state("fade-out")

box.connect("enter-event", pointer_enter_cb, transitions)
box.connect("leave-event", pointer_leave_cb, transitions)

stage.add_constraint(Clutter.BindConstraint.new(box, Clutter.BindCoordinate.HEIGHT, 50.0))
stage.add_constraint(Clutter.BindConstraint.new(box, Clutter.BindCoordinate.WIDTH, 50.0))

stage.add_actor(box)
stage.show()

Clutter.main()
