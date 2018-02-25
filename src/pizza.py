class PizzaGrid:

    def __init__(self, rows, cols, toppings):
        n = len(toppings)
        assert(rows * cols == n)

        self._num_mushrooms = toppings.count('M')
        self._num_tomatoes = toppings.count('T')

        self._rows = rows
        self._cols = cols
        self._rowcols = []
        k = 0
        for i in range(rows):
            self._rowcols.append([])
            for j in range(cols):
                self._rowcols[i].append(toppings[k])
                k += 1

    def get_cell(self, row, col):
        return self._rowcols[row, col]

    def get_slice(self, r0, c0, r1, c1):
        chunk = [row[c0:c1+1] for row in self._rowcols[r0:r1+1]]
        flat = [x for sublist in chunk for x in sublist]
        as_string = ''.join(flat)
        return (as_string, as_string.count('M'), as_string.count('T'), r0, c0, r1, c1)

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._cols

    @property
    def total_mushrooms(self):
        return self._num_mushrooms

    @property
    def total_tomatoes(self):
        return self._num_tomatoes

class PizzaBase:

    def __init__(self, pizza_grid, minc, maxc):
        self._grid = pizza_grid
        self._minc = minc
        self._maxc = maxc

    def process(self, new_grid=None):
        raise NotImplementedError()

    def get_result(self):
        raise NotImplementedError()

    def _validate_slice(self, slice_):
        if slice_[1] >= self._minc and slice_[2] >= self._minc:
            return True
        else:
            return False

# Partitions pizza into uniform slices, and picks the best distribution in spec.
class NaivePizzaSlicer(PizzaBase):

    def __init__(self, pizza_grid, minc, maxc):
        super().__init__(pizza_grid, minc, maxc)
        self._set = None

    def process(self, new_grid=None):
        if new_grid:
            self._grid = new_grid

        subsets = [[[] for x in range(self._maxc)] for y in range(self._maxc)]
        for k in range(1, self._maxc + 1):
            for i in range(0, self._grid.rows - k + 1, k):
                for j in range(1, self._maxc // k + 1):
                    for m in range(0, self._grid.columns - j + 1, j):
                        #print(k, ' ', j)
                        subsets[k-1][j-1].append(self._grid.get_slice(i, m, i + k - 1, m + j - 1))

        max_ = 0
        for i, row in enumerate(subsets):
            for j, col in enumerate(row):
                sum_ = 0
                set_ = []
                for k, block in enumerate(col):
                    if self._validate_slice(block):
                        sum_ += block[1] + block[2]
                        set_.append(block)
                if sum_ > max_:
                    max_ = sum_
                    self._set = set_
        return self.get_result()

    def get_result(self):
        result = []
        for block in self._set:
            result.append((block[3], block[4], block[5], block[6]))
        return result

#pizza_grid = PizzaGrid(6, 7, 'TMMMTTTMMMMTMMTTMTTMTTMMTMMMTTTTTTMTTTTTTM')
#slicer = NaivePizzaSlicer(pizza_grid, 1, 5)
#print(slicer.process())

#class MagicPizzaSlicer(PizzaBase):
#
#    def __init__(self, pizza_grid):
#        pass
