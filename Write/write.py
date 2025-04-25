import os

# Consts
fn = ""
l = []  # noqa
cwd = os.getcwd()
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
        for i in range(len(l)):
            print(l[i])
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
