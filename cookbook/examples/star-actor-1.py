#!/usr/bin/env python3

from gi.repository import Clutter, Cogl

class StarActor(Clutter.Actor):
    def __init__(self):
        Clutter.Actor.__init__(self)

        self.set_reactive(True)

        # set default color to black
        color = Clutter.Color.from_string("#000")
        self.set_color(color)

    def set_color(self, color):
        self._color = color

    def do_paint(self):
        allocation = self.get_allocation_box()
        width, height = allocation.get_size()

        color = self._color

        tmp_alpha = self.get_paint_opacity() * color.alpha / 255

        Cogl.Path.new()
        Cogl.set_source_color4ub(color.red, color.green, color.blue, tmp_alpha)

        Cogl.Path.move_to(width * 0.5, 0)
        Cogl.Path.line_to(width, height * 0.75)
        Cogl.Path.line_to(0, height * 0.75)
        Cogl.Path.move_to(width * 0.5, height)
        Cogl.Path.line_to(0, height * 0.25)
        Cogl.Path.line_to(width, height * 0.25)
        Cogl.Path.line_to(width * 0.5, height)

        Cogl.Path.fill()

    def do_pick(self, pick_color):
        if not self.should_pick_paint():
            return

        allocation = self.get_allocation_box()
        width, height = allocation.get_size()

        Cogl.Path.new()
        Cogl.set_source_color4ub(pick_color.red, pick_color.green, pick_color.blue, pick_color.alpha)

        Cogl.Path.move_to(width * 0.5, 0)
        Cogl.Path.line_to(width, height * 0.75)
        Cogl.Path.line_to(0, height * 0.75)
        Cogl.Path.move_to(width * 0.5, height)
        Cogl.Path.line_to(0, height * 0.25)
        Cogl.Path.line_to(width, height * 0.25)
        Cogl.Path.line_to(width * 0.5, height)

        Cogl.Path.fill()


def clicked_cb(self, *args, **kwargs):
    print("click!")

if __name__ == "__main__":
    stage = Clutter.Stage()

    stage.set_title("star-actor")
    stage.connect("destroy", Clutter.main_quit)

    star_actor = StarActor()
    star_actor.set_size(100, 100)

    color = Clutter.Color.from_string("yellow")
    star_actor.set_color(color)

    click_action = Clutter.ClickAction()
    click_action.connect("clicked", clicked_cb)
    star_actor.add_action(click_action)

    stage.add_actor(star_actor)
    stage.show_all()

    Clutter.main()
