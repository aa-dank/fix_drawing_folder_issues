import os, datetime, re, shutil
import pandas as pd

csvFile = "Drawing_Dir_No_F5.csv"
csvPath = os.path.join(os.getcwd(), csvFile)

DF = pd.read_csv(csvPath, sep='delimiter')


import pdb; pdb.set_trace()