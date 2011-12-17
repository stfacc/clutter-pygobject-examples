#!/usr/bin/env python3

from gi.repository import Clutter, Cogl, GObject

def convert_clutter_path_node_to_cogl_path(node, *args, **kwargs):
    knot = node.points[0]
    if node.type == Clutter.PathNodeType.MOVE_TO:
        Cogl.Path.move_to(knot.x, knot.y)
    elif node.type == Clutter.PathNodeType.LINE_TO:
        Cogl.Path.line_to(knot.x, knot.y)

def canvas_paint_cb(self, path):
    Cogl.Path.new()
    Cogl.set_source_color4ub(255, 255, 0, 255)
    path.foreach(convert_clutter_path_node_to_cogl_path, None)
    Cogl.Path.stroke()
    # Now we should call:
    #   GObject.signal_stop_emission_by_name(self, "paint")
    # but it segfaults. Because of this, the normal "paint" callback
    # for Clutter.Texture is called, which fills the texture with
    # some random color covering our path.
    # A workaround is use connect_after (see below), so at least the
    # random color is _under_ our path

def pointer_motion_cb(self, event, path):
    stage_x, stage_y = event.get_coords()
    x, y = self.transform_stage_point(stage_x, stage_y)

    print("motion; x %s, y %s" % (x, y))

    path.add_line_to(x, y)

    self.queue_redraw()

    return True

def pointer_enter_cb(self, event, path):
    stage_x, stage_y = event.get_coords()
    x, y = self.transform_stage_point(stage_x, stage_y)

    print("enter; x %s, y %s" % (x, y))

    path.add_move_to(x, y)

    self.queue_redraw()

    return True

path = Clutter.Path()

stage = Clutter.Stage()
stage.set_color(Clutter.Color.from_string("#333355"))
stage.set_size(400, 400)
stage.connect("destroy", Clutter.main_quit)

rect = Clutter.Rectangle()
rect.set_color(Clutter.Color.from_string("#aa9900"))
rect.set_size(300, 300)
rect.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.X_AXIS, 0.5))
rect.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.Y_AXIS, 0.5))

stage.add_actor(rect)

canvas = Clutter.Texture()
canvas.set_size(300, 300)
canvas.add_constraint(Clutter.AlignConstraint.new(rect, Clutter.AlignAxis.X_AXIS, 0))
canvas.add_constraint(Clutter.AlignConstraint.new(rect, Clutter.AlignAxis.Y_AXIS, 0))
canvas.set_reactive(True)

stage.add_actor(canvas)
canvas.raise_top()

canvas.connect("motion-event", pointer_motion_cb, path)
canvas.connect("enter-event", pointer_enter_cb, path)
# For the use of connect_after here see comment in canvas_paint_cb
canvas.connect_after("paint", canvas_paint_cb, path)

stage.show()

Clutter.main()
