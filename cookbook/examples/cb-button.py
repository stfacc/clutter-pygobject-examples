#!/usr/bin/env python3

from gi.repository import Clutter, Pango, GObject

# We're demonstrating a very simple Actor subclass here, whose purpose is to be as
# close to the C-based cookbook example as possible. Ideally, you wouldn't actually
# derive from Actor directly, but something more "intelligent" like Clutter.Box
# itself (rather than hiding it like we've done).
#
# However, we demonstrate such usage here because it CAN be educational.
#
# One of the most important bits of information to take away from this code is how
# we are required to prefix the "builtin" method overrides with the string "do_".
# The EXACT reasons for this are not entirely known to me, but it has been this way
# since the days of pygtk, and honored thusly.
class CbButton(Clutter.Actor):
    # Define a "clicked" signal that our custom actor can emit.
    __gsignals__ = {
        "clicked": (GObject.SIGNAL_RUN_LAST, None, ())
    }

    # Demonstrate defining a GObject.property member data for this object.
    def set_text(self, value):
        self.__text = value

        self.__label.set_text(value)
    
    def get_text(self):
        return self.__text
    
    text = GObject.property(type=str, setter=set_text, getter=get_text)

    def __init__(self):
        Clutter.Actor.__init__(self)

        self.__text  = None
        self.__click = Clutter.ClickAction()
        self.__child = Clutter.Box()
        self.__label = Clutter.Text()
        
        self.__label.set_line_alignment(Pango.Alignment.CENTER)
        self.__label.set_ellipsize(Pango.EllipsizeMode.END)

        self.__click.connect("clicked", self.clicked)

        self.__child.set_layout_manager(Clutter.BinLayout.new(
            Clutter.BinAlignment.CENTER,
            Clutter.BinAlignment.CENTER
        ))
        self.__child.add_actor(self.__label)
        self.__child.set_parent(self)

        self.set_reactive(True)
        self.add_action(self.__click)

    def set_background_color(self, color):
        self.__child.set_color(color)

    def set_text_color(self, color):
        self.__label.set_color(color)

    def clicked(self, *args, **kargs):
        self.emit("clicked")

    def do_get_preferred_width(self, height):
        w = [v + 20.0 for v in self.__child.get_preferred_width(height)]
        
        print("get_preferred_width (for height %s): %s" % (height, w))

        # BUG: Returning the listcomp from above directly will crash Python!
        return tuple(w)

    def do_get_preferred_height(self, width):
        h = [v + 20.0 for v in self.__child.get_preferred_height(width)]

        print("get_preferred_height (for width %s): %s" % (width, h))

        # BUG: Returning the listcomp from above directly will crash Python!
        return tuple(h)

    def do_allocate(self, box, flags):
        print("allocate: %s %s %s %s" % (box.x1, box.y1, box.x2, box.y2))
        
        child_box    = Clutter.ActorBox()
        child_box.x1 = 0
        child_box.y1 = 0
        child_box.x2 = box.get_width()
        child_box.y2 = box.get_height()
        
        self.__child.allocate(child_box, flags)

        Clutter.Actor.do_allocate(self, box, flags)

    def do_paint(self):
        self.__child.paint()

def on_click(button):
    if button.text == "hello":
        button.text = "world"

    else:
        button.text = "hello"

if __name__ == "__main__":
    stage = Clutter.Stage()

    stage.set_title("cb-button")
    stage.set_color(Clutter.Color.from_string("#333355"))
    stage.connect("destroy", Clutter.main_quit)

    button = CbButton()
    
    button.set_text("hello")
    button.set_text_color(Clutter.Color.from_string("#ffffff"))
    button.set_background_color(Clutter.Color.from_string("#888800"))
    button.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.X_AXIS, 0.5))
    button.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.Y_AXIS, 0.5))
    button.connect("clicked", on_click)

    stage.add_actor(button)
    stage.show()

    Clutter.main()

