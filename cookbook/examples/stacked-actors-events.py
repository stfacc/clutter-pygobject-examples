#!/usr/bin/env python3

from gi.repository import Clutter

def pointer_motion_cb(self, event):
    stage_x, stage_y = event.get_coords()
    actor_x, actor_y = self.transform_stage_point(stage_x, stage_y)

    print("pointer on actor %s @ x %s, y %s" % (self.get_name(), actor_x, actor_y))

    return True


stage = Clutter.Stage()
stage.set_size(300, 300)
stage.set_color(Clutter.Color.from_string("#333355"))
stage.connect("destroy", Clutter.main_quit)

r1 = Clutter.Rectangle()
r1.set_color(Clutter.Color.from_string("red"))
r1.set_size(150, 150)
r1.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.X_AXIS, 0.25))
r1.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.Y_AXIS, 0.25))
r1.set_reactive(True)
r1.set_name("red")

r2 = Clutter.Rectangle()
r2.set_color(Clutter.Color.from_string("green"))
r2.set_size(150, 150)
r2.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.X_AXIS, 0.5))
r2.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.Y_AXIS, 0.5))
r2.set_reactive(True)
r2.set_name("green")

r3 = Clutter.Rectangle()
r3.set_color(Clutter.Color.from_string("blue"))
r3.set_size(150, 150)
r3.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.X_AXIS, 0.75))
r3.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.Y_AXIS, 0.75))
r3.set_opacity(125)
r3.set_name("blue")

stage.add(r1, r2, r3)

r1.connect("motion-event", pointer_motion_cb)
r2.connect("motion-event", pointer_motion_cb)

stage.show()

Clutter.main()
