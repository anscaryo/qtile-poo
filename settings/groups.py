# Qtile workspaces
import re
from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from .keys import mod, keys

#-----------------------------------------------------------------------
#   Grupos
#-----------------------------------------------------------------------

__groups = {
        1:Group("", layout="monadtall"),
        2:Group("", layout="monadwide", matches=[Match(wm_class=re.compile(r"^(firefox|brave)$"))], screen_affinity = 1),
        3:Group("󰨞", layout="monadwide", matches=[Match(wm_class=re.compile(r"^(Code)$"))]),
        4:Group("", layout="monadwide"),
        5:Group("", layout="monadtall"),
        0:Group("", layout="monadthreecol", screen_affinity = 0),
        }

groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend([
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(), desc = "Cambia al grupo {}".format(i.name)),
        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc = "Cambia y mueve el foco al grupo {}".format(i.name)),
        ])

