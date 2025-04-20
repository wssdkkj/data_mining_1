from LoadData import load_data
from EDA import eda
from preprocess import preprocess
from Profile import User_Profile

if __name__ == '__main__':
    data = load_data('./10G_data_new')
    eda(data)
    data_clean = preprocess(data)
    User_Profile(data_clean)