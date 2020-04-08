# Import packages
import numpy as np
import pandas as pd
from scipy import stats

# Read in housing data
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

# Add calculations below 
brooklyn_mean = np.average(brooklyn_price)
manhattan_mean = np.average(manhattan_price)
queens_mean = np.average(queens_price)

brooklyn_median = np.median(brooklyn_price)
manhattan_median = np.median(manhattan_price)
queens_median = np.median(queens_price)

brooklyn_mode =stats.mode(brooklyn_price)
manhattan_mode = stats.mode(manhattan_price)
queens_mode = stats.mode(queens_price)







