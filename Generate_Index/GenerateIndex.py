import os
from os.path import isdir


def iter(file, dir):
    for i in os.listdir(dir):
        if i == "index.html":
            continue
        if os.path.isdir(dir + "/" + i):
            iter(file, dir + "/" + i)
        else:
            line = (
                '\n<li><a href="'
                + dir.split("docs//")[-1]
                + "/"
                + i
                + '">'
                + dir.split("docs//")[-1]
                + "/"
                + i.split(".")[0]
                + "</a> </li>\n"
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
