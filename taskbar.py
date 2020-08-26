#!/usr/bin/env python

import subprocess

windows = []
for line in subprocess.run(['wmctrl', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8').split("\n"):
    windows.append(tuple(line.replace("  ", " ").split(" ", 3)))

current_desktop = 0

for line in subprocess.run(['wmctrl', '-d'], stdout=subprocess.PIPE).stdout.decode('utf-8').split("\n"):
    desktop = tuple(line.replace("  ", " ").split(" ", 3))
    if len(desktop) > 2 and desktop[1] == "*":
        current_desktop = desktop[0]

current_window = subprocess.run(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE).stdout.decode('utf-8').split(" ")[4].rstrip()[2:]
while len(current_window) < 8:
    current_window = '0' + current_window
current_window = '0x' + current_window

output = " "

for win in windows:
    if len(win) == 4:
        fg_col = "#999999"
        bg_col = "#1103ecfc"
        if win[1] == current_desktop:
            fg_col = "#ffffff"
        if win[0] == current_window:
            bg_col = "#9904bfbf"
        output = output + "%{A1:wmctrl -i -a " + win[0] + ":}%{B" + bg_col + "}%{F" + fg_col + "}  " + win[3] + "  %{F- B- A-} "
print(output)
