from read_data_in import InputData
from generate_output import GenerateOutput
from visualiser import Visualiser
from scorecalculator import ScoreCalc


def main():
# input data
    inputDataFileName = '/home/dane/repos/oops/datasets/small.in'
    print("Input Dataset: ", inputDataFileName)
    smallData = InputData(inputDataFileName)

# assume the slices piece is valid
# magic code goes here
    slicedSmallPizza = [7, [[0, 0, 1, 1], [0, 3, 1, 4], [0, 5, 1, 6],
                            [2, 0, 3, 1], [2, 2, 3, 3], [2, 4, 3, 5],
                            [4, 5, 5, 6]]]
# visualise slices
    Visualiser(smallData, slicedSmallPizza[1])

# calculate the score
    print('Score: ', ScoreCalc(slicedSmallPizza[1]).score)

# output the the file
    outputDataFileName = '/home/dane/repos/oops/output/small.out'
    print("Output file: ", outputDataFileName)
    GenerateOutput(slicedSmallPizza, outputDataFileName)


if __name__ == '__main__':
    main()