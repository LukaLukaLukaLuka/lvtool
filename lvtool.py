import os

import typer

app = typer.Typer()
d = {
    "write": "curl -o write.py https://raw.githubusercontent.com/LukaLukaLukaLuka/lvtool/refs/heads/master/Write/write.py?token=GHSAT0AAAAAADAO7UNMJ2WZVYAND4VI7FGA2BETCMQ",
    "convert": "curl -o convert.py https://raw.githubusercontent.com/LukaLukaLukaLuka/lvtool/refs/heads/master/Convert/convert.py?token=GHSAT0AAAAAADAO7UNMS33YNFJJ44KXVUEU2BETD7A",
}


def search(program):
    os.system(d.get(program))


@app.command()
def install(programid: str):
    search(programid)


@app.command()
def placeholder():
    pass


if __name__ == "__main__":
    app()
