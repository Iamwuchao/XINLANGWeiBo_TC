from config import *

def user_max_min_forward(train_data):
    user_max_forward = train_data.groupby('uid')['forward_count'].max()
    user_max_forward.to_csv(user_forward_max_path,sep=',')
    user_min_forward = train_data.groupby('uid')['forward_count'].min()
    user_min_forward.to_csv(user_forward_min_path,sep=',')

def user_max_min_comment(train_data):
    user_min_comment = train_data.groupby('uid')['comment_count'].min()
    user_max_comment = train_data.groupby('uid')['comment_count'].max()
    user_min_comment.to_csv(user_comment_min_path,sep=',')
    user_max_comment.to_csv(user_comment_max_path,sep=',')

def user_max_min_like(train_data):
    user_max_like = train_data.groupby('uid')['like_count'].max()
    user_min_like = train_data.groupby('uid')['like_count'].min()
    user_max_like.to_csv(user_like_max_path,sep=',')
    user_min_like.to_csv(user_like_min_path,sep=',')


