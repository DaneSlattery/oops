class ScoreCalc:
    def __init__(self, slices):
        self.score = 0
        self.slices = slices
        self.calculatescore()

    def calculatescore(self):
        for slice in self.slices:
            r1 = slice[0]
            c1 = slice[1]
            r2 = slice[2]
            c2 = slice[3]
            self.score += abs(r2-r1+1)*abs(c2-c1+1)