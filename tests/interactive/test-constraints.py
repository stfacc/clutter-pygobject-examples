#!/usr/bin/env python3

import math

from gi.repository import Clutter

# We store the name of the region as the dictionary key, and then keep a list of the color
# and a reference to the created Rectangle instance.
RECTS = {
    "NorthWest": ["#8ae234", None], "North":  ["#73d216", None], "NorthEast": ["#4e9a06", None],
    "West":      ["#729fcf", None], "Center": ["#3465a4", None], "East":      ["#204a87", None],
    "SouthWest": ["#ef2929", None], "South":  ["#cc0000", None], "SouthEast": ["#a40000", None]
}

SHADER_SOURCE = """
uniform sampler2D tex;
uniform float factor;
vec3 desaturate (const vec3 color, const float desaturation) {
    const vec3 gray_conv = vec3 (0.299, 0.587, 0.114);
    vec3 gray = vec3 (dot (gray_conv, color));
    return vec3 (mix (color.rgb, gray, desaturation));
}
void main () {
    vec4 color = cogl_color_in * texture2D (tex, vec2 (cogl_tex_coord_in[0].xy));
    color.rgb = desaturate (color.rgb, factor);
    cogl_color_out = color;
}
"""

RECT_SIZE   = 128
V_PADDING   = 32
H_PADDING   = 32
ANIM_TIME   = 750
IS_EXPANDED = False

def do_animate(rect, opacity, reactive, x, y):
    properties = {
        "opacity": opacity,
        "reactive": reactive
    }

    if not x == None:
        properties["@constraints.x-bind.offset"] = x
        
    if not y == None:
        properties["@constraints.y-bind.offset"] = y

    RECTS[rect][1].animate(Clutter.AnimationMode.EASE_OUT_EXPO, ANIM_TIME, properties)

def button_release_cb(actor, event, data):
    global IS_EXPANDED

    if not IS_EXPANDED:
        north = (RECTS["Center"][1].get_height() + V_PADDING) * -1.0
        south = (RECTS["Center"][1].get_height() + V_PADDING)
        west  = (RECTS["Center"][1].get_width() + H_PADDING) * -1.0
        east  = (RECTS["Center"][1].get_width() + H_PADDING)

        do_animate("NorthWest", 255, True, west, north)
        do_animate("North", 255, True, None, north)
        do_animate("NorthEast", 255, True, east, north)
        do_animate("West", 255, True, west, None)
        do_animate("East", 255, True, east, None)
        do_animate("SouthWest", 255, True, west, south)
        do_animate("South", 255, True, None, south)
        do_animate("SouthEast", 255, True, east, south)

        RECTS["Center"][1].animate(
            Clutter.AnimationMode.LINEAR,
            ANIM_TIME,
            "@effects.desaturate.enabled", True,
            "reactive", False
        )

    else:
        RECTS["Center"][1].animate(
            Clutter.AnimationMode.LINEAR,
            ANIM_TIME,
            "@effects.desaturate.enabled", False,
            "reactive", True
        )

        for rect in RECTS.keys():
            if rect == "Center":
                continue

            do_animate(rect, 0, False, 0.0, 0.0)

    IS_EXPANDED = not IS_EXPANDED

if __name__ == "__main__":
    stage = Clutter.Stage()

    stage.set_title("Constraints")
    stage.set_user_resizable(True)
    stage.set_size(800, 600)
    stage.connect("destroy", Clutter.main_quit)

    rect = Clutter.Rectangle()

    rect.set_color(Clutter.Color.from_string(RECTS["Center"][0]))
    rect.set_size(RECT_SIZE, RECT_SIZE)
    rect.set_reactive(True)
    rect.set_name("Center")
    rect.connect("button-release-event", button_release_cb, None)

    x_constraint = Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.X_AXIS, 0.5)
    y_constraint = Clutter.AlignConstraint.new(stage, Clutter.AlignAxis.Y_AXIS, 0.5)

    rect.add_constraint_with_name("x-align", x_constraint)
    rect.add_constraint_with_name("y-align", y_constraint)

    effect = Clutter.ShaderEffect()

    effect.set_shader_source(SHADER_SOURCE)
    effect.set_uniform_value("tex", 0)
    effect.set_uniform_value("factor", 0.66)

    rect.add_effect_with_name("desaturate", effect)

    stage.add_actor(rect)

    # Keep a copy of our Center rect for later.
    RECTS["Center"][1] = rect

    for rect_name, rect_data in RECTS.items():
        # Skip the Center rect, we've already created it.
        if rect_name == "Center":
            continue

        r = Clutter.Rectangle()
        
        r.set_color(Clutter.Color.from_string(rect_data[0]))
        r.set_opacity(0.0)
        r.set_name(rect_name)

        x_bind    = Clutter.BindConstraint.new(rect, Clutter.BindCoordinate.X, 0.0)
        y_bind    = Clutter.BindConstraint.new(rect, Clutter.BindCoordinate.Y, 0.0)
        size_bind = Clutter.BindConstraint.new(rect, Clutter.BindCoordinate.SIZE, 0.0)
        
        r.add_constraint_with_name("x-bind", x_bind)
        r.add_constraint_with_name("y-bind", y_bind)
        r.add_constraint_with_name("size-bind", size_bind)
        r.connect("button-release-event", button_release_cb, None)

        stage.add_actor(r)

        # Keep a copy of each rect for later, like Center above.
        rect_data[1] = r

    stage.show_all()

    Clutter.main()

