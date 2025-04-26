import os

import colorama
from colorama import Style
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from rich.console import Console
from rich.markdown import Markdown

# Consts
fn = ""
fnexists = False
l = []  # noqa
cwd = os.getcwd()
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = Style.RESET_ALL
colorama.init(autoreset=True)
console = Console()


class View:
    def txt():
        count = 0
        for i in range(len(l)):
            print(l[i])
            count += 1
            if count % 20 == 0:
                input("Press Enter to Continue...")

    def py():
        count = 0
        for i in range(len(l)):
            print(highlight(l[i], PythonLexer(), TerminalFormatter()), end="")
            count += 1
            if count % 20 == 0:
                input("Press Any Key to Continue...")

    def md():
        text = "\n".join(l)
        lines = text.splitlines()
        console = Console()
        for i in range(0, len(lines), 20):
            chunk = "\n".join(lines[i : i + 20])
            markdown = Markdown(chunk)
            console.print(markdown)
            if i + 20 < len(lines):
                input("Press Any Key to Continue")
                print("\n" * 20)


while True:

    def save():
        os.system(f"echo {l[0]} > {fn}")
        for i in range(1, len(l)):
            os.system(f"echo {l[i]} >> {fn}")

    command = input("CMDWrite > ")
    if command == ":w":
        winput = input("Insert text > ")
        l.append(winput)
    elif command == ":v":
        _, extension = os.path.splitext(fn)
        if extension == ".txt":
            View.txt()
        elif extension == ".md":
            View.md()
        elif command == ":py":
            pyinput = input("What command do you want to run in python?: ")
            eval(pyinput)
        else:
            View.txt()
    elif command == ":sa":
        fn = input("Insert filename > ")
        save()
        size = os.path.getsize(fn)
        print(rf'"{cwd}\{fn}" {len(l)}L, {size}B written')
        fnexists = True
    elif command == ":s":
        if not fnexists:
            fn = input("Insert filename > ")
            save()
            size = os.path.getsize(fn)
            print(rf'"{cwd}\{fn}" {len(l)}L, {size}B written')
            fnexists = True
        else:
            save()
            size = os.path.getsize(fn)
            print(rf'"{cwd}\{fn}" {len(l)}L, {size}B written')
    elif command == ":q":
        dywtq = input(
            "If you haven't saved your current file any unsaved changes will be lost, do you want to continue? (Y/N): "
        )
        if dywtq.lower() == "y":
            quit()
        elif dywtq.lower() == "n":
            pass
        else:
            print("Invalid Charachter!")
    elif command == ":q!":
        quit()
    elif command == ":cmd":
        cmdinput = input("What command do you want to run in cmd?: ")
        os.system(cmdinput)
    elif command == ":py":
        pyinput = input("What command do you want to run in python?: ")
        eval(pyinput)
    elif command == ":d":
        delput = int(input("What line do you want to delete?: "))
        l.remove(l[delput - 1])
    elif command == ":e":
        edput = int(input("What line do you want to edit?: "))
        print("Old text: " + l[edput - 1])
        edputext = input("Insert new text > ")
        l[edput - 1] = edputext
    elif command == ":o":
        oput = input("What file do you want to open? (Absolute or relative path): ")
        with open(oput, "r", encoding="utf-8") as f:
            l = f.readlines()  # noqa
        fn = oput
        _, extension = os.path.splitext(fn)
    else:
        print("Invalid Command!")
