#!/usr/bin/env python3

from gi.repository import Clutter, Pango, Cogl

def on_entry_paint(actor):
    allocation = actor.get_allocation_box()

    allocation.clamp_to_pixel()

    Cogl.set_source_color4ub(255, 255, 255, 50);
    Cogl.rectangle(0, 0, *allocation.get_size());

def on_entry_activate(text):
    print("Text activated: %s (cursor: %d, selection at: %d)" % (
        text.get_text(),
        text.get_cursor_position(),
        text.get_selection_bound()
    ))

# def on_captured_event

def create_label(color, markup):
    text = Clutter.Text()
    
    text.set_color(Clutter.Color.from_string(color))
    text.set_markup(markup)
    text.set_editable(False)
    text.set_selectable(False)
    text.set_single_line_mode(True)
    text.set_ellipsize(Pango.EllipsizeMode.END)

    return text

def create_entry(color, passchar, maxlength):
    text = Clutter.Text()
    
    text.set_color(Clutter.Color.from_string(color))
    text.set_reactive(True)
    text.set_editable(True)
    text.set_selectable(True)
    text.set_activatable(True)
    text.set_password_char(passchar)
    text.set_cursor_color(Clutter.Color.from_string("#fff"))
    text.set_selected_text_color(Clutter.Color.from_string("#acf"))
    text.set_single_line_mode(True)
    text.set_max_length(maxlength)

    text.connect("paint", on_entry_paint)
    text.connect("activate", on_entry_activate)
    # text.connect("captured-event", on_captured_event)

    return text

if __name__ == "__main__":
    stage = Clutter.Stage()

    stage.set_color(Clutter.Color.from_string("#000"))
    stage.set_size(500, 250)
    stage.set_title("Text Fields")
    stage.connect("destroy", Clutter.main_quit)

    table = Clutter.TableLayout()

    table.set_column_spacing(6)
    table.set_row_spacing(6)

    box = Clutter.Box(table)

    box.add_constraint(Clutter.BindConstraint.new(stage, Clutter.BindCoordinate.WIDTH, -24))
    box.add_constraint(Clutter.BindConstraint.new(stage, Clutter.BindCoordinate.HEIGHT, -24))
    box.set_position(12, 12)

    box.pack(
        create_label("#fff", "<b>Input field: </b>"),
        row=0,
        column=0,
        x_expand=False,
        y_expand=False
    )

    box.pack(
        create_entry("#ccc", '*', 0),
        row=0,
        column=1,
        x_expand=True,
        x_fill=True,
        y_expand=False
    )

    stage.add_actor(box)
    # stage.set_key_focus(text)
    stage.show_all()

    Clutter.main()

