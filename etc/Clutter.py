# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2009 Johan Dahlin <johan@gnome.org>
#               2010 Simon van der Linden <svdlinden@src.gnome.org>
#               2011 Bastian Winkler <buz@netbuz.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA

import sys
from ..overrides import override
from ..importer import modules
from gi.repository import GObject

Clutter = modules['Clutter']._introspection_module

__all__ = []


class Color(Clutter.Color):
    def __new__(cls, *args, **kwargs):
        return Clutter.Color.__new__(cls)

    def __init__(self, red=0, green=0, blue=0, alpha=0):
        Clutter.Color.__init__(self)
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __repr__(self):
        return '<Clutter.Color(red=%d, green=%d, blue=%d, alpha=%s)>' % (
            self.red, self.green, self.blue, self.alpha)

    def __len__(self):
        return 4

    def __getitem__(self, index):
        if index == 0:
            return self.red
        elif index == 1:
            return self.green
        elif index == 2:
            return self.blue
        elif index == 3:
            return self.alpha
        elif isinstance(index, slice):
            raise TypeError("sequence index must be integer, not 'slice'")
        else:
            raise IndexError("index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.red = value
        elif index == 1:
            self.green = value
        elif index == 2:
            self.blue = value
        elif index == 3:
            self.alpha = value
        else:
            raise IndexError("index out of range")

    def __eq__(self, other):
        return self.equal(other)

    def __ne__(self, other):
        return not self.equal(other)

    @classmethod
    def from_string(cls, string):
        self = cls()
        Clutter.Color.from_string(self, string)
        return self

    @classmethod
    def from_hls(cls, hue, luminance, saturation):
        self = cls()
        Clutter.Color.from_hls(self, hue, luminance, saturation)
        return self

    @classmethod
    def from_pixel(cls, pixel):
        self = cls()
        Clutter.Color.from_pixel(self, pixel)
        return self

Color = override(Color)
__all__.append('Color')


class ActorBox(Clutter.ActorBox):
    def __new__(cls, *args, **kwargs):
        return Clutter.ActorBox.__new__(cls)

    def __init__(self, x1=0.0, y1=0.0, x2=0.0, y2=0.0):
        Clutter.ActorBox.__init__(self)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return '<Clutter.ActorBox(x1=%f, y1=%f, x2=%f y2=%f)>' % (
            self.x1, self.y1, self.x2, self.y2)

    def __len__(self):
        return 4

    def __getitem__(self, index):
        if index == 0:
            return self.x1
        elif index == 1:
            return self.y1
        elif index == 2:
            return self.x2
        elif index == 3:
            return self.y2
        elif isinstance(index, slice):
            raise TypeError("sequence index must be integer, not 'slice'")
        else:
            raise IndexError("index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x1 = value
        elif index == 1:
            self.y1 = value
        elif index == 2:
            self.x2 = value
        elif index == 3:
            self.y2 = value
        else:
            raise IndexError("index out of range")

    def __eq__(self, other):
        return self.equal(other)

    def __ne__(self, other):
        return not self.equal(other)

    @property
    def size(self):
        return (self.x2 - self.x1, self.y2 - self.y1)

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

ActorBox = override(ActorBox)
__all__.append('ActorBox')


class Vertex(Clutter.Vertex):
    def __new__(cls, *args, **kwargs):
        return Clutter.Vertex.__new__(cls)

    def __init__(self, x=0.0, y=0.0, z=0.0):
        Clutter.Vertex.__init__(self)
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '<Clutter.Vertex(x=%f, y=%f, z=%f)>' % (self.x, self.y, self.z)

    def __len__(self):
        return 3

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        elif isinstance(index, slice):
            raise TypeError("sequence index must be integer, not 'slice'")
        else:
            raise IndexError("index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.y = value
        else:
            raise IndexError("index out of range")

    def __eq__(self, other):
        return self.equal(other)

    def __ne__(self, other):
        return not self.equal(other)

Vertex = override(Vertex)
__all__.append('Vertex')


class Geometry(Clutter.Geometry):
    def __new__(cls, *args, **kwargs):
        return Clutter.Geometry.__new__(cls)

    def __init__(self, x=0, y=0, width=0, height=0):
        Clutter.Geometry.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        return '<Clutter.Geometry(x=%d, y=%d, width=%d, height=%d)>' % (
            self.x, self.y, self.width, self.height)

    def __len__(self):
        return 4

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.width
        elif index == 3:
            return self.height
        elif isinstance(index, slice):
            raise TypeError("sequence index must be integer, not 'slice'")
        else:
            raise IndexError("index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.width = value
        elif index == 3:
            self.height = value
        else:
            raise IndexError("index out of range")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and \
                self.width == other.width and self.height == other.height

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or \
                self.width != other.width or self.height != other.height

Geometry = override(Geometry)
__all__.append('Geometry')


class Event(Clutter.Event):
    _UNION_MEMBERS = {
        Clutter.EventType.KEY_PRESS: 'key',
        Clutter.EventType.KEY_RELEASE: 'key',
        Clutter.EventType.MOTION: 'motion',
        Clutter.EventType.ENTER: 'crossing',
        Clutter.EventType.LEAVE: 'crossing',
        Clutter.EventType.BUTTON_PRESS: 'button',
        Clutter.EventType.BUTTON_RELEASE: 'button',
        Clutter.EventType.SCROLL: 'scroll',
        Clutter.EventType.STAGE_STATE: 'stage_state'
    }

    def __new__(cls, *args, **kwargs):
        return Clutter.Event.__new__(cls)

    def __getattr__(self, name):
        real_event = getattr(self, '_UNION_MEMBERS').get(self.type())
        if real_event:
            return getattr(getattr(self, real_event), name)
        else:
            raise AttributeError("'%s' object has no attribute '%s'" %
                                 (self.__class__.__name__, name))

    def __str__(self):
        def get_key():
            from gi.overrides import keysyms
            for name in dir(keysyms):
                if self.keyval == getattr(keysyms, name):
                    return name
            if sys.version_info < (3, 0):
                return unichr(self.get_key_unicode()).encode('UTF-8')
            else:
                return chr(self.get_key_unicode())

        def actor_name(actor):
            if not actor:
                return 'None'
            if actor.get_name():
                return actor.get_name()
            return actor.__class__.__name__

        def get_state():
            if self.get_state():
                return 'modifier: %s; ' % str(self.get_state())
            return ''

        if self.type() == Clutter.EventType.BUTTON_PRESS:
            return ('<Button Press at (%d,%d); button: %d; count: %d; %s' +
                    'time: %d; source: %s>') % (self.button.x, self.button.y,
                            self.button.button, self.button.click_count,
                            get_state(), self.get_time(),
                            actor_name(self.get_source()))
        elif self.type() == Clutter.EventType.BUTTON_RELEASE:
            return ('<Button Release at (%d,%d); button: %d; count: %d; %s' +
                    'time: i%d; source: %s>') % (self.button.x, self.button.y,
                            self.button.button, self.button.click_count,
                            get_state(), self.get_time(),
                            actor_name(self.get_source()))
        elif self.type() == Clutter.EventType.KEY_PRESS:
            return "<Key Press '%s'; %stime: %d; source %s>" % (
                    get_key(), get_state(), self.get_time(),
                    actor_name(self.get_source()))
        elif self.type() == Clutter.EventType.KEY_RELEASE:
            return "<Key Release '%s'; %stime: %d; source %s>" % (
                    get_key(), get_state(), self.get_time(),
                    actor_name(self.get_source()))
        elif self.type() == Clutter.EventType.MOTION:
            return "<Motion at (%d,%d); time: %d; source %s>" % (
                    self.motion.x, self.motion.y, self.get_time(),
                    actor_name(self.get_source()))
        elif self.type() == Clutter.EventType.ENTER:
            return "<Entering actor %s related to actor %s; time %d>" % (
                    actor_name(self.get_source()),
                    actor_name(self.get_related()), self.get_time())
        elif self.type() == Clutter.EventType.LEAVE:
            return "<Leaving actor %s related to actor %s; time %d>" % (
                    actor_name(self.get_source()),
                    actor_name(self.get_related()), self.get_time())
        elif self.type() == Clutter.EventType.SCROLL:
            return ("<Scroll %d at (%d,%d); modifier: %s; time: %d; " +
                    "source: %s>") % ( self.scroll.direction.value_nick,
                            self.scroll.x, self.scroll.y, self.get_time(),
                            actor_name(self.get_source()))
        elif self.type() == Clutter.EventType.STAGE_STATE:
            return '<Stage state %s on %s>' % (self.get_flags(),
                    actor_name(self.get_stage()))
        elif self.type() == Clutter.EventType.NOTHING:
            return '<Nothing>'
        else:
            return '<Unkown event>'


Event = override(Event)
__all__.append('Event')


class Actor(Clutter.Actor):
    def _update_animation(self, *args, **kwargs):
        def _detach_animation(animation):
            delattr(self, '_animation')
            del animation

        # check if we already have a running animation
        if hasattr(self, '_animation'):
            animation = getattr(self, '_animation')
        else:
            animation = Clutter.Animation()
            animation.set_object(self)
            animation.connect('completed', _detach_animation)
            setattr(self, '_animation', animation)

        # check arguments
        if len(args) == 1 and isinstance(args[0], dict):
            properties = args[0].items()
        elif len(args) == 2 and isinstance(args[0], (tuple, list)) and \
                isinstance(args[1], (tuple, list)):
            properties = zip(args[0], args[1])
        elif len(args) >= 2 and not 2 % 2:
            properties = zip(args[::2], args[1::2])
        elif kwargs:
            properties = kwargs.items()
        else:
            raise TypeError('The arguments must be: ' +
                    '"property", value, "property", value, ... or ' +
                    '("property", "property", ...), (value, value, ...) ' +
                    'or {"property": value, "property", value}')

        for prop, value in properties:
            if not isinstance(prop, str):
                raise TypeError('A property must be a string, got %s' %
                        type(prop))
            elif prop.startswith("fixed::"):
                prop = prop[7:]
                self.set_property(prop, value)
            elif animation.has_property(prop):
                animation.update(prop, value)
            else:
                animation.bind(prop, value)
        return animation

    def animate(self, mode, duration, *args, **kwargs):
        """
        The animate() method is a convenience method to create or update a
        Clutter.Animation. The animation properties can be specified in
        multiple ways:

        Property/value pairs
        >>> actor.animate(Clutter.AnimationMode.LINEAR, 1000,
        ...     "x", 200.0, "y", 200.0)

        A keyword list
        >>> actor.animate(Clutter.AnimationMode.LINEAR, 1000,
        ...     x=200.0, y=200.0)

        A tuple with properties and a tuple with values
        >>> actor.animate(Clutter.AnimationMode.LINEAR, 1000,
        ...     ("x", "y"), (200.0, 200.0))

        A single dictionary
        >>> actor.animate(Clutter.ANimationMode.LINEAR, 1000,
        ...     {"x": 200.0, "y", 200.0})
        """
        animation = self._update_animation(*args, **kwargs)
        animation.set_mode(mode)
        animation.set_duration(duration)
        animation.get_timeline().start()
        return animation

    def animate_with_timeline(self, mode, timeline, *args, **kwargs):
        animation = self._update_animation(*args, **kwargs)
        animation.set_mode(mode)
        animation.set_timeline(timeline)
        animation.get_timeline().start()
        return animation

    def animate_with_alpha(self, alpha, *args, **kwargs):
        animation = self._update_animation(*args, **kwargs)
        animation.set_alpha(alpha)
        animation.get_timeline().start()
        return animation

    def raise_actor(self, below):
        parent = self.get_parent()
        if not parent:
            return
        parent.raise_child(self, below)

    def lower_actor(self, above):
        parent = self.get_parent()
        if not parent:
            return
        parent.lower_child(self, above)

    def transform_stage_point(self, x, y):
        success, x_out, y_out = super(Actor, self).transform_stage_point(x, y)
        if success:
            return (x_out, y_out)

    def get_paint_box(self):
        success, box = super(Actor, self).get_paint_box()
        if success:
            return box

Actor = override(Actor)
__all__.append('Actor')


class Container(Clutter.Container):
    def __len__(self):
        return len(self.get_children())

    def __contains__(self, actor):
        return actor in self.get_children()

    def __iter__(self):
        return iter(self.get_children())

    def __getitem__(self, index):
        return self.get_children()[index]

    def add(self, *actors):
        for actor in actors:
            Clutter.Container.add_actor(self, actor)

    def remove(self, *actors):
        for actor in actors:
            Clutter.Container.remove_actor(self, actor)

    def child_get_property(self, child, property_name):
        meta = self.get_child_meta(child)
        return meta.get_property(property_name)

    def child_set_property(self, child, property_name, value):
        meta = self.get_child_meta(child)
        meta.set_property(property_name, value)

Container = override(Container)
__all__.append('Container')


class Texture(Clutter.Texture, Actor):
    def __init__(self, filename=None, **kwargs):
        if filename is not None:
            kwargs['filename'] = filename
        Clutter.Texture.__init__(self, **kwargs)

Texture = override(Texture)
__all__.append('Texture')


class Rectangle(Clutter.Rectangle, Actor):
    def __init__(self, color=None, **kwargs):
        if color is not None:
            kwargs['color'] = color
        Clutter.Rectangle.__init__(self, **kwargs)

Rectangle = override(Rectangle)
__all__.append('Rectangle')


class Text(Clutter.Text, Actor):
    def __init__(self, font_name=None, text=None, color=None, **kwargs):
        if font_name is not None:
            kwargs['font_name'] = font_name
        if text is not None:
            kwargs['text'] = text
        if color is not None:
            kwargs['color'] = color
        Clutter.Text.__init__(self, **kwargs)

    def position_to_coords(self, position):
        success, x, y, lh = Clutter.Text.position_to_coords(self, position)
        if success:
            return (x, y, lh)

Text = override(Text)
__all__.append('Text')


class CairoTexture(Clutter.CairoTexture):
    def __init__(self, surface_width, surface_height, **kwargs):
        Clutter.CairoTexture.__init__(self, surface_width=surface_width,
                                      surface_height=surface_height, **kwargs)

CairoTexture = override(CairoTexture)
__all__.append('CairoTexture')


class Clone(Clutter.Clone):
    def __init__(self, source=None, **kwargs):
        Clutter.Clone.__init__(self, source=source, **kwargs)

Clone = override(Clone)
__all__.append('Clone')


class LayoutManager(Clutter.LayoutManager):
    def child_set_property(self, container, child, property_name, value):
        meta = self.get_child_meta(container, child)
        meta.set_property(property_name, value)

    def child_get_property(self, container, child, property_name):
        meta = self.get_child_meta(container, child)
        return meta.get_property(property_name)

LayoutManager = override(LayoutManager)
__all__.append('LayoutManager')


class Box(Clutter.Box, Actor):
    def __init__(self, layout_manager=None, **kwargs):
        Clutter.Box.__init__(self, layout_manager=layout_manager, **kwargs)

    def pack(self, actor, **kwargs):
        self.add_actor(actor)
        layout_manager = self.get_layout_manager()
        if layout_manager:
            for k, v in kwargs.items():
                layout_manager.child_set_property(actor, k, v)

    def pack_after(self, actor, silbing, **kwargs):
        self.add_actor(actor)
        self.raise_child(actor, silbing)
        layout_manager = self.get_layout_manager()
        if layout_manager:
            for k, v in kwargs.items():
                layout_manager.child_set_property(actor, k, v)

    def pack_before(self, actor, silbing, **kwargs):
        self.add_actor(actor)
        self.lower_child(actor, silbing)
        layout_manager = self.get_layout_manager()
        if layout_manager:
            for k, v in kwargs.items():
                layout_manager.child_set_property(actor, k, v)

Box = override(Box)
__all__.append('Box')


class Model(Clutter.Model):
    def insert(self, row, *args):
        if len(args) < 2 or len(args) % 2:
            raise ValueError("Clutter.Model.insert needs at least one " +
                    "column / value pair")
            for column, value in zip(args[::2], args[1::2]):
                self.insert_value(row, column, value)

    def append(self, *args):
        if len(args) < 2 or len(args) % 2:
            raise ValueError("Clutter.Model.append needs at least one " +
                    "column / value pair")
            row = self.get_n_rows()
        self.insert(row, *args)

    def prepend(self, *args):
        if len(args) < 2 or len(args) % 2:
            raise ValueError("Clutter.Model.prepend needs at least one " +
                    "column / value pair")
        # FIXME: This won't work
        self.insert(-1, *args)

Model = override(Model)
__all__.append('Model')


class ListModel(Clutter.ListModel):
    def __init__(self, *args):
        Clutter.ListModel.__init__(self)
        if len(args) < 2 or len(args) % 2:
            raise TypeError("Clutter.ListModel requires at least one " +
                            "type / name pair")
        self.set_types(args[::2])
        self.set_names(args[1::2])

ListModel = override(ListModel)
__all__.append('ListModel')


class Timeline(Clutter.Timeline):
    def __init__(self, duration=1000, **kwargs):
        Clutter.Timeline.__init__(self, duration=duration, **kwargs)

    def list_markers(self, position=-1):
        markers, n_markers = Clutter.Timeline.list_markers(self, position)
        return markers

Timeline = override(Timeline)
__all__.append('Timeline')


class Alpha(Clutter.Alpha):
    def __init__(self, timeline=None, mode=Clutter.AnimationMode.LINEAR,
            **kwargs):
        Clutter.Alpha.__init__(self, timeline=timeline, mode=mode, **kwargs)

Alpha = override(Alpha)
__all__.append('Alpha')


class Path(Clutter.Path):
    def __init__(self, description=None, **kwargs):
        Clutter.Path.__init__(self)
        if description:
            self.set_description(description)

Path = override(Path)
__all__.append('Path')


class BehaviourPath(Clutter.BehaviourPath):
    def __init__(self, alpha=None, path=None, description=None):
        Clutter.BehaviourPath.__init__(self)
        self.props.alpha = alpha
        if path:
            self.set_path(path)
        elif description is not None:
            path = Path(description)
            self.set_path(path)

BehaviourPath = override(BehaviourPath)
__all__.append('BehaviourPath')


class Script(Clutter.Script):
    def get_objects(self, *objects):
        ret = []
        for name in objects:
            obj = self.get_object(name)
            ret.append(obj)
        return ret

Script = override(Script)
__all__.append('Script')


class BindingPool(Clutter.BindingPool):
    def __init__(self, name, **kwargs):
        Clutter.BindingPool.__init__(self, name=name, **kwargs)

BindingPool = override(BindingPool)
__all__.append('BindingPool')


class Shader(Clutter.Shader):
    def set_vertex_source(self, data, length=-1):
        Clutter.Shader.set_vertex_source(self, data, length)

    def set_fragment_source(self, data, length=-1):
        Clutter.Shader.set_fragment_source(self, data, length)

Shader = override(Shader)
__all__.append('Shader')


def _gvalue_from_python(obj, prop_name, v):
    try:
        pspec = getattr(obj.__class__.props, prop_name)
    except AttributeError:
        raise AttributeError("Objects of type %s don't have a property '%s" %
                             (type(obj), prop_name))
    value = GObject.Value()
    value.init(pspec.value_type)
    if pspec.value_type == GObject.TYPE_INT:
        value.set_int(int(v))
    elif pspec.value_type == GObject.TYPE_UINT:
        value.set_uint(int(v))
    elif pspec.value_type == GObject.TYPE_CHAR:
        value.set_char(int(v))
    elif pspec.value_type == GObject.TYPE_UCHAR:
        value.set_uint(int(v))
    elif pspec.value_type == GObject.TYPE_FLOAT:
        value.set_float(float(v))
    elif pspec.value_type == GObject.TYPE_DOUBLE:
        value.set_double(float(v))
    elif pspec.value_type == GObject.TYPE_LONG:
        value.set_long(long(v))
    elif pspec.value_type == GObject.TYPE_ULONG:
        value.set_ulong(long(v))
    elif pspec.value_type == GObject.TYPE_INT64:
        value.set_int64(long(v))
    elif pspec.value_type == GObject.TYPE_UINT64:
        value.set_uint64(long(v))
    elif pspec.value_type == GObject.TYPE_BOOLEAN:
        value.set_boolean(bool(v))
    elif pspec.value_type == GObject.TYPE_STRING:
        if isinstance(v, str):
            v = str(v)
        elif sys.version_info < (3, 0):
            if isinstance(v, unicode):
                v = v.encode('UTF-8')
            else:
                raise ValueError("Expected string or unicode for property " + \
                        "%s but got %s%s" % (prop_name, v, type(v)))
        else:
            raise ValueError("Expected string or unicode for property " + \
                    "%s but got %s%s" % (prop_name, v, type(v)))
        value.set_string(str(v))
    else:
        return v
    return value


class Animator(Clutter.Animator):
    def set_key(self, obj, prop, mode, progress, value):
        return Clutter.Animator.set_key(self, obj, prop, mode, progress,
                _gvalue_from_python(obj, prop, value))


Animator = override(Animator)
__all__.append('Animator')


class State(Clutter.State):
    def set_key(self, source_state, target_state, obj, prop, mode,
                value, pre_delay=0.0, post_delay=0.0):
        return Clutter.State.set_key(self, source_state, target_state, obj,
                prop, mode, _gvalue_from_python(obj, prop, value),
                pre_delay, post_delay)

State = override(State)
__all__.append('State')


# override the main_quit function to ignore additional arguments. This enables
# common stuff like stage.connect('destroy', Clutter.main_quit)
def main_quit(*args, **kwargs):
    Clutter.main_quit()

__all__.append('main_quit')


clutter_version = (Clutter.MAJOR_VERSION, Clutter.MINOR_VERSION,
                   Clutter.MICRO_VERSION)
__all__.append('clutter_version')


# Initialize Clutter directly on import
initialized, argv = Clutter.init(sys.argv)
sys.argv = argv
if not initialized:
    raise RuntimeError("Could not initialize Cluttter")
