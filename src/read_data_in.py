class InputData:
    def __init__(self, inputfile):
        self.R = 0
        self.C = 0
        self.L = 0
        self.H = 0
        self.Toppings = 'TMT'
        self.inputfile = inputfile
        self.inputlist = ['']
        self.read_in()
        self.extract_initial_data()
        self.extract_toppings()

    def read_in(self):
        f = open(self.inputfile, 'r')
        try:
            self.inputlist = f.readlines()
        finally:
            print('Data read succesfully: ')
            f.close()

    def extract_initial_data(self):
        self.inputlist[0] = self.inputlist[0].strip('\n')
        firstline = self.inputlist[0].split()
        self.R = int(firstline[0])
        print(self.R, 'rows')
        self.C = int(firstline[1])
        print(self.C, 'columns')
        self.L = int(firstline[2])
        print(self.L, 'min ingredient cells in a slice')
        self.H = int(firstline[3])
        print(self.H, 'max total cells in a slice')
        del self.inputlist[0]

    def extract_toppings(self):
        self.Toppings = ''
        for x in self.inputlist:
            self.Toppings += x.strip('\n')

        print('Pizza Data: ' + self.Toppings)

