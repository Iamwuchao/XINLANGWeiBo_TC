from .data_config import *
import pandas as pd

train_data = pd.read_table(TRAIN_DATA_PATH,header=None,
                     names=['uid','mid','time','forward_count','comment_count','like_count','content'],
                     encoding='utf-8',delim_whitespace=True,index_col=1)
print("shape : "+train_data.shape)