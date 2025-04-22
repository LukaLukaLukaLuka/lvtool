import os

fn = ""


def compare_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        if f1.read() == f2.read():
            return True  # noqa
        else:
            return False  # noqa


while True:
    command = input("CMDWrite > ")
    if command == ":w":
        a = input("Insert text > ")
        os.system(f"echo {a} >> write.~wr")
    elif command == ":v":
        try:
            os.system("type write.~wr")  # noqa
        except FileNotFoundError:
            print("You must write something in the file before you can view it")  # noqa
    elif command == ":sa":
        fn = input("Insert filename > ")
        os.system(f"type write.~wr > {fn}")
    elif command == ":s":
        if not fn:
            print("You must use the :sa ( Save as ) because there is no existing file")
        else:
            os.system(f"type write.~wr > {fn}")
    elif command == ":q":
        try:
            a = compare_files("write.~wr", fn)
            if a:
                quit()
            else:
                print("File not saved. To override this failsafe use :q!")
        except FileNotFoundError:
            quit()
    elif command == ":q!":
        quit()
    elif command == ":ct":
        try:
            os.system("del write.~wr")
        except FileNotFoundError:
            pass
        finally:
            os.system(r".\mfl.bat write.~wr")
    elif command == ":o":
        a = input("Insert file to open ( Relative or Absolute Path ) > ")
        fn = a
        print(fn)
