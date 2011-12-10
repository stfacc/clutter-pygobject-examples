#!/usr/bin/env python3

import cairo
import math
import time

from gi.repository import Clutter

SIZE_WIDTH, SIZE_HEIGHT = 300, 300

def cairo_draw(canvas, cr):
    # Rather than using GTimeDate (which I couldn't find), we'll use Python time.
    t = time.localtime()
    s = t.tm_sec * math.pi / 30.0
    m = t.tm_min * math.pi / 30.0
    h = t.tm_hour * math.pi / 6.0

    # Clear the texture contents, so that our drawing doesn't "stack."
    # If you don't call this, you'll notice lots of aliasing artifacts.
    canvas.clear()

    # Scale the modelview to the size of the surface.
    cr.scale(*canvas.get_surface_size())

    cr.set_line_cap(cairo.LINE_CAP_ROUND)
    cr.set_line_width(0.1)

    # The black rail that holds the seconds indicator.
    cr.set_source_rgb(0.0, 0.0, 0.0)
    cr.translate(0.5, 0.5)
    cr.arc(0.0, 0.0, 0.4, 0.0, math.pi * 2.0)
    cr.stroke()

    # The seconds indicator.
    cr.set_source_rgb(1.0, 1.0, 1.0)
    cr.move_to(0.0, 0.0)
    cr.arc(math.sin(s) * 0.4, -math.cos(s) * 0.4, 0.05, 0.0, math.pi * 2)
    cr.fill()

    # The minutes hand. Here we want to assign a Clutter-based color to a
    # cairo context, so we need to use Clutter wrappers.
    Clutter.cairo_set_source_color(
        cr,
        Clutter.Color.get_static(Clutter.StaticColor.CHAMELEON_DARK)
    )

    cr.move_to(0.0, 0.0)
    cr.line_to(math.sin(m) * 0.4, -math.cos(m) * 0.4)
    cr.stroke()

    # The hours hand.
    cr.move_to(0.0, 0.0)
    cr.line_to(math.sin(h) * 0.2, -math.cos(h) * 0.2)
    cr.stroke()

    return True

# This routine simply calls invalidate on the CairoTexture so that the draw
# event will be emitted.
def invalidate_clock(canvas):
    canvas.invalidate()

    return True

if __name__ == "__main__":
    # The stage is the "window", its where our actors play.
    stage = Clutter.Stage()

    stage.set_title("2D Clock")
    stage.set_color(Clutter.Color.get_static(Clutter.StaticColor.SKY_BLUE_LIGHT))
    stage.set_user_resizable(True)
    stage.set_size(SIZE_WIDTH, SIZE_HEIGHT)
    stage.connect("destroy", Clutter.main_quit)
    stage.show()

    # This is one way of setting up a constraint manually; we could also use
    # BindConstraint.new(), and do it in one (LONG) line.
    constraint = Clutter.BindConstraint()

    constraint.set_source(stage)
    constraint.set_coordinate(Clutter.BindCoordinate.SIZE)
    constraint.set_offset(0)

    # This is our Cairo drawing texture. We will eventually be passed a 
    # rendering context for this texture when responding to the "draw"
    # event...
    canvas = Clutter.CairoTexture(SIZE_WIDTH, SIZE_HEIGHT)
    
    canvas.add_constraint(constraint)
    canvas.set_auto_resize(True)
    canvas.connect("draw", cairo_draw)
    canvas.invalidate()

    # Finally, add the canvas and turn it loose.
    stage.add_actor(canvas)

    # This appears to actually call add_timeout_full()
    Clutter.threads_add_timeout(1, 1000, invalidate_clock, canvas)
    Clutter.main()

