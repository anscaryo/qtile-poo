from libqtile import widget, qtile
from .colors import init_colors

colors = init_colors()

f_ground = colors[0]
b_ground = colors[1]



#-----------------------------------------------------------------------
#   Funciones
#-----------------------------------------------------------------------

def texto(texto):
    return widget.TextBox(
                    font="FontAwesome",
                    text=texto,
                    foreground=colors[3], #"fba922",
                    background=colors[1], #"#2f343f",
                    pading=0,
                    fontsize=16
                    )


def layout_actual():
    return widget.CurrentLayout(
                    foreground = f_ground,
                    background = b_ground,
                    fontsize = 16)


def window_name():
    return widget.WindowName(font="Noto Sans",
                                  foreground=colors[12],#"#5dade2",
                                  background=colors[1],
                                  fontsize=12)


def separador():
    return widget.Sep(
            linewidth = 0,
            padding = 10,
            foreground = colors[2],
            background = colors[1]
            )


def call_rofi(qtile):
    qtile.cmd_spawn('rofi -i -show drun -modi drun -show-icons')




#   --------------------------------------------------------------------------
#   Primera Pantalla
#   --------------------------------------------------------------------------


primary_widgets = [
                    widget.Image(
                    filename="~/.config/qtile/imagen/archlinux.png",
                    background=colors[1],
                    foreground=colors[2],
                    mouse_callbacks={'Button1':lambda:qtile.spawn("rofi -show drun")}
                    #mouse_callbacks={'Button1':lambda:qtile.spawn("xdg_menu")}
                    ),

               separador(),
                widget.GroupBox(font="FontAwesome",
                                fontsize=18,
                                margin_x=0,
                                margin_y=0,
                                padding_y=6,
                                padding_x=5,
                                disable_drag = True,
                                active = colors[14], #"#f5b7b1",
                                inactive = colors[9], #"#a9a9a9",
                                rounded = False,
                                highlight_method = "text",
                                this_current_screen_border = colors[8], # "#6790eb",
                                foreground=f_ground,
                                background= colors[1],
                               ),
                separador(),
                layout_actual(),
                separador(),
                widget.Prompt(
                    foreground = colors[0],
                    background = colors[5]),
                separador(),
                window_name(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                
                widget.NetGraph(
                        font="Noto Sans",
                        fontsize=12,
                        bandwidth="down",
                        interface="auto",
                        fill_color = colors[8],
                        foreground=colors[2],
                        background=colors[1],
                        graph_color = colors[0],
                        border_color = colors[1],
                        padding = 0,
                        line_width = 1,
                        mouse_callbacks={'Button1':lambda:qtile.spawn('alacritty -e btop')}

                        ),
                widget.Systray(
                        foreground=colors[2],
                        background=colors[1],
                        icon_size=20
                ),
                separador(),
                widget.TextBox(" 󰚰 ",
                               name= "Update", 
                               font="FontAwesome",
                               foreground=colors[3], #"fba922",
                               background=colors[1], #"#2f343f",
                               pading=0,
                               fontsize=16,
                               mouse_callbacks={'Button1': lambda : qtile.cmd_spawn('alacritty -e sudo pacman -Syyu')}),
                separador(),
                texto(" 󰃰 "),
                widget.Clock(
                        foreground=colors[2],
                        background=colors[1],
                        format="%d/%m/%Y %A %H:%M "
                        ),
                widget.Image(
                    filename="~/.config/qtile/imagen/halt_orange.png",
                    background=colors[1],
                    size=18,
                    foreground=colors[2],
                    mouse_callbacks={'Button1':lambda:qtile.cmd_spawn("archlinux-logout")}
                    ),
           ]

#   --------------------------------------------------------------------------
#   Segunda Pantalla
#   --------------------------------------------------------------------------

secondary_widgets = [
                widget.GroupBox(font="FontAwesome",
                                fontsize=18,
                                margin_x=0,
                                margin_y=0,
                                padding_y=6,
                                padding_x=5,
                                disable_drag = True,
                                active = colors[14], #"#f5b7b1",
                                inactive = colors[9],
                                rounded = False,
                                highlight_method = "text",
                                this_current_screen_border = colors[8],
                                foreground=f_ground,
                                background=b_ground,),
                separador(),
                window_name(),
                layout_actual(),
                widget.Clock(
                    foreground=colors[2],
                    background=colors[1],
                    format="%H:%M:%S "
                    ),
            widget.TextBox(
                    font="FontAwesome",
                    text="  ",
                    foreground=colors[2],
                    background=colors[1],
                    padding = 0,
                    fontsize=16
                    ),
            widget.CPUGraph(
                    border_color = colors[1],
                    fill_color = colors[8],
                    graph_color = colors[0],
                    background=colors[1],
                    border_width = 1,
                    line_width = 1,
                    core = "all",
                    type = "box"                       ),
            ]
    


widgets_defaults = {
        'font': 'FontAwesome',
        'fontsize': 18,
        'padding': 1,
        }
extension_default = widgets_defaults.copy()
