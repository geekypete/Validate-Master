"""
Class for whitespace, comma, and tab delimited data 
"""


class Data:
    def __init__(self, filelocation, seper, skiprow=False):
        self.filelocation = filelocation
        self.seper = seper
        if skiprow is False:
            if self.seper == "whitespace":
                self.data, self.n = self.whitespace()
                self.header = self.data[0]
                self.data = {thisKey: self.data[thisKey] for thisKey in range(1, self.n)}
            elif self.seper == "comma":
                self.data, self.n = self.comma()
                self.header = self.data[0]
                self.data = {thisKey: self.data[thisKey] for thisKey in range(1, self.n)}
            elif self.seper == "tab":
                self.data, self.n = self.tab()
                self.header = self.data[0]
                self.data = {thisKey: self.data[thisKey] for thisKey in range(1, self.n)}
        else:
            if self.seper == "whitespace":
                self.data, self.n = self.whitespace()
            elif self.seper == "comma":
                self.data, self.n = self.comma()
            elif self.seper == "tab":
                self.data, self.n = self.tab()
''' <REVIEW PLAWSON>

It's probably not necessary to break the parser into three separate functions, rather it would be trivial to pass the appropriate delimiter to the string
split inside a single function. This isn't necessary, just a means to shorten up the code a bit. 

<END REVIEW>'''

    # The following two functions establish the possible options for delimiters: whitespace, comma, or tab
    def whitespace(self):
        """
        Produces a dictionary with data that used whitespace as a delimiter

        :return: a dictionary with the parsed data and the amount of data
        """
        f = open(self.filelocation, "rb")
        temp = list()
        for line in f.readlines():
            temp.append(line.replace("\n", "").split(" "))
        f.close()
        data = dict()
        count = 0
        for row in temp:
            data[count] = list()
            for each in row:
                if each is not "":
                    data[count].append(each)
            count += 1
        return data, count

    def comma(self):
        """
        Produces a dictionary with data that used a comma as a delimiter

        :return: a dictionary with the parsed data and the amount of data
        """
        f = open(self.filelocation, "rb")
        temp = list()
        for line in f.readlines():
            temp.append(line.replace("\n", "").split(","))
        f.close()
        data = dict()
        count = 0
        for row in temp:
            data[count] = list()
            for each in row:
                if each is not "":
                    data[count].append(each)
            count += 1
        return data, count

    def tab(self):
        """
        Produces a dictionary with data that used a tab as a delimiter

        :return: a dictionary with the parsed data and the amount of data
        """
        f = open(self.filelocation, "rb")
        temp = list()
        for line in f.readlines():
            temp.append(line.replace("\n", "").split("\t"))
        f.close()
        data = dict()
        count = 0
        for row in temp:
            data[count] = list()
            for each in row:
                if each is not "":
                    data[count].append(each)
            count += 1
        return data, count
