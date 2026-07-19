# NewBook
A notepad-style software that can be used inside your terminal! Supports Mac, Windows, and Linux. <br>
Must have the Colorama library to function. (requires install)<br>
<br>
If you're using a Unix-like operating system (Linux, macOS, and WSL), the `readline` library will work fine. <br>
The readline module does not work on Windows. (So, the history feature accessed by pressing the up arrow will not work if you're on Windows).

# Formatting
Quick note: the tags cannot be used in combination. <br>
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
<b> # Makes text bold.
<encrypt> # Makes text invisible (compatible with readline history!)
<rev> # Flips the text color and the background color
<ov> # Adds an overline (underline that is on the top). (❌🍏)
<link> # Formats a link (first message is the link, second is the text (separated by spaces)). (❌🍏)
<color> # Allows you to change text to a custom color. (first 3 parameters are RGB and the rest is text)
```
There are also hybrid tags which format the text AND change the color:
```python
<redacted> # Makes text gray and has a strikethrough. (the strikethrough does not work on Mac ⚠️🍏)
<bluelink> # If you added <blue> and <link> together!
```
There are also system tags which perform system actions:
```python
<wtitle.> # Changes the window name of the terminal. (partly works on Mac ⚠️🍏)
^. # Moves the cursor up (beta)
v. # Moves the cursor down. (beta)
^x. # Moves the cursor up AND removes the line it moved to.
vx. # Moves the cursor down AND removes the line it moved to.
<clrscn.> # Clears the terminal. (also removes the system messages).
```
There are also help tags which can help you in certain ways:
```python
<.help> # Shows useful help information.
<.validtag> # Sends a success/error help message if the tag next to it is a valid tag.
```
NewBook also has its own version of Markdown, called Writedown:
```javascript
<wd> // Text after this tag is formatted in Writedown.
*Example Text* // Makes text underlined.
**Example Text** // Makes text bold and yellow.
`Example Text` // Makes text magenta/purple.
* Example Text // Makes text into a bulleted list.
- Example Text // Makes text into an unordered list.
1. Example Text // Makes text into a numbered list. (There are numbered versions of this tag through 10).
```
More tags will be released in version 1.7, so stay tuned!<br>
Happy notetaking!
