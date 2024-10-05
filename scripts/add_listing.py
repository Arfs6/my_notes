#! /usr/bin/env python3
"""
This script appends a list of directories and
html files to a `index.html` file.
"""

from typing import List, Tuple
import os
import sys
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """An HTML parser for getting title and checking
    the position of </body>
    """

    def handle_starttag(self, tag, attr):
        """Looks for the title tag."""
        if tag.lower() == "title":
            self._title = True

    def handle_data(self, data):
        """Saves the title text"""
        if hasattr(self, "_title"):
            self.title = data
            del self._title

    def handle_endtag(self, tag):
        """Saves the position of </body>"""
        if tag.lower() == "body":
            self.endBodyPos = self.getpos()


def getFilesAndDirs(path: str):
    """Returns all the html files and valid directories."""
    ls = os.listdir(path)
    files = []
    dirs = []
    for i in ls:
        if not os.path.isdir(i) and i.endswith(".html") and i.lower() != "index.html":
            files.append(i)
        elif os.path.exists(os.path.join(path, i, "index.html")):
            dirs.append(i)
    return files, dirs


def getTitle(path: str) -> str:
    """Returns the title of an html file."""
    with open(path) as fileObj:
        text = fileObj.read()
    parser = MyHTMLParser()
    parser.feed(text)
    return parser.title if hasattr(parser, "title") else "Untitled"


def createMarkup(files: List[Tuple], dirs: List[Tuple]) -> str:
    """Create the markup that represents a list of available files and directories"""
    markup: List[str] = []
    markup.append("<h2>Notes</h2>")
    if not files:
        markup.append("<p>No notes yet.</p>")
    else:
        markup.append("<ol>\n")
        try:
            for file in files:
                markup.append(f'<li><a href="{file[1]}">{file[0]}</a></li>\n')
        except Exception as mess:
            print(f"Error while trying to create markup: {mess}")
        finally:
            markup.append("</ol>")

    markup.append("<h2>Directories</h2>")
    if not dirs:
        markup.append("No directories yet.")
    else:
        markup.append("<ol>")
        try:
            for i in dirs:
                markup.append(f'<li><a href="{i[1]}">{i[0]}</a></li>')
        except Exception as mess:
            print("Exception while trying to list directories: ", mess)
        finally:
            markup.append("</ol>")

    return "\n".join(markup)


def run(path: str):
    """"""
    dirName = os.path.dirname(path)
    _files, _dirs = getFilesAndDirs(dirName)
    files: List[Tuple] = []
    dirs: List[Tuple] = []
    for file in _files:
        filePath = os.path.join(dirName, file)
        files.append((getTitle(filePath), f"./{file}"))

    for i in _dirs:
        dirPath = os.path.join(dirName, i, "index.html")
        dirs.append((getTitle(dirPath), f"./{i}/index.html"))

    markup = createMarkup(files, dirs)
    with open(path, "r") as fileObj:
        content = fileObj.read()
    parser = MyHTMLParser()
    parser.feed(content)
    lines = content.split("\n")
    row, col = parser.endBodyPos
    if col == 0:  # new line
        row -= 1
    lines[row] = f"\n{markup}\n{lines[row]}"
    with open(path, "w") as fileObj:
        fileObj.write("\n".join(lines))


if __name__ == "__main__":
    if not sys.argv[1]:
        print("You must pass path to a index.tex or  index.html file.")
        exit(1)
    path = sys.argv[1]
    if path[:2] != "./":
        path = "./" + path
    if not os.path.exists(path) or os.path.isdir(path):
        print("invalid file.")
        exit(1)
    if os.path.basename(path) != "index.tex":
        print("File must be index.tex.")
        exit(1)

    path = path.rpartition("tex")[0] + "html"
    run(path)
