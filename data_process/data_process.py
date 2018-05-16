from data_process.data_config import *
import pandas as pd

def read_train_data():
    train_data = pd.read_table(TRAIN_DATA_PATH,header=None,
                     names=['uid','mid','time','forward_count','comment_count','like_count','content'],
                     encoding='utf-8',delim_whitespace=True,index_col=1)
    return train_data

def read_predict_data():
    predict_data = pd.read_table(PREDICT_DATA_PATH,header=None,
                                 names=['uid','mid','time','content'],
                                 encoding='utf-8',delim_whitespace=True)
    return predict_data
