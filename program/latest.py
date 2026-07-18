## NewBook Ver. 1.5 c

import sys
import os
try:
    import readline
except ImportError:
    pass
import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#--VARIABLES--#

notes_history = []     
history_index = -1     
saved_current = ""     

#--FUNCTIONS--#

def menu():
    """
    The code with the main formatting script.
    Params:
        null.
    What it does:
        Formats strings inputted by the user and is the main script.
    """
    cmd = "nil"
    while not cmd == "exitp":
        cmd = input("")
        if "^." or "v." not in cmd:
            sys.stdout.write("\033[A\033[2K")
        sys.stdout.flush()
        if cmd == "exitp":
            placeholder = "nil"
        elif cmd == "<clrscn.>":
            clearscreen()
        else:
            if "<green>" in cmd:
                cmd = cmd.replace("<green>", "")
                cmd = cmd.lstrip()
                print(Fore.GREEN + cmd)
            elif "<blue>" in cmd:
                cmd = cmd.replace("<blue>", "")
                cmd = cmd.lstrip()
                print(Fore.BLUE + cmd)
            elif "<red>" in cmd:
                cmd = cmd.replace("<red>", "")
                cmd = cmd.lstrip()
                print(Fore.RED + cmd)
            elif "<cyan>" in cmd:
                cmd = cmd.replace("<cyan>", "")
                cmd = cmd.lstrip()
                print(Fore.CYAN + cmd)
            elif "<magenta>" in cmd:
                cmd = cmd.replace("<magenta>", "")
                cmd = cmd.lstrip()
                print(Fore.MAGENTA + cmd)
            elif "<yellow>" in cmd:
                cmd = cmd.replace("<yellow>", "")
                cmd = cmd.lstrip()
                print(Fore.YELLOW + cmd)
            elif "<white>" in cmd:
                cmd = cmd.replace("<white>", "")
                cmd = cmd.lstrip()
                print(Fore.WHITE + cmd)
            elif "<black>" in cmd:
                cmd = cmd.replace("<black>", "")
                cmd = cmd.lstrip()
                print(Fore.BLACK + cmd)
            elif "<orange>" in cmd:
                cmd = cmd.replace("<orange>", "")
                cmd = cmd.lstrip()
                print("\033[38;5;208m" + cmd)
            elif "<gray>" in cmd:
                cmd = cmd.replace("<gray>", "")
                cmd = cmd.lstrip()
                print("\033[90m" + cmd + "\033[0m")
            elif "<lgreen>" in cmd:
                cmd = cmd.replace("<lgreen>", "")
                cmd = cmd.lstrip()
                print(Fore.LIGHTGREEN_EX + cmd)
            elif "<lblue>" in cmd:
                cmd = cmd.replace("<lblue>", "")
                cmd = cmd.lstrip()
                print(Fore.LIGHTBLUE_EX + cmd)
            elif "<lred>" in cmd:
                cmd = cmd.replace("<lred>", "")
                cmd = cmd.lstrip()
                print(Fore.LIGHTRED_EX + cmd)
            elif "<lcyan>" in cmd:
                cmd = cmd.replace("<lcyan>", "")
                cmd = cmd.lstrip()
                print(Fore.LIGHTCYAN_EX + cmd)
            elif "<lmagenta>" in cmd:
                cmd = cmd.replace("<lmagenta>", "")
                cmd = cmd.lstrip()
                print(Fore.LIGHTMAGENTA_EX + cmd)
            elif "<lyellow>" in cmd:
                cmd = cmd.replace("<lyellow>", "")
                cmd = cmd.lstrip()
                print(Fore.LIGHTYELLOW_EX + cmd)
            elif "<lwhite>" in cmd:
                cmd = cmd.replace("<lwhite>", "")
                cmd = cmd.lstrip()
                print(Fore.LIGHTWHITE_EX + cmd)
            elif "<lblack>" in cmd:
                cmd = cmd.replace("<lblack>", "")
                cmd = cmd.lstrip()
                print(Fore.LIGHTBLACK_EX + cmd)
            elif "<lorange>" in cmd:
                cmd = cmd.replace("<lorange>", "")
                cmd = cmd.lstrip()
                print("\033[38;5;215m" + cmd)
            elif "<lgray>" in cmd:
                cmd = cmd.replace("<lgray>", "")
                cmd = cmd.lstrip()
                print("\033[38;5;246m" + cmd)
            elif "<i>" in cmd:
                cmd = cmd.replace("<i>", "")
                cmd = cmd.lstrip()
                print("\033[3m" + cmd + "\033[0m")
            elif "<bl>" in cmd:
                cmd = cmd.replace("<bl>", "")
                cmd = cmd.lstrip()
                print("\033[5m" + cmd + "\033[0m")
            elif "<d>" in cmd:
                cmd = cmd.replace("<d>", "")
                cmd = cmd.lstrip()
                print("\033[2m" + cmd + "\033[0m")
            elif "<u>" in cmd:
                cmd = cmd.replace("<u>", "")
                cmd = cmd.lstrip()
                print("\033[4m" + cmd + "\033[0m")
            elif "<redacted>" in cmd:
                cmd = cmd.replace("<redacted>", "")
                cmd = cmd.lstrip()
                print("\033[9;90m" + cmd + "\033[0m")
            elif "<encrypt>" in cmd:
                cmd = cmd.replace("<encrypt>", "")
                cmd = cmd.lstrip()
                print("\033[8m" + cmd + "\033[0m")
            elif "<rev>" in cmd:
                cmd = cmd.replace("<rev>", "")
                cmd = cmd.lstrip()
                print("\033[7m" + cmd + "\033[0m")
            elif "<ov>" in cmd:
                cmd = cmd.replace("<ov>", "")
                cmd = cmd.lstrip()
                print("\033[53m" + cmd + "\033[0m")
            elif "<link>" in cmd:
                cleaned_cmd = cmd.replace("<link>", "")
                cleaned_cmd = cleaned_cmd.lstrip()
                cmd_list = cleaned_cmd.split(" ")
                link = cmd_list[0]
                linkitems = cmd_list[1:]
                print(f"\033]8;;{link}\a{' '.join(linkitems)}\033]8;;\a")
            elif "<bluelink>" in cmd:
                cleaned_cmd = cmd.replace("<bluelink>", "")
                cleaned_cmd = cleaned_cmd.lstrip()
                cmd_list = cleaned_cmd.split(" ")
                link = cmd_list[0]
                linkitems = cmd_list[1:]
                print(Fore.BLUE + f"\033]8;;{link}\a{' '.join(linkitems)}\033]8;;\a")
            elif "<wtitle.>" in cmd:
                cmd = cmd.replace("<wtitle.>", "")
                cmd = cmd.lstrip()
                sys.stdout.write(f"\033]0;{cmd}\a")
                sys.stdout.flush()
            elif "^." in cmd:
                cmd = cmd.replace("^.", "")
                sys.stdout.write("\033[1A")
            elif "v." in cmd:
                cmd = cmd.replace("v.", "")
                sys.stdout.write("\033[1B")
            elif "^x." in cmd:
                cmd = cmd.replace("^x.", "")
                sys.stdout.write("\033[1A")
                sys.stdout.write("\033[2K")
            elif "vx." in cmd:
                cmd = cmd.replace("vx.", "")
                sys.stdout.write("\033[1B")
                sys.stdout.write("\033[2K")
            elif "<color>" in cmd:
                cleaned_cmd = cmd.replace("<color>", "")
                cleaned_cmd = cleaned_cmd.lstrip()
                cmd_list = cleaned_cmd.split(" ")
                color1 = cmd_list[0]
                color2 = cmd_list[1]
                color3 = cmd_list[2]
                colortext = cmd_list[3:]
                cleancolortext = " ".join(colortext)
                print(str(f"\x1b[38;2;{color1};{color2};{color3}m{cleancolortext}\x1b[0m"))
            elif "<b>" in cmd:
                cleaned_cmd = cmd.replace("<b>", "")
                cleaned_cmd = cleaned_cmd.lstrip()
                print(f"\033[1m" + cleaned_cmd + "\033[0m")
            else:
                print(cmd)


def clearscreen():
    # 'nt' means Windows, 'posix' means Mac or Linux
    if os.name == 'nt':
        # Windows requires running through cmd because 'cls' is a built-in shell command
        subprocess.run(['cmd', '/c', 'cls'])
    else:
        # Mac and Linux run the 'clear' executable directly
        subprocess.run(['clear'])

#--STARTUP--#

clearscreen()
print(Fore.YELLOW + '<SYS> NewBook Ver. 1.5 c')
print(Fore.YELLOW + '<SYS> Type "exitp" at any time to exit the program')
print(Fore.YELLOW + '<SYS> Go to the README.md file to learn how to format your notes!')

menu()
clearscreen()
