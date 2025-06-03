import os
from os.path import isdir


def iter(file, dir):
    for i in os.listdir(dir):
        counter = 1
        if i == "index.html":
            continue
        if os.path.isdir(dir + "/" + i):
            line = (
                "<ul>" * counter + i +"</ul> "* counter
            )
            print(line + " Counter=" + str(counter))
            file.write(line)
            iter(file, dir + "/" + i)
            counter += 1
        else:
            line = (
                '\n'
                + '<ul>' * (counter + 1 )
                + '<li><a href="'
                + dir.split("docs//")[-1]
                + "/"
                + i
                + '">'
                + dir.split("docs//")[-1]
                + "/"
                + i.split(".")[0]
                + "</a> </li>\n"
                + '</ul>' * (counter + 1)
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
