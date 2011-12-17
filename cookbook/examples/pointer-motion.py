#!/usr/bin/env python3

from gi.repository import Clutter

def pointer_motion_cb(self, event):
    stage_x, stage_y = event.get_coords()
    actor_x, actor_y = self.transform_stage_point(stage_x, stage_y)

    print("pointer @ stage x %s, y %s; actor x %s, y %s" % (stage_x, stage_y, actor_x, actor_y))

    return True


stage = Clutter.Stage()
stage.set_size(400, 400)
stage.set_color(Clutter.Color.from_string("#333355"))
stage.connect("destroy", Clutter.main_quit)

rectangle = Clutter.Rectangle()
rectangle.set_color(Clutter.Color.from_string("#aa9900"))
rectangle.set_size(300, 300)
rectangle.set_position(50, 50)
rectangle.set_reactive(True)

stage.add_actor(rectangle)

rectangle.connect("motion-event", pointer_motion_cb)

stage.show()

Clutter.main()
