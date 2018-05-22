import pandas as pd
from config import *

'''
计算各个估计值的
'''


def uid_weibo_info(train_data):
    uid_weibo_dict = {}
    uid_set = set()
    for index, row in train_data.iterrows():
        uid = row['uid']
        forward_count = row['forward_count']
        comment_count = row['comment_count']
        like_count = row['like_count']
        uid_weibos_list = uid_weibo_dict.get(uid, [])
        uid_weibos_list.append((forward_count, comment_count, like_count))
        uid_weibo_dict[uid] = uid_weibos_list
        uid_set.add(uid)
    print("看看这字典有多少数据")
    print(len(uid_weibo_dict))
    print("多少UID")
    print(len(uid_set))
    return uid_weibo_dict


def uid_predict_f_c_l(uid_weibo_dict):
    uid_f_max_df = pd.read_csv(user_forward_max_path, header=None, names=['uid', 'f_max'], index_col=0)
    uid_f_min_df = pd.read_csv(user_forward_min_path, header=None, names=['uid', 'f_min'], index_col=0)
    uid_f_max_dict = uid_f_max_df.to_dict(orient='index')
    uid_f_min_dict = uid_f_min_df.to_dict(orient='index')

    uid_c_max_df = pd.read_csv(user_comment_max_path, header=None, names=['uid', 'c_max'], index_col=0)
    uid_c_min_df = pd.read_csv(user_comment_min_path, header=None, names=['uid', 'c_min'], index_col=0)
    uid_c_max_dict = uid_c_max_df.to_dict(orient='index')
    uid_c_min_dict = uid_c_min_df.to_dict(orient='index')

    uid_l_max_df = pd.read_csv(user_like_max_path, header=None, names=['uid', 'l_max'], index_col=0)
    uid_l_min_df = pd.read_csv(user_like_min_path, header=None, names=['uid', 'l_min'], index_col=0)
    uid_l_max_dict = uid_l_max_df.to_dict(orient='index')
    uid_l_min_dict = uid_l_min_df.to_dict(orient='index')

    all_uid_list = uid_weibo_dict.keys()
    user_forward_predict = {}
    user_comment_predict = {}
    user_like_predict = {}
    for uid in all_uid_list:
        f_max = uid_f_max_dict[uid]['f_max']
        f_min = uid_f_min_dict[uid]['f_min']
        best_score_f = 0
        for f_predict in range(f_min, f_max + 1):
            score = compute_score(uid_weibo_dict[uid], forward_label, f_predict, 5, 0.5)
            if (best_score_f < score):
                user_forward_predict[uid] = (f_predict)

        best_score_c = 0
        c_max = uid_c_max_dict[uid]['c_max']
        c_min = uid_c_min_dict[uid]['c_min']
        for c_predict in range(c_min, c_max + 1):
            score = compute_score(uid_weibo_dict[uid], comment_label, c_predict, 3, 0.25)
            if (best_score_c < score):
                user_comment_predict[uid] = c_predict

        best_score_l = 0
        l_max = uid_l_max_dict[uid]['l_max']
        l_min = uid_l_min_dict[uid]['l_min']
        for l_predict in range(c_min, c_max + 1):
            score = compute_score(uid_weibo_dict[uid], like_label, l_predict, 3, 0.25)
            if (best_score_l < score):
                user_like_predict[uid] = l_predict
    return user_forward_predict, user_comment_predict, user_like_predict


def compute_score(weibo_list, label, predict, weight1, weight2):
    '''
    :param weibo_list: 该用户的所有微博
    :param label: 预测的哪一个，转发 0 评论 1 点赞 2
    :param predict: 预测值
    :param weight1: 第一步计算偏差的权值
    :param weight2:第二部计算准确率的权值
    :return: 得分
    '''
    fenzi_sum = 0
    fenmu_sum = 0
    for weibo in weibo_list:
        deviation = abs(weibo[label] - predict) / (weibo[label] + weight1)
        precision = 1 - weight2 * deviation
        count = weibo[0] + weibo[1] + weibo[2] + 1
        if (precision > 0.8):
            fenzi_sum = fenzi_sum + count
        fenmu_sum = fenmu_sum + count
    return fenzi_sum * 1.0 / fenmu_sum
