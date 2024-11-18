from abc import ABC

from evdev import UInput, ecodes as e

from os_Interfaces.universal_interface import UniversalInterface, isShiftCharacter


class LinuxInterface(UniversalInterface, ABC):
    def update_keyboard_mapping(self, keyboard_mapping: dict):
        keyboard_mapping.update({
            'backspace': e.KEY_BACKSPACE,
            '\b': e.KEY_BACKSPACE,
            '\r': e.KEY_ENTER,
            'super': e.KEY_LEFTMETA,
            'tab': e.KEY_TAB,
            '\t': e.KEY_TAB,
            'clear': e.KEY_CLEAR,
            'enter': e.KEY_ENTER,
            '\n': e.KEY_ENTER,
            'return': e.KEY_ENTER,
            'shift': e.KEY_LEFTSHIFT,
            'ctrl': e.KEY_LEFTCTRL,
            'alt': e.KEY_LEFTALT,
            'pause': e.KEY_PAUSE,
            'capslock': e.KEY_CAPSLOCK,
            'hanguel': e.KEY_HANGEUL,
            'hangul': e.KEY_HANGUEL,
            'hanja': e.KEY_HANJA,
            'esc': e.KEY_ESC,
            'escape': e.KEY_ESC,
            ' ': e.KEY_SPACE,
            'space': e.KEY_SPACE,
            'pgup': e.KEY_PAGEUP,
            'pgdn': e.KEY_PAGEDOWN,
            'pageup': e.KEY_PAGEUP,
            'pagedown': e.KEY_PAGEDOWN,
            'end': e.KEY_END,
            'home': e.KEY_HOME,
            'left': e.KEY_LEFT,
            'up': e.KEY_UP,
            'right': e.KEY_RIGHT,
            'down': e.KEY_DOWN,
            'select': e.KEY_SELECT,
            'print': e.KEY_PRINT,
            'prtsc': e.KEY_SYSRQ,
            'prtscr': e.KEY_SYSRQ,
            'prntscrn': e.KEY_SYSRQ,
            'printscreen': e.KEY_SYSRQ,
            'insert': e.KEY_INSERT,
            'del': e.KEY_DELETE,
            'a': e.KEY_A,
            'b': e.KEY_B,
            'c': e.KEY_C,
            'd': e.KEY_D,
            'e': e.KEY_E,
            'f': e.KEY_F,
            'g': e.KEY_G,
            'h': e.KEY_H,
            'i': e.KEY_I,
            'j': e.KEY_J,
            'k': e.KEY_K,
            'l': e.KEY_L,
            'm': e.KEY_M,
            'n': e.KEY_N,
            'o': e.KEY_O,
            'p': e.KEY_P,
            'q': e.KEY_Q,
            'r': e.KEY_R,
            's': e.KEY_S,
            't': e.KEY_T,
            'u': e.KEY_U,
            'v': e.KEY_V,
            'w': e.KEY_W,
            'x': e.KEY_X,
            'y': e.KEY_Y,
            'z': e.KEY_Z,
            '`': e.KEY_GRAVE,
            '1': e.KEY_1,
            '2': e.KEY_2,
            '3': e.KEY_3,
            '4': e.KEY_4,
            '5': e.KEY_5,
            '6': e.KEY_6,
            '7': e.KEY_7,
            '8': e.KEY_8,
            '9': e.KEY_9,
            '0': e.KEY_0,
            '-': e.KEY_MINUS,
            '=': e.KEY_EQUAL,
            '[': e.KEY_LEFTBRACE,
            ']': e.KEY_RIGHTBRACE,
            '\\': e.KEY_BACKSLASH,
            ';': e.KEY_SEMICOLON,
            "'": e.KEY_APOSTROPHE,
            ',': e.KEY_COMMA,
            '.': e.KEY_DOT,
            '/': e.KEY_SLASH,
            'f1': e.KEY_F1,
            'f2': e.KEY_F2,
            'f3': e.KEY_F3,
            'f4': e.KEY_F4,
            'f5': e.KEY_F5,
            'f6': e.KEY_F6,
            'f7': e.KEY_F7,
            'f8': e.KEY_F8,
            'f9': e.KEY_F9,
            'f10': e.KEY_F10,
            'f11': e.KEY_F11,
            'f12': e.KEY_F12,
            '!': e.KEY_1,
            '@': e.KEY_2,
            '#': e.KEY_3,
            '$': e.KEY_4,
            '%': e.KEY_5,
            '^': e.KEY_6,
            '&': e.KEY_7,
            '*': e.KEY_8,
            '(': e.KEY_9,
            ')': e.KEY_0,
            '_': e.KEY_MINUS,
            '+': e.KEY_EQUAL,
            '{': e.KEY_LEFTBRACE,
            '}': e.KEY_RIGHTBRACE,
            '|': e.KEY_BACKSLASH,
            ':': e.KEY_SEMICOLON,
            '"': e.KEY_APOSTROPHE,
            '<': e.KEY_COMMA,
            '>': e.KEY_DOT,
            '?': e.KEY_SLASH,
            '~': e.KEY_GRAVE,

       })


    def perform_key_action(self, key, keyboard_mapping: dict, up=True):
        key = str(key)
        needs_shift = isShiftCharacter(key)
        if needs_shift:
            key = key.lower()
            self.ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
        else:
            self.ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 0)
        self.ui.syn()

        if up:
            self.ui.write(e.EV_KEY, keyboard_mapping[key], 0)
        else:
            self.ui.write(e.EV_KEY, keyboard_mapping[key], 1)
        self.ui.syn()

        # release shift
        if needs_shift:
            self.ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 0)
            self.ui.syn()
        
