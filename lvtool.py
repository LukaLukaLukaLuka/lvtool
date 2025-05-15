import os

import typer

app = typer.Typer()
installlinks = {
    "write": 'curl -H "Authorization: token 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" -o write.py "https://raw.githubusercontent.com/LukaLukaLukaLuka/lvtool/refs/heads/master/Write/write.py"',
    "convert": 'curl -H "Authorization: token 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" -o convert.py "https://raw.githubusercontent.com/LukaLukaLukaLuka/lvtool/refs/heads/master/Convert/convert.py"',
}
programinfo = {
    "write": "A simple write program that can be used standalone, but is meant to be imported",
    "convert": "A simple conversion program to convert most file types",
}


def searchinstall(program):
    os.system(installlinks.get(program))


def searchuninstall(program):
    os.system(f"del {program}.py")


def searchsearch(program):
    typer.echo(programinfo.get(program))


@app.command()
def install(programid: str):
    searchinstall(programid)


@app.command()
def uninstall(programid: str):
    searchuninstall(programid)


@app.command()
def search(programid: str):
    searchsearch(programid)


if __name__ == "__main__":
    app()
