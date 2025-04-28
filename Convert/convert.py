import os

p = (
    ".md",
    ".mmd",
    ".rmd",
    ".txt",
    ".rst",
    ".org",
    ".adoc",
    ".mediawiki",
    ".dokuwiki",
    ".viki",
    ".opml",
    ".html",
    ".xhtml",
    ".xml",
    ".fb2",
    ".epub",
    ".odt",
    ".docx",
    ".pptx",
    ".tex",
    ".pdf",
    ".json",
    ".jats",
    ".man",
    ".haddock",
    ".mdown",
    ".rst",
)
f = (
    ".avi",
    ".mp4",
    ".mov",
    ".mkv",
    ".webm",
    ".flv",
    ".wmv",
    ".mpeg",
    ".mpg",
    ".mp3",
    ".aac",
    ".wav",
    ".ogg",
    ".flac",
    ".opus",
    ".ac3",
    ".dts",
    ".m4a",
    ".3gp",
    ".hevc",
    ".h264",
    ".vob",
    ".asf",
    ".ts",
    ".rm",
    ".swf",
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".gif",
    ".tiff",
    ".tif",
    ".raw",
    ".yuv",
)
while True:
    command = input("CMDConvert > ")
    if command == ":c":
        fn = input("Name of file to convert > ")
        fnn = input("New File name > ")
        _, extension = os.path.splitext()
        if extension in p:
            os.system(rf".\pandoc.exe {fn} -o {fnn}")
        elif extension in f:
            os.system(rf".\ffmpeg.exe -i {fn} {fnn}")
        else:
            print("Unsupported File Type")
    elif command == ":q":
        quit()
    elif command == ":i":
        os.system("tar -xf dependencies.zip")
        if not Exception:
            print("Install Succes!")
