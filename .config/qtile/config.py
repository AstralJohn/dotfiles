import os
import subprocess

from libqtile.log_utils import logger
from libqtile import bar, layout, widget
from libqtile import hook
import libqtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(["mod1"], "h", lazy.next_screen(), desc="Move to next screen"),
    Key(["mod1"], "l", lazy.next_screen(), desc="Move to next screen"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(["mod1", "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key(["mod1"], "Return", lazy.spawn("zsh /home/john/.config/rofi/launchers/type-2/launcher.sh")),
    Key([mod], "p", lazy.spawn("zsh /home/john/.config/rofi/launchers/type-2/launcher-window.sh")),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "m", lazy.layout.maximize()),
    Key([mod], "period", lazy.spawn("zsh /home/john/.config/rofi/launchers/type-2/launcher-emoji.sh")),
]

#  from libqtile.dgroups import simple_key_binder
#  dgroups_key_binder = simple_key_binder("mod4")

# for qwerty keyboards
#  group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#  group_labels = ["web", "code", "term", "games", "social", "music"]
#  for i in range(len(group_labels)):
#      groups.append(
#              Group(
#                  name=group_names[i],
#                  label=group_labels[i]
#                  )
#              )


# groups = [Group(i) for i in "123456789"]


groups = [Group("DEV", layout='monadtall'),
          Group("WWW", layout='monadtall'),
          Group("CHAT", layout='monadtall'),
          Group("MUS", layout='monadtall'),
          Group("VID", layout='monadtall'),
          Group("GAME", layout='monadtall'),
          Group("SYS", layout='monadtall'),
          ]

#  from libqtile.dgroups import simple_key_binder
#  dgroups_key_binder = simple_key_binder("mod4")


for i in range(len(groups)):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(i + 1),
                lazy.group[groups[i].name].toscreen(),
                desc="Switch to group {}".format(groups[i].name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(i + 1),
                lazy.window.togroup(groups[i].name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(groups[i].name),
            ),
            
            Key(
                [mod],
                groups[i].name[0].lower(),
                lazy.group[groups[i].name].toscreen(),
                desc="Switch to group {}".format(groups[i].name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                groups[i].name[0].lower(),
                lazy.window.togroup(groups[i].name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(groups[i].name),
            ),

            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
    

@hook.subscribe.client_new
def client_new(c):
    #  logger.warning(c.name)
    if c.name == "Mozilla Firefox":
        c.togroup('WWW')


colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(
        #  margin = 25
        ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    #  layout.Bsp(),
    # layout.Matrix(),
    #  layout.MonadTall( margin=25),
    #  layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Ubuntu",
    fontsize=18,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 12,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Image(
                    filename = "~/.config/qtile/icons/archlinux_icon.png",
                    scale = True,
                    background = colors[0],
                    margin_y = 2
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 12,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.GroupBox(
                    fontsize = 10,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 3,
                    borderwidth = 3,
                    active = colors[2],
                    inactive = colors[7],
                    rounded = False,
                    highlight_color = colors[1],
                    highlight_method = "line",
                    this_current_screen_border = colors[6],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[6],
                    other_screen_border = colors[4],
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.TextBox(
                    text = '|',
                    font = "Ubuntu Mono",
                    background = colors[0],
                    foreground = '474747',
                    padding = 2,
                    fontsize = 14
                ),
                widget.CurrentLayoutIcon(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                ),
                widget.CurrentLayout(
                        fontsize = 14,
                       foreground = colors[2],
                       background = colors[0],
                       padding = 5
                ),
                widget.TextBox(
                    text = '|',
                    font = "Ubuntu Mono",
                    background = colors[0],
                    foreground = '474747',
                    padding = 2,
                    fontsize = 14
                ),

                widget.WindowName(
                        fontsize=14,
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                ),
                # widget.Prompt(),
                # widget.TextBox("default config", name="default"),
                widget.Systray(background=colors[0]),

                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Net(
                    background = colors[0],
                    fontsize=14,
                    interface = "wlp4s0",
                    format = 'Net: {down} ↓↑ {up}',
                ),

                widget.Battery(
                    fontsize = 14,
                    format = "{percent: 2.0%} {hour:d}:{min:02d}",
                    charge_char = '↑',
                    discharge_char = '↓',
                    background = colors[0],
                ),
                widget.Memory(
                       foreground = colors[1],
                       background = colors[6],
                       fmt = 'Mem: {}',
                       padding = 5,
                       fontsize=14
                       ),


                # widget.Net(interface="wlp4s0"),
                #  widget.Clock(format="%m/%d/%y (%a) %I:%M %p", font="Ubuntu"),
                widget.Clock(
                    fontsize=14,
                    foreground = colors[1],
                    background = colors[9],
                    format="%m/%d/%y (%a) %I:%M %p"
                ),

            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 12,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Image(
                    filename = "~/.config/qtile/icons/archlinux_icon.png",
                    scale = True,
                    background = colors[0],
                    margin_y = 2
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 12,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.GroupBox(
                    fontsize = 10,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 3,
                    borderwidth = 3,
                    active = colors[2],
                    inactive = colors[7],
                    rounded = False,
                    highlight_color = colors[1],
                    highlight_method = "line",
                    this_current_screen_border = colors[6],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[6],
                    other_screen_border = colors[4],
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.TextBox(
                    text = '|',
                    font = "Ubuntu Mono",
                    background = colors[0],
                    foreground = '474747',
                    padding = 2,
                    fontsize = 14
                ),
                widget.CurrentLayoutIcon(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                ),
                widget.CurrentLayout(
                        fontsize = 14,
                       foreground = colors[2],
                       background = colors[0],
                       padding = 5
                ),
                widget.TextBox(
                    text = '|',
                    font = "Ubuntu Mono",
                    background = colors[0],
                    foreground = '474747',
                    padding = 2,
                    fontsize = 14
                ),

                widget.WindowName(
                        fontsize=14,
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Net(
                    background = colors[0],
                    fontsize=14,
                    interface = "wlp4s0",
                    format = 'Net: {down} ↓↑ {up}',
                ),

                widget.Battery(
                    fontsize = 14,
                    format = "{percent: 2.0%} {hour:d}:{min:02d}",
                    charge_char = '↑',
                    discharge_char = '↓',
                    background = colors[0],
                ),
                widget.Memory(
                       foreground = colors[1],
                       background = colors[6],
                       fmt = 'Mem: {}',
                       padding = 5,
                       fontsize=14
                       ),


                # widget.Net(interface="wlp4s0"),
                #  widget.Clock(format="%m/%d/%y (%a) %I:%M %p", font="Ubuntu"),
                widget.Clock(
                    fontsize=14,
                    foreground = colors[1],
                    background = colors[9],
                    format="%m/%d/%y (%a) %I:%M %p"
                ),

            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen(['zsh', home])
