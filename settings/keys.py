#   Qtile mapeo de teclas
from libqtile.config import Key
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy


#-----------------------------------------------------------------------
#   Asignación de teclas
#-----------------------------------------------------------------------


mod = "mod4"

terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html


#----    Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.

   # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
   # Grow windows. If current window is on the edge of screen and direction
   # will be to screen edge - window would shrink.

   
#----    RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        #lazy.layout.increase_ratio(),
        #lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        #lazy.layout.increase_ratio(),
        #lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        #lazy.layout.decrease_ratio(),
        #lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        #lazy.layout.decrease_ratio(),
        #lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        #lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        #lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        #lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        #lazy.layout.increase_nmaster(),
        ),
#    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
#    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
#    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
#    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key(
    #    [mod, "shift"],
    #    "Return",
    #    lazy.layout.toggle_split(),
    #    desc="Toggle between split and unsplit sides of stack",
    #),

    
#----   Aplicaciones:
    Key([mod, "shift"], "Return", lazy.spawn("thunar"), desc="Lanza el administrador de archivos"),
    Key([mod], "x", lazy.spawn("archlinux-logout"), desc="Lanza el menu para cerrar seison de arcolinux"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Lanza la terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "m", lazy.spawn("rofi -i -show drun -modi drun -show-icons"), desc="Abre el menu rofi"),
    Key([mod, "shift"], "f", lazy.spawn("firefox"), desc="Lanza el navegador firefox"),
    Key([mod], "b", lazy.spawn("brave"), desc="Lanza el navegador brave"),
    Key([mod, "shift"], "c", lazy.spawn("code"), desc="Lanza Visual Studio Code"),
    Key([mod, "shift"], "s", lazy.spawn("pavucontrol"), desc="Lanza aplicación para controlar el sonido")
    
]


