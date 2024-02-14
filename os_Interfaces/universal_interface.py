import sys
import abc



class UniversalInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'update_keyboard_mapping') and
                callable(subclass.update_keyboard_mapping) and
                hasattr(subclass, 'perform_key_action') and
                callable(subclass.perform_key_action) or
                NotImplemented)

    @abc.abstractmethod
    def update_keyboard_mapping(self, keyboard_mapping: dict):
        raise NotImplementedError

    @abc.abstractmethod
    def perform_key_action(self, key, keyboard_mapping: dict, action):
        raise NotImplementedError


def isShiftCharacter(character):
    """
    Returns True if the ``character`` is a keyboard key that would require the shift key to be held down, such as
    uppercase letters or the symbols on the keyboard's number row.
    """
    # NOTE TODO - This will be different for non-qwerty keyboards.
    # SOURCE https://github.com/asweigart/pyautogui/blob/b4255d0be42c377154c7d92337d7f8515fc63234/pyautogui/__init__.py#L526
    return character.isupper() or character in set('~!@#$%^&*()_+{}|:"<>?')


if sys.platform == "win32":
    from os_Interfaces._win32 import Win32Interface as UniversalInterface
# elif sys.platform == 'x11':
#     from _linux import LinuxInterface as UniversalInterface
else:
    raise NotImplementedError("Unsupported operating system")
