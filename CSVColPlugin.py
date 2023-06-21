import sys

class CSVColPlugin:
    def input(self, inputfile):
        self.infile = open(inputfile, 'r')

    def run(self):
        pass

    def output(self, outputfile):
        self.outfile = open(outputfile, 'w')


        firstline = self.infile.readline()
        contents = firstline.strip().split(',')

        for element in contents:
           self.outfile.write(element[1:len(element)-1]+"\n")
