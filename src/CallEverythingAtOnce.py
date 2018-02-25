from read_data_in import InputData
from generate_output import GenerateOutput
from visualiser import Visualiser
from scorecalculator import ScoreCalc

def main():
    example = InputData('../datasets/small.in')
    totalNumberOfCells = example.R*example.C
# assume the slices piece is valid
    slicedpizza = [7, [[0, 0, 1, 1], [0, 3, 1, 4], [0, 5, 1, 6],
                       [2, 0, 3, 1], [2, 2, 3, 3], [2, 4, 3, 5],
                       [4, 5, 5, 6]]]

    seeme = Visualiser(example, slicedpizza[1])
    seeme.printdata()
    scorecalc = ScoreCalc(slicedpizza[1])
    print('Score: ', scorecalc.score, ". Total Cells:", totalNumberOfCells)
    output = GenerateOutput(slicedpizza, '../output/small.out')

if __name__ == '__main__':
    main()