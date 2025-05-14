import os
import sys

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
console = Console()
d = {
    ":w": "Commands.write()",
    ":v": "Commands.view()",
    ":s": "Commands.save()",
    ":sa": "Commands.saveas()",
    ":q": "Commands.quit()",
    ":d": "Commands.delete()",
    ":e": "Commands.edit()",
    ":o": "Commands.open()",
    ":i": "Commands.insert()",
    ":cmd": "Commands.runcmdcommand()",
    ":py": "Commands.runpycommand()",
}


class View:
    def txt():
        count = 0
        for i in range(len(l)):
            print(l[i])
            count += 1
            if count % 20 == 0:
                input("Press Any Key to Continue...")

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


class Commands:
    @staticmethod
    def saveer():
        global fn
        global fnexists
        global l  # noqa
        os.system(f"echo {l[0]} > {fn}")
        for i in range(1, len(l)):
            os.system(f"echo {l[i]} >> {fn}")

    @staticmethod
    def write():
        global l  # noqa
        winput = input("Insert text > ")
        l.append(winput)

    @staticmethod
    def view():
        _, extension = os.path.splitext(fn)
        if extension == ".txt":
            View.txt()
        elif extension == ".md":
            View.md()
        elif extension == ".py":
            View.py()
        else:
            View.txt()

    @staticmethod
    def saveas():
        global fn
        global fnexists
        global l  # noqa
        fn = input("Insert filename > ")
        Commands.save()
        size = os.path.getsize(fn)
        print(rf'"{cwd}\{fn}" {len(l)}L, {size}B written')
        fnexists = True

    @staticmethod
    def save():
        global fn
        global fnexists
        global l  # noqa
        if not fnexists:
            fn = input("Insert filename > ")
            Commands.saveer()
            size = os.path.getsize(fn)
            print(rf'"{cwd}\{fn}" {len(l)}L, {size}B written')
            fnexists = True
        else:
            Commands.saveer()
            size = os.path.getsize(fn)
            print(rf'"{cwd}\{fn}" {len(l)}L, {size}B written')

    @staticmethod
    def quit():
        dywtq = input(
            "If you haven't saved your current file any unsaved changes will be lost, do you want to continue? (Y/N): "
        )
        if dywtq.lower() == "y":
            sys.exit(0)
        elif dywtq.lower() == "n":
            pass
        else:
            print("Invalid Charachter!")

    @staticmethod
    def quitforced():
        sys.exit(0)

    @staticmethod
    def runcmdcommand():
        cmdinput = input("What command do you want to run in cmd?: ")
        os.system(cmdinput)

    @staticmethod
    def runpycommand():
        pyinput = input("What command do you want to run in python?: ")
        eval(pyinput)

    @staticmethod
    def edit():
        global l  # noqa
        edput = int(input("What line do you want to edit?: "))
        print("Old text: " + l[edput - 1])
        edputext = input("Insert new text > ")
        l[edput - 1] = edputext

    @staticmethod
    def delete():
        global l  # noqa
        delput = int(input("What line do you want to delete?: "))
        del l[delput - 1]

    @staticmethod
    def open():
        global fn
        global fnexists
        global l  # noqa
        oput = input("What file do you want to open? (Absolute or relative path): ")
        with open(oput, "r", encoding="utf-8") as f:
            l = f.readlines()  # noqa
        fn = oput
        fnexists = True
        _, extension = os.path.splitext(fn)

    @staticmethod
    def insert():
        aput = int(input("What line do you want to insert to?: "))
        atext = input("Insert text > ")
        l.insert(aput - 1, atext)


def main():
    while True:
        command = input("CMDWrite > ")
        if command != ":q!":
            try:
                eval(d.get(command))
            except:  # noqa
                print(Exception)
        else:
            sys.exit(0)


if __name__ == "__main__":
    main()
