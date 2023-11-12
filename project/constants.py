import numpy as np
import pandas as pd

TEST_FILE = 'test.txt'
IMAGE_FILE = 'plot.png'

PROGRAM_DESCRIPTION = "The program takes as input a text file, via a mandatory command line argument and outputs a bar plot of the 'RANGE' most common words."
RANGE = 50
COMMENT_SYMBOL = '%'

TEST_DICT = {'I':1 , "am":2, "Tom":3, "Marvolo":5, "Riddle":10}

PUNCTUATION = ('\n','\t',"...",';',':'," ",",", ".","?","!")

