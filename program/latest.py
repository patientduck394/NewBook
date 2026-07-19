## Graphite Ver. 2.0 s

import sys
import os
import subprocess
import platform
import time
import threading
import urllib.request # Built-in network handler

import site


user_site_packages = site.getusersitepackages()
if user_site_packages not in sys.path:
    sys.path.append(user_site_packages)

if platform.system() == "Windows":
    import winsound
try:
    import readline
except ImportError:
    pass

try:
    import colorama
    from colorama import Fore, Style
except ImportError:
    # If Colorama is missing, install it cleanly matching your terminal environment
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama", "--user"], 
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import colorama
    from colorama import Fore, Style



try:
    import execjs # type: ignore
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyExecJS", "--user"], 
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import execjs # type: ignore

def play_github_shared_sound(github_url):
    """
    Takes your browser link, changes it to a raw link automatically,
    and streams it so other users hear it cleanly over curl and afplay.
    """
    # Automatically switch the link text to 'raw' if it is a standard web browser permalink
    if "github.com" in github_url and "/blob/" in github_url:
        raw_url = github_url.replace("github.com", "://githubusercontent.com").replace("/blob/", "/")
    else:
        raw_url = github_url

    def worker():
        temp_file = "/tmp/shared_github_sound.wav"
        if platform.system() == "Darwin":
            # Downloads the raw audio bytes silently and plays it natively on their Mac
            os.system(f"curl -s -L '{raw_url}' -o {temp_file}")
            if os.path.exists(temp_file):
                os.system(f"afplay '{temp_file}'")
    
    # Runs on a background daemon thread so your users' terminal text never lags
    threading.Thread(target=worker, daemon=True).start()

def play_ui_sound(sound_name):
    """
    Instantly plays a native Mac system sound in the background.
    Zero installation. Zero internet downloads. Never crashes.
    """
    if platform.system() == "Darwin":
        # The '&' runs it in the background so your typing prompt never lags
        os.system(f"afplay /System/Library/Sounds/{sound_name}.aiff &")

def run_system_boot():
    """
    Safely audits, downloads, and reloads packages internally
    without allowing raw root-level imports to trigger system crashes.
    """
    if platform.system() == "Darwin":
        os.system("defaults write com.apple.Terminal AutoMarkPromptLines -int 0")
        os.system("defaults write com.apple.Terminal ShowLineMarks -int 0")
        print(r"\e[?2004l", end="", flush=True)

    clear_cmd = "cls" if platform.system() == "Windows" else "clear"
    os.system(clear_cmd)

    print("\033[94m======================================\033[0m")
    print("\033[1m       LAUNCHING NEWBOOK UTILITY      \033[0m")
    print("\033[94m======================================\033[0m\n")

    relaunch_needed = False

    # Check Colorama
    print("\033[90m[*] Checking Colorama engine...\033[0m", end="", flush=True)
    time.sleep(0.2)
    try:
        __import__("colorama") # Safe string checker bypass
        print("\033[92m OK\033[0m")
    except ImportError:
        print("\033[93m MISSING\033[0m")
        if platform.system() == "Darwin":
            os.system("afplay /System/Library/Sounds/Basso.aiff &")
        print("\033[33m[!] Automatically acquiring Colorama dependencies...\033[0m")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama", "--user"], 
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        relaunch_needed = True

    # Check PyExecJS
    print("\033[90m[*] Checking JavaScript compiler bridge...\033[0m", end="", flush=True)
    time.sleep(0.2)
    try:
        __import__("execjs") # Safe string checker bypass
        print("\033[92m OK\033[0m")
    except ImportError:
        print("\033[93m MISSING\033[0m")
        if platform.system() == "Darwin":
            os.system("afplay /System/Library/Sounds/Basso.aiff &")
        print("\033[33m[!] Automatically acquiring JavaScript dependencies...\033[0m")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyExecJS", "--user"], 
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        relaunch_needed = True

    # The Hot-Reload Switch: Force terminal to refresh if updates were saved
    if relaunch_needed:
        print("\n\033[93m<SYS> Finalizing packages. Reloading environment...\033[0m")
        time.sleep(0.8)
        
        import importlib
        importlib.invalidate_caches()
        
        python_exe = sys.executable
        script_args = sys.argv
        os.execv(python_exe, [python_exe] + script_args)

    # --- RUN THE TEST COMPILATION ---
    print("\033[90m[*] Spawning internal JavaScript compiler...\033[0m", end="", flush=True)
    time.sleep(0.2)
    try:
        import execjs # type: ignore
        js_context = execjs.compile("""
            function testBoot() { return "Engine Verified"; }
        """)
        if js_context.call("testBoot") == "Engine Verified":
            print("\033[92m OK\033[0m")
    except Exception:
        print("\033[91m TIMEOUT\033[0m")

    print("\033[90m[*] Syncing core interface maps...\033[0m", end="", flush=True)
    time.sleep(0.2)
    if platform.system() == "Darwin":
        os.system("afplay /System/Library/Sounds/Tink.aiff &")
    print("\033[92m OK\033[0m")

    print("\n\033[92m[✓] NewBook Core Active. Entering environment...\033[0m")
    time.sleep(0.6)
    os.system(clear_cmd)

def print_markdown_to_terminal(markdown_text):
    """
    Parses standard Markdown syntax string formatting loops and translates
    them directly into terminal screen Colorama escape styles.
    """
    lines = markdown_text.split(r"\n") # Splits text lines accurately
    
    
    
    for line in lines:
        processed_line = line.strip()
        
        # 1. Parse # Headers -> Bright Cyan Bold
        if processed_line.startswith("# "):
            processed_line = Fore.CYAN + Style.BRIGHT + "▶ " + processed_line[2:].upper()
        # 2. Parse ##  and ### Headers -> Bright White Bold
        elif processed_line.startswith("## "):
            processed_line = Fore.WHITE + Style.BRIGHT + "▷ " + processed_line[3:]
        elif processed_line.startswith("### "):
            processed_line = Fore.WHITE + "▷ " + processed_line[4:]
        # 3. Parse * Bullet points -> Green Bullet Indent
        elif processed_line.startswith("* "):
            processed_line = "  " + Fore.GREEN + "• " + Fore.WHITE + processed_line[2:]
        elif processed_line.startswith("- "):
            processed_line = "  " + Fore.GREEN + "- " + Fore.WHITE + processed_line[2:]
        elif processed_line.startswith("1. "):
            processed_line = "  " + Fore.RED + "1. " + Fore.WHITE + processed_line[3:]
        elif processed_line.startswith("2. "):
            processed_line = "  " + Fore.RED + "2. " + Fore.WHITE + processed_line[3:]
        elif processed_line.startswith("3. "):
            processed_line = "  " + Fore.RED + "3. " + Fore.WHITE + processed_line[3:]
        elif processed_line.startswith("4. "):
            processed_line = "  " + Fore.RED + "4. " + Fore.WHITE + processed_line[3:]
        elif processed_line.startswith("5. "):
            processed_line = "  " + Fore.RED + "5. " + Fore.WHITE + processed_line[3:]
        elif processed_line.startswith("6. "):
            processed_line = "  " + Fore.RED + "6. " + Fore.WHITE + processed_line[3:]
        elif processed_line.startswith("7. "):
            processed_line = "  " + Fore.RED + "7. " + Fore.WHITE + processed_line[3:]
        elif processed_line.startswith("8. "):
            processed_line = "  " + Fore.RED + "8. " + Fore.WHITE + processed_line[3:]
        elif processed_line.startswith("9. "):
            processed_line = "  " + Fore.RED + "9. " + Fore.WHITE + processed_line[3:]
        elif processed_line.startswith("10. "):
            processed_line = "  " + Fore.RED + "10. " + Fore.WHITE + processed_line[4:]
            
        # 4. Parse Inline **Bold** markers using colorama replacements
        while "**" in processed_line:
            processed_line = processed_line.replace("**", Fore.YELLOW + Style.BRIGHT, 1).replace("**", Style.RESET_ALL + Fore.WHITE, 1)
            
        # 5. Parse Inline *Italic* markers (we can use Underline style for italics in terminal layouts)
        while "*" in processed_line:
            processed_line = processed_line.replace("*", "\033[4m", 1).replace("*", "\033[24m", 1)
            
        # 6. Parse Inline `Code` markers -> Magenta text style
        while "`" in processed_line:
            processed_line = processed_line.replace("`", Fore.MAGENTA, 1).replace("`", Fore.WHITE, 1)

        print(Fore.WHITE + processed_line)
        
    

# Now it is completely safe to import them cleanly for your application logic
import colorama
from colorama import Fore, Style


colorama.init(autoreset=True)


# ----------------------------------------------------
# YOUR MAIN NEWBOOK CORE LOGIC STARTS DOWN HERE
# ----------------------------------------------------
#print("NewBook Engine v1.0 Active.")
# cmd = input("NewBook > ") ...


#--VARIABLES--#

notes_history = []
tags = ["<green>", "<blue>", "<red>", "<cyan>", "<magenta>", "<yellow>", "<white>", "<black>", "<orange>", "<gray>", "<lgreen>", "<lblue>", "<lred>", "<lcyan>", "<lmagenta>", "<lyellow>", "<lwhite>", "<lblack>", "<lorange>", "<lgray>", "<i>","<bl>", "<d>", "<u>", "<redacted>", "<encrypt>", "<rev>", "<ov>", "<link>","<bluelink>", "<wtitle.>", "<clrscn.>", "^.","v.", "^x.", "vx.", "<color>","<b>", "<.validtag>", "<.help>","<wd>"]
history_index = -1
saved_current = ""

#--FUNCTIONS--#



def play_system_alert(sound_type="error"):
    """
    Plays an offline native system sound based on the host Operating System.
    Supported types: 'error', 'success', 'warning'
    """
    current_os = platform.system()
    
    # ----------------------------------------------------
    # MAC OPERATING SYSTEM AUDIO LOGIC
    # ----------------------------------------------------
    if current_os == "Darwin":  # 'Darwin' is Python's internal name for macOS
        if sound_type == "error":
            os.system("afplay /System/Library/Sounds/Basso.aiff &")
        elif sound_type == "success":
            os.system("afplay /System/Library/Sounds/Glass.aiff &")
        elif sound_type == "warning":
            os.system("afplay /System/Library/Sounds/Frog.aiff &")
        elif sound_type == "info":
            os.system("afplay /System/Library/Sounds/Ping.aiff &")
            
    # ----------------------------------------------------
    # WINDOWS OPERATING SYSTEM AUDIO LOGIC
    # ----------------------------------------------------
    elif current_os == "Windows":
        if sound_type == "error":
            # Plays the hardware standard error chord frequency
            winsound.MessageBeep(winsound.MB_ICONHAND)
        elif sound_type == "success":
            # Plays the standard system asterisk confirmation sound
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        elif sound_type == "warning":
            # Plays the standard exclamation hazard notification beep
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        elif sound_type == "info":
            winsound.MessageBeep(winsound.MB_OK)
            
    # ----------------------------------------------------
    # LINUX OPERATING SYSTEM AUDIO LOGIC (FALLBACK)
    # ----------------------------------------------------
    else:
        # Linux doesn't share a standardized sound system, so we drop back to the standard ANSI bell
        print("\a", end="", flush=True)

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
        notes_history.append(cmd + "\n")
        if "^." or "v." not in cmd:
            sys.stdout.write("\033[A\033[2K")
        sys.stdout.flush()
        if cmd == "exitp":
            placeholder = "nil"
        elif "<.validtag>" in cmd:
            cleaned_cmd = cmd.replace("<.validtag>", "")
            cleaned_cmd = cleaned_cmd.strip()
            if cleaned_cmd in tags:
                play_system_alert("success")
                print(Fore.GREEN + "<SYS-HELP> Valid tag")
            else:
                play_system_alert("error")
                print(Fore.RED + "<SYS-HELP> Invalid tag")
        elif cmd == "<clrscn.>":
            clearscreen()
        elif cmd == "restartp":
            print("\033[93m<SYS> Re-initializing NewBook environment...\033[0m")
            time.sleep(0.5) # Brief visual delay to make the restart feel clean
            
            # 1. Grab the active path to your Python interpreter engine executable
            python_exe = sys.executable
            
            # 2. Grab the precise path array of your currently running script file
            script_args = sys.argv
            
            # 3. Force-replace the active system process with a fresh execution boot
            os.execv(python_exe, [python_exe] + script_args)
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
            elif "<.help>" in cmd:
                play_system_alert("info")
                print(Fore.YELLOW + '<SYS-HELP> Type exitp to exit.')
                print(Fore.YELLOW + '           Go to the GitHub repository for formatting help!')
            elif "<wd>" in cmd:
                cleaned_cmd = cmd.replace("<wd>", "")
                cleaned_cmd = cleaned_cmd.lstrip()
                print_markdown_to_terminal(cleaned_cmd)
            elif "<calc>" in cmd:
                cleaned_cmd = cmd.replace("<calc>", "")
                cleaned_cmd = cleaned_cmd.lstrip()
                cmd_list = cleaned_cmd.split(" ")
                calcvar1 = int(cmd_list[0])
                calcoperation = cmd_list[1]
                calcvar2 = int(cmd_list[2])
                if calcoperation == "+":
                    print(Fore.GREEN + "<SYS-CALC> Answer: " + str((calcvar1 + calcvar2)))
                elif calcoperation == "-":
                    print(Fore.GREEN + "<SYS-CALC> Answer: " + str((calcvar1 - calcvar2)))
                elif calcoperation == "*":
                    print(Fore.GREEN + "<SYS-CALC> Answer: " + str((calcvar1 * calcvar2)))
                elif calcoperation == "/":
                    print(Fore.GREEN + "<SYS-CALC> Answer: " + str((calcvar1 / calcvar2)))
                elif calcoperation == "^":
                    print(Fore.GREEN + "<SYS-CALC> Answer: " + str((calcvar1 ^ calcvar2)))
                elif calcoperation == "%":
                    print(Fore.GREEN + "<SYS-CALC> Answer: " + str((calcvar1 + calcvar2)))
                else:
                    print(Fore.RED + "<SYS-CALC> Invalid calculation.")
                    print(Fore.RED + "           Make sure to use allowed operations")
                    print(Fore.RED + "           and write operations like 1 + 1 instead of 1+1")
                    print(Fore.RED + "           so the engine can detect the first number, calculation, and second number properly.")
            elif "<save.>" in cmd:
                cleaned_cmd = cmd.replace("<save.>", "")
                cleaned_cmd = cleaned_cmd.lstrip()
                with open("history.txt", "w", encoding="utf-8") as file:
                    # writelines() takes a list of strings and streams them straight into the file.
                    # Because we added '\n' to each item, they will stack beautifully into real lines!
                    file.writelines(notes_history)
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

def disable_apple_terminal_marks():
    """
    Detects if the user is running macOS and automatically executes system shell
    overrides to turn off visual prompt marks and bracketed mode.
    """
    if platform.system() == "Darwin": # Checks if user is on a Mac
        # 1. Disables the visual left/right bracket prompt tracking lines permanently
        os.system("defaults write com.apple.Terminal AutoMarkPromptLines -bool NO")
        
        # 2. Sends a direct ANSI string sequence to turn off the current session's bracketed paste mode
        print(r"\e[?2004l", end="", flush=True)

#--STARTUP--#


run_system_boot()
import colorama
from colorama import Fore, Style
import execjs # type: ignore

colorama.init(autoreset=True)

disable_apple_terminal_marks()
clearscreen()

print(Fore.YELLOW + '<SYS> Graphite Ver. 2.0 s')
print(Fore.YELLOW + '      Type "exitp" at any time to exit the program')
print(Fore.YELLOW + '      Go to the README.md file to learn how to format your notes!')
print(Fore.YELLOW + '      Type <.help> at any time for help!')
print(Fore.YELLOW + '      Type restartp at any time to restart the program!')
print(Fore.YELLOW + '      DID YOU KNOW: Graphite used to be called NewBook but had to be changed because of confusion with another website?')



menu()
clearscreen()
