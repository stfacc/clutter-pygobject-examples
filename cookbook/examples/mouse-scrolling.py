#!/usr/bin/env python3

import sys
from gi.repository import GObject, Clutter

STAGE_HEIGHT = 300
STAGE_WIDTH = STAGE_HEIGHT
SCROLL_AMOUNT = (STAGE_HEIGHT * 0.125)

def scroll_event_cb(self, event, scrollable):
    viewport_height = self.get_height()
    scrollable_height = scrollable.get_height()

    # no need to scroll if the scrollable is shorter than the viewport
    if scrollable_height < viewport_height:
        return True

    y = scrollable.get_y()

    direction = event.get_scroll_direction()

    if direction == Clutter.ScrollDirection.UP:
        y -= SCROLL_AMOUNT
    elif direction == Clutter.ScrollDirection.DOWN:
        y += SCROLL_AMOUNT

    # we allow the scrollable's y position to be decremented to the point
    # where its base is aligned with the base of the viewport
    if y < viewport_height - scrollable_height:
        y = viewport_height - scrollable_height
    elif y > 0.0:
        y = 0.0

    print(y)

    # animate the change to the scrollable's y coordinate
    scrollable.animate(Clutter.AnimationMode.EASE_OUT_CUBIC, 300, "y", y)

    return False


image_file_path = "../../data/redhand.png"

if len(sys.argv) > 1:
    image_file_path = sys.argv[1]

stage = Clutter.Stage()
stage.set_size(STAGE_WIDTH, STAGE_HEIGHT)
stage.connect("destroy", Clutter.main_quit)

# the scrollable actor
texture = Clutter.Texture(filename=image_file_path)
texture.set_keep_aspect_ratio(True)

# set the texture's height so it's as tall as the stage
texture.set_request_mode(Clutter.RequestMode.WIDTH_FOR_HEIGHT)
texture.set_height(STAGE_HEIGHT)

# the viewport which the box is scrolled within
viewport = Clutter.Group()
viewport.set_size(STAGE_WIDTH, STAGE_HEIGHT * 0.5)

# align the viewport to the center of the stage's y axis
viewport.add_constraint(Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.Y_AXIS, 0.5))

# viewport needs to respond to scroll events
viewport.set_reactive(True)

# clip all actors inside viewport to the group's allocation
viewport.set_clip_to_allocation(True)

# put the texture inside the viewport
viewport.add_actor(texture)

# add viewport the the stage
stage.add_actor(viewport)

viewport.connect("scroll-event", scroll_event_cb, texture)

stage.show()

Clutter.main()
