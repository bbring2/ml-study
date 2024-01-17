import pandas as pd
import warnings
warnings.filterwarnings("ignore")


card_data_set = pd.read_csv('./creditcard.csv')
card_data_set.head(3)

print(card_data_set)