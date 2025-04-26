import os

from colorama import Fore, Style

# Consts
fn = ""
fnexists = False
l = []  # noqa
cwd = os.getcwd()
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = Style.RESET_ALL


class View:
    def md():
        def printst(text):
            return md_bold(md_italic(text))

        def md_bold(line):
            out = ""
            bold = False
            i = 0
            while i < len(line):
                if line[i : i + 2] == "**":
                    out += BOLD if not bold else RESET
                    bold = not bold
                    i += 2
                else:
                    out += line[i]
                    i += 1
            return out

        def md_italic(line):
            out = ""
            italic = False
            i = 0
            while i < len(line):
                if line[i : i + 1] == "*":
                    out += ITALIC if not italic else RESET
                    italic = not italic
                    i += 1
                else:
                    out += line[i]
                    i += 1
            return out

        for i in range(len(l)):
            if l[i].lstrip().startswith("#"):
                print(Fore.GREEN + l[i])
            elif l[i].lstrip().startswith("---") and l[i].lstrip().endswith("---"):
                print(Fore.BLUE + l[i])
            else:
                print(printst(Fore.WHITE + l[i]))

    def txt():
        for i in range(len(l)):
            print(Fore.WHITE + l[i])


while True:

    def save():
        os.system(f"echo {l[0]} > {fn}")
        for i in range(1, len(l)):
            os.system(f"echo {l[i]} >> {fn}")

    command = input(Fore.WHITE + "CMDWrite > ")
    if command == ":w":
        winput = input("Insert text > ")
        l.append(winput)
    elif command == ":v":
        _, extension = os.path.splitext(fn)
        if extension == ".txt":
            View.txt()
        elif extension == ".md":
            View.md()
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
    else:
        print(
            "Invalid Command! Please refer to the manual (featurelist.md) for the list of commands"
        )
