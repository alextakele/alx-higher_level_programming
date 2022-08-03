
def append_after(filename="", search_string="", new_string=""):
    text = ""
    with open(filename) as r:
        line: str
        for line in r:
            text += line
            if search_string in line:
                text += new_string
                with open(filename, "w") as w:
                    w.write(text)
