### Auto Typist
Have you ever found yourself in a situation where you need to develop an application in a VM environment without any Internet connection and copy-paste is disabled from/to the VM? If you've ever experienced this, you know the pain it can cause, especially when it comes to programming tasks.

Auto Typist is a solution to this problem. It converts texts to keypresses just like typing on a keyboard, except that it can type much faster (500 characters per second).

### How to use
![showcase.gif](static%2Fshowcase.gif)

1. Copy what you want to type to the program.
2. Click start.
3. Move your cursor to the place you want to type.
4. Wait for 3 seconds and the program will start typing.

### Releases
1. Standalone executable (maybe detected as malware by Windows Defender, I'm trying to fix this): https://github.com/yixinliu99/AutoTypist/releases/tag/v1.0.0
2. Clone the repo, and run `python gui.py` to start the program.

### Dependencies
Just python3, no third-party library is used.

### Credits
https://github.com/asweigart/pyautogui
