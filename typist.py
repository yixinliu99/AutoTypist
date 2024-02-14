import time
import os_Interfaces.universal_interface as os_interface

KEY_NAMES = [
    "\t",
    "\n",
    "\r",
    " ",
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "{",
    "|",
    "}",
    "~",
    "accept",
    "add",
    "alt",
    "altleft",
    "altright",
    "apps",
    "backspace",
    "browserback",
    "browserfavorites",
    "browserforward",
    "browserhome",
    "browserrefresh",
    "browsersearch",
    "browserstop",
    "capslock",
    "clear",
    "convert",
    "ctrl",
    "ctrlleft",
    "ctrlright",
    "decimal",
    "del",
    "delete",
    "divide",
    "down",
    "end",
    "enter",
    "esc",
    "escape",
    "execute",
    "f1",
    "f10",
    "f11",
    "f12",
    "f13",
    "f14",
    "f15",
    "f16",
    "f17",
    "f18",
    "f19",
    "f2",
    "f20",
    "f21",
    "f22",
    "f23",
    "f24",
    "f3",
    "f4",
    "f5",
    "f6",
    "f7",
    "f8",
    "f9",
    "final",
    "fn",
    "hanguel",
    "hangul",
    "hanja",
    "help",
    "home",
    "insert",
    "junja",
    "kana",
    "kanji",
    "launchapp1",
    "launchapp2",
    "launchmail",
    "launchmediaselect",
    "left",
    "modechange",
    "multiply",
    "nexttrack",
    "nonconvert",
    "num0",
    "num1",
    "num2",
    "num3",
    "num4",
    "num5",
    "num6",
    "num7",
    "num8",
    "num9",
    "numlock",
    "pagedown",
    "pageup",
    "pause",
    "pgdn",
    "pgup",
    "playpause",
    "prevtrack",
    "print",
    "printscreen",
    "prntscrn",
    "prtsc",
    "prtscr",
    "return",
    "right",
    "scrolllock",
    "select",
    "separator",
    "shift",
    "shiftleft",
    "shiftright",
    "sleep",
    "space",
    "stop",
    "subtract",
    "tab",
    "up",
    "volumedown",
    "volumemute",
    "volumeup",
    "win",
    "winleft",
    "winright",
    "yen",
    "command",
    "option",
    "optionleft",
    "optionright",
]
KEYBOARD_MAPPING = {key: key for key in KEY_NAMES}


class Typist:
    def __init__(self, data, interval):
        self.data = data
        self.interval = interval
        self.universal_interface = os_interface.UniversalInterface()

    def press(self, keys, presses=1, interval=0.0):
        """
        Performs a keyboard key press down, followed by a release.
        @param keys: The key to be pressed. The valid names are listed in KEYBOARD_KEYS. Can also be a list of such strings.
        @param presses: The number of press repetitions. 1 by default, for just one press.
        @param interval: How many seconds between each press. 0.0 by default, for no pause between presses.
        @return: None
        """
        if type(keys) == str:
            if len(keys) > 1:
                keys = keys.lower()
            keys = [keys]  # If keys is 'enter', convert it to ['enter'].
        else:
            lower_keys = []
            for s in keys:
                if len(s) > 1:
                    lower_keys.append(s.lower())
                else:
                    lower_keys.append(s)
            keys = lower_keys
        for i in range(presses):
            for k in keys:
                self.universal_interface.perform_key_action(k, KEYBOARD_MAPPING, False)
                self.universal_interface.perform_key_action(k, KEYBOARD_MAPPING, True)
            time.sleep(float(interval))

    def startTyping(self, message, interval=0.0):
        """
        Type the message by sending keyboard key presses.
        @param message: The string to be typed.
        @param interval: How many seconds to wait in between each key press.
        @return: None
        """
        for c in message:
            if len(c) > 1:
                c = c.lower()
            self.press(c)
            time.sleep(float(interval))

    def main(self, data, interval):
        self.universal_interface.update_keyboard_mapping(KEYBOARD_MAPPING)
        self.startTyping(data, interval)
