# polybar-taskbar
Simple taskbar module for [polybar](https://github.com/polybar/polybar) written in Python 3.

Module displays all opened GUI applications next to each other.

![Example](https://raw.githubusercontent.com/ThomasTheHuman/polybar-taskbar/master/example.png "Example")

Three different styles are provided for:
- focused window,
- unfocused windows on active workspace,
- windows on unactive workspaces.

Chosen window can be focused using left mouse click.

### Example module declaration:
```
[module/taskbar]
type = custom/script
interval = 0.25
label-foreground = ${colors.foreground}
label-background = ${colors.background}
label = %output%
format = <label>
exec = python3 /path/to/taskbar.py
```

#### THIS MODULE IS WORK IN PROGRESS

At current stage it is just a proof of concept.
For now most of configuration must be done inside script file.
