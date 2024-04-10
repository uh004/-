# 데이터를 불러오기

import pandas as pd

def load_data():
  data = pd.read_csv('seoul3_real_estate_1000.csv')
  return data