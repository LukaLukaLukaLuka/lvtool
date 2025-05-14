import os

import typer

app = typer.Typer()
d = {
    "write": 'curl -H "Authorization: token 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" -o write.py "https://raw.githubusercontent.com/LukaLukaLukaLuka/lvtool/refs/heads/master/Write/write.py"',
    "convert": 'curl -H "Authorization: token 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" -o convert.py "https://raw.githubusercontent.com/LukaLukaLukaLuka/lvtool/refs/heads/master/Convert/convert.py"',
}


def searchi(program):
    os.system(d.get(program))


def searchu(program):
    os.system(f"del {program}.py")


@app.command()
def install(programid: str):
    searchi(programid)


@app.command()
def uninstall(programid: str):
    searchu(programid)


if __name__ == "__main__":
    app()
