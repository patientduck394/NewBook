# NewBook
A notepad-style software that can be used inside your terminal! Supports Mac, Windows, and Linux. <br>
Must have the Colorama library to function. (requires install)<br>
<br>
If you're using a Unix-like operating system (Linux, macOS, and WSL), the `readline` library will work fine. If you are not using a Unix-like operating system, then an error message with the visible tag `<SYS-ERR>` will say `The readline module is not available on this system. Command history will not be available.` This will be updated soon and will be put in this `README.md` file instead of the terminal.

# Formatting
Quick note: the tags cannot be used in combination and must be used like this: `<green>Green text!` for this version. <br>
Tags that cannot be used in the Mac terminal correctly will be labeled with ❌🍏. <br>
Since some tags use unsupported ANSI codes, some are unusable for certain platforms and will be labeled accordingly. <br>
<br>
Use these tags for colored text:
```python
<green> # Makes text green.
<blue> # Makes text blue.
<red> # Makes text red.
<cyan> # Makes text cyan.
<magenta> # Makes text magenta.
<yellow> # Makes text yellow.
<white> # Makes text white.
<black> # Makes text black.
```
There is also a collection of other tags for lighter colors:
```python
<lgreen> # Makes text light-green.
<lblue> # Makes text light-blue.
<lred> # Makes text light-red.
<lcyan> # Makes text light-cyan.
<lmagenta> # Makes text light-magenta.
<lyellow> # Makes text light-yellow.
<lwhite> # Makes text light-white.
<lblack> # Makes text light-black.
```
There are also tags for formatting text and not changing the color:
```python
<i> # Makes text italic. (❌🍏)
<bl> # Makes text blink.
<d> # Dims text.
<u> # Underlines text.
<encrypt> # Makes text invisible (compatible with readline history!)
<rev> # Flips the text color and the background color
```
There are also hybrid tags which format the text AND change the color:
```python
<redacted> # Makes text gray and has a strikethrough. (❌🍏)
```
More tags will be released in version 1.2, so stay tuned!<br>
Happy notetaking!
