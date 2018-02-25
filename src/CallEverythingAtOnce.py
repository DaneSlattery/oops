from read_data_in import InputData
from generate_output import GenerateOutput
from visualiser import Visualiser
from scorecalculator import ScoreCalc
from pizza import PizzaGrid, NaivePizzaSlicer

def main():
# input data
    inputDataFileName = '/home/dane/repos/oops/datasets/small.in'
    print("Input Dataset: ", inputDataFileName)
    smallData = InputData(inputDataFileName)

# assume the slices piece is valid
# magic code goes here
    smallPizzaGrid = PizzaGrid(smallData.R, smallData.C, smallData.Toppings)
    Slicer = NaivePizzaSlicer(smallPizzaGrid, smallData.L, smallData.H)
    slicedSmallPizza = Slicer.process()
    slicedSmallPizza = [len(slicedSmallPizza), slicedSmallPizza]

    print(slicedSmallPizza)

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