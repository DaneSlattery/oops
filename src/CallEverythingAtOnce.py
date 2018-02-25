from read_data_in import InputData
from generate_output import GenerateOutput
from visualiser import Visualiser

def main():
    example = InputData('../datasets/example.in')
    slicedpizza = [3, [[0, 0, 2, 1], [0, 2, 2, 2], [0, 3, 2, 4]]]
    seeme = Visualiser(example, slicedpizza[1])
    seeme.printdata()
    output = GenerateOutput(slicedpizza, '../output/test.out')

if __name__ == '__main__':
    main()