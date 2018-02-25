class Visualiser:
    def __init__(self, data, blocks):
        self.data = data
        self.blocks = blocks
        self.printlist = []
        self.formatdata()
        self.drawblocks()

    def appendZero(self):
        rowlist = []
        for x in range(0, self.data.C * 2 + 1):
            rowlist.append(" ")
        self.printlist.append(rowlist)

    def formatdata(self):
        print('\nVisualise data:')
        self.appendZero()

        for row in range(0, self.data.R):
            rowlist = []
            for col in range(0, self.data.C):
                rowlist.append(" ")
                rowlist.append(self.data.Toppings[row*self.data.C + col])


            rowlist.append(" ")
            self.printlist.append(rowlist)
            self.appendZero()

    def printdata(self):
        for row in range(len(self.printlist)):
            for col in range(len(self.printlist[0])):
                print(self.printlist[row][col], end='')
            print()

    def drawblocks(self):
        for block in self.blocks:
            r1 = block[0]
            c1 = block[1]
            r2 = block[2]
            c2 = block[3]
            for row in range(r1*2, r2*2 + 2 + 1):
                for col in range(c1*2, c2*2 + 2 + 1):
                    if row in [r1*2, r2*2 + 2]:
                        self.printlist[row][col] = '-'
                    if col in [c1*c2, c2*2+2]:
                        self.printlist[row][col] = '|'


