from preprocessing import Preprocessing
from models import Models
from preprocessing_two import PreprocessingTwo
from preprocessing_three import PreprocessingThree

if __name__ == '__main__':
    pre = Preprocessing()
    # pre = PreprocessingTwo()
    # pre_three = PreprocessingThree()
    models = Models(pre.final_dataframe)
