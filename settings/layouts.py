from libqtile import layout
from libqtile.config import Match
from .widgets import colors

#-----------------------------------------------------------------------
#   Layouts
#-----------------------------------------------------------------------


def init_layout_theme():

    return{
            "margin":5,
            "border_width":2,
            "border_focus":colors[10],
            "border_normal":colors[11]
            }



layout_theme =  init_layout_theme()

layouts = [
    layout.MonadWide(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
   ]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)


