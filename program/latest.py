## NewBook Ver. 1.2 c

import sys
import os
try:
    import readline
except ImportError:
    print("<SYS_ERR> The \033[3mreadline\033[0m module is not available on this system. Command history will not be available.")
import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#--FUNCTIONS--#

def menu():
    cmd = "nil"
    while not cmd == "exitp":
        cmd = input("").strip()
        sys.stdout.write("\033[A\033[2K")
        sys.stdout.flush()
        if cmd == "exitp":
            placeholder = "nil"
        else:
            if "<green>" in cmd:
                cmd = cmd.replace("<green>", "")
                print(Fore.GREEN + cmd)
            elif "<blue>" in cmd:
                cmd = cmd.replace("<blue>", "")
                print(Fore.BLUE + cmd)
            elif "<red>" in cmd:
                cmd = cmd.replace("<red>", "")
                print(Fore.RED + cmd)
            elif "<cyan>" in cmd:
                cmd = cmd.replace("<cyan>", "")
                print(Fore.CYAN + cmd)
            elif "<magenta>" in cmd:
                cmd = cmd.replace("<magenta>", "")
                print(Fore.MAGENTA + cmd)
            elif "<yellow>" in cmd:
                cmd = cmd.replace("<yellow>", "")
                print(Fore.YELLOW + cmd)
            elif "<white>" in cmd:
                cmd = cmd.replace("<white>", "")
                print(Fore.WHITE + cmd)
            elif "<black>" in cmd:
                cmd = cmd.replace("<black>", "")
                print(Fore.BLACK + cmd)
            elif "<gray>" in cmd:
                cmd = cmd.replace("<gray>", "")
                print("\033[90m" + cmd + "\033[0m")
            elif "<lgreen>" in cmd:
                cmd = cmd.replace("<lgreen>", "")
                print(Fore.LIGHTGREEN_EX + cmd)
            elif "<lblue>" in cmd:
                cmd = cmd.replace("<lblue>", "")
                print(Fore.LIGHTBLUE_EX + cmd)
            elif "<lred>" in cmd:
                cmd = cmd.replace("<lred>", "")
                print(Fore.LIGHTRED_EX + cmd)
            elif "<lcyan>" in cmd:
                cmd = cmd.replace("<lcyan>", "")
                print(Fore.LIGHTCYAN_EX + cmd)
            elif "<lmagenta>" in cmd:
                cmd = cmd.replace("<lmagenta>", "")
                print(Fore.LIGHTMAGENTA_EX + cmd)
            elif "<lyellow>" in cmd:
                cmd = cmd.replace("<lyellow>", "")
                print(Fore.LIGHTYELLOW_EX + cmd)
            elif "<lwhite>" in cmd:
                cmd = cmd.replace("<lwhite>", "")
                print(Fore.LIGHTWHITE_EX + cmd)
            elif "<lblack>" in cmd:
                cmd = cmd.replace("<lblack>", "")
                print(Fore.LIGHTBLACK_EX + cmd)
            elif "<i>" in cmd:
                cmd = cmd.replace("<i>", "")
                print("\033[3m" + cmd + "\033[0m")
            elif "<bl>" in cmd:
                cmd = cmd.replace("<bl>", "")
                print("\033[5m" + cmd + "\033[0m")
            elif "<d>" in cmd:
                cmd = cmd.replace("<d>", "")
                print("\033[2m" + cmd + "\033[0m")
            elif "<u>" in cmd:
                cmd = cmd.replace("<u>", "")
                print("\033[4m" + cmd + "\033[0m")
            elif "<redacted>" in cmd:
                cmd = cmd.replace("<redacted>", "")
                print("\033[9;90m" + cmd + "\033[0m")
            elif "<encrypt>" in cmd:
                cmd = cmd.replace("<encrypt>", "")
                print("\033[8m" + cmd + "\033[0m")
            elif "<rev>" in cmd:
                cmd = cmd.replace("<rev>", "")
                print("\033[7m" + cmd + "\033[0m")
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
print(Fore.YELLOW + "<SYS> NewBook Ver. 1.2 c")
print(Fore.YELLOW + '<SYS> Type "exitp" at any time to exit the program')
print(Fore.YELLOW + '<SYS> Go to the README.md file to learn how to format your notes!')

try:
    readline.add_history("<cyan> You found me!")
except:
    pass

menu()
clearscreen()
