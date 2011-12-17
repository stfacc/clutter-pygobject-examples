#!/usr/bin/env python3

from gi.repository import Clutter, Cogl

class Canvas(Clutter.Texture):
    def __init__(self):
        Clutter.Texture.__init__(self)

        self._path = Clutter.Path()

        self.connect("motion-event", self.pointer_motion_cb)
        self.connect("enter-event", self.pointer_enter_cb)
        self.set_reactive(True)

    def convert_clutter_path_node_to_cogl_path(self, node, *args, **kwargs):
        knot = node.points[0]
        if node.type == Clutter.PathNodeType.MOVE_TO:
            Cogl.Path.move_to(knot.x, knot.y)
        elif node.type == Clutter.PathNodeType.LINE_TO:
            Cogl.Path.line_to(knot.x, knot.y)

    def do_paint(self):
        Cogl.Path.new()
        Cogl.set_source_color4ub(255, 255, 0, 255)
        self._path.foreach(self.convert_clutter_path_node_to_cogl_path, None)
        Cogl.Path.stroke()

    def pointer_motion_cb(self, actor, event):
        stage_x, stage_y = event.get_coords()
        x, y = self.transform_stage_point(stage_x, stage_y)

        print("motion; x %s, y %s" % (x, y))

        self._path.add_line_to(x, y)

        self.queue_redraw()

        return True

    def pointer_enter_cb(self, actor, event):
        stage_x, stage_y = event.get_coords()
        x, y = self.transform_stage_point(stage_x, stage_y)

        print("enter; x %s, y %s" % (x, y))

        self._path.add_move_to(x, y)

        self.queue_redraw()

        return True


if __name__ == "__main__":
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

    canvas = Canvas()
    canvas.set_size(300, 300)
    canvas.add_constraint(Clutter.AlignConstraint.new(rect, Clutter.AlignAxis.X_AXIS, 0))
    canvas.add_constraint(Clutter.AlignConstraint.new(rect, Clutter.AlignAxis.Y_AXIS, 0))

    stage.add_actor(canvas)
    canvas.raise_top()

    stage.show()

    Clutter.main()
