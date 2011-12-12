#!/usr/bin/env python3
# Example by: Jeremy Moles <cubicool@gmail.com>

import sys
import math

from gi.repository import Clutter, Cogl

SIZE_WIDTH, SIZE_HEIGHT = 300, 300

class Arrow(Clutter.Actor):
    def __init__(self, w, h):
        Clutter.Actor.__init__(self)

        self.set_size(w, h)

    def do_paint(self):
        w, h = self.get_allocation_box().get_size()

        Cogl.scale(w, h, 1.0)
        Cogl.Path.new()
        Cogl.Path.move_to(0.0, 1.0)
        Cogl.Path.line_to(0.5, 0.0)
        Cogl.Path.line_to(1.0, 1.0)
        Cogl.Path.curve_to(1.0, 0.75, 0.0, 0.75, 0.0, 1.0)
        Cogl.set_source_color4ub(100, 150, 200, 255)
        Cogl.Path.fill()

    def move_towards(self, x, y):
        self.animate(Clutter.AnimationMode.EASE_OUT_SINE, 250, "x", x)
        self.animate(Clutter.AnimationMode.EASE_OUT_SINE, 250, "y", y)

    def point_towards(self, px, py):
        def dotproduct(v1, v2):
            return sum((a * b) for a, b in zip(v1, v2))

        def length(v):
            return math.sqrt(dotproduct(v, v))

        def angle(v1, v2):
            return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

        v1  = 0.0, 1.0
        v2  = px, py
        l2  = length(v2)
        n2  = v2[0] / l2, v2[1] / l2
        deg = angle(v1, n2) * (180.0 / math.pi)

        if px < 0.0:
            deg = -deg

        self.set_z_rotation_from_gravity(deg, Clutter.Gravity.CENTER)

def motion_event(stage, event, arrow):
    x, y = arrow.get_position()
    w, h = arrow.get_size()
    
    arrow.point_towards(event.x - (x + (w / 2.0)), -event.y + (y + (h / 2.0)))

def press_event(stage, event, arrow):
    arrow.move_towards(event.x, event.y)

if __name__ == "__main__":
    print("Using Clutter version: %s" % Clutter.VERSION_S)

    stage = Clutter.Stage()
    arrow = Arrow(30, 30)

    arrow.set_position(SIZE_WIDTH / 2.0, SIZE_HEIGHT / 2.0)

    # arrow.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.Y_AXIS, 0.5))
    # arrow.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.X_AXIS, 0.5))

    stage.set_title("Arrow Follow")
    stage.set_color(Clutter.Color.from_string("#acf"))
    stage.set_size(SIZE_WIDTH, SIZE_HEIGHT)
    stage.connect("destroy", Clutter.main_quit)
    stage.connect("motion-event", motion_event, arrow)
    stage.connect("button-press-event", press_event, arrow)

    stage.add_actor(arrow)
    stage.show()

    Clutter.main()

