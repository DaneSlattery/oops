class GenerateOutput:

    def __init__(self, sliced_pizza, outputfilename):
        self.S = sliced_pizza[0]
        self.slices = sliced_pizza[1]
        self.outputfile = open(outputfilename, 'w')
        self.outputstring = ''
        self.formatoutput()
        self.writeoutput()

    def formatoutput(self):
        self.outputstring = str(self.S) + '\n'
        for x in range(0,self.S):
            self.outputstring += ' '.join(str(e) for e in self.slices[x]) + '\n'

    def writeoutput(self):
#       print(self.outputstring)
        self.outputfile.write(self.outputstring)
        self.outputfile.close()
