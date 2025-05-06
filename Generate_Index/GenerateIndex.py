import os
from os.path import isdir


def iter(file, dir):
    for i in os.listdir("../docs"):
        if i == "index.html":
            continue
        if os.path.isdir(dir + "/" + i):
            iter(file, dir + "/" + i)
        else:
            line = (
                '<li>            <a href="'
                + dir
                + '"'
                + i
                + '">'
                + i.split(".")[0]
                + "</a> </li>"
            )
            file.write(line)


with open("../docs/index.html", "w") as file:
    with open("indexHead.txt", "r") as head:
        for line in head:
            file.write(line)
    iter(file, "../docs/")
    with open("indextail.txt", "r") as tail:
        for line in tail:
            file.write(line)
