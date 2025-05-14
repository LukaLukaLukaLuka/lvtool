import os

import typer

app = typer.Typer()
d = {
    "write": "curl -o write.py https://raw.githubusercontent.com/LukaLukaLukaLuka/lvtool/refs/heads/master/Write/write.py?token=GHSAT0AAAAAADAO7UNMJ2WZVYAND4VI7FGA2BETCMQ",
    "convert": "curl -o convert.py https://raw.githubusercontent.com/LukaLukaLukaLuka/lvtool/refs/heads/master/Convert/convert.py?token=GHSAT0AAAAAADAO7UNMS33YNFJJ44KXVUEU2BETD7A",
}


def searchi(program):
    os.system(d.get(program))


def searchu(program):
    os.system(f"del {program}.py")


@app.command()
def install(programid: str):
    searchi(programid)


app.command()


def uninstall(programid: str):
    searchu(programid)


if __name__ == "__main__":
    app()
