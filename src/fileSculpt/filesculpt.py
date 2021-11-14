import re


class Sculptfile:
    def __init__(self, findregex: re, replace: str, inpath: str, outpath: str):
        self.findregex = findregex
        self.replace = replace
        try:
            self.inpath = inpath
            try:
                self.outpath = outpath
            except:
                self.outpath = inpath
        except:
            print("!!!! ------- No input path was specified ------- !!!!")

    def __str__(self):
        return f"{self.findregex} {self.replace} {self.inpath} {self.outpath}"

    def scuttle(self):
        output_set = None

        with open(self.inpath, "r") as file:
            content = file.read()

            regexset = re.compile(self.findregex + r"()")
            output_set = re.findall(regexset, content)

        return output_set

    def sculpt(self):
        scuttled = self.scuttle()
        output_string = ""
        for entry in scuttled:
            for item in self.replace:
                if type(item) is int:
                    output_string += entry[item]
                else:
                    output_string += item

        with open(self.outpath, "w") as file:
            file.write(output_string)
