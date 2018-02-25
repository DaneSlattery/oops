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
        return (as_string, as_string.count('M'), as_string.count('T'))

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

class MagicPizzaSlicer:

    def __init__(self, pizza_grid):
        self._grid = pizza_grid
