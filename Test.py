from data_process.data_process import *
from user_feature import *
from evaluate import *

# train_data = read_train_data()

# print(train_data.shape)
# print(train_data.columns)
# print(train_data['uid'].drop_duplicates().count())
#
# print("forward_count")#转发
# print(train_data['forward_count'].max()) #最大值
# print(train_data['forward_count'].mean()) #均值
# print(train_data['forward_count'].median()) #中位数
# print(train_data['forward_count'].mode()) #众数
#
# print("comment_count")#评论
# print(train_data['comment_count'].max())
# print(train_data['comment_count'].mean())
# print(train_data['comment_count'].median())
# print(train_data['comment_count'].mode())
#
#
# print("like_count")#点赞数
# print(train_data['like_count'].max())
# print(train_data['like_count'].mean())
# print(train_data['like_count'].median())
# print(train_data['like_count'].mode())

# 用户数据分析
# predict_data = read_predict_data()
# print(predict_data.shape)

# train_user_data = train_data['uid']

# predict_user_data = predict_data['uid']
# print("预测用户")
# print(predict_user_data.drop_duplicates().count())

# train_user_data.d

train_data = read_train_data()
user_max_min_forward(train_data)
user_max_min_comment(train_data)
user_max_min_like(train_data)

print("开始")
uid_weibo_dict = uid_weibo_info(train_data)
user_forward_predict,user_comment_predict,user_like_predict = uid_predict_f_c_l(uid_weibo_dict)

print("获取预测数据")
predict_data = read_predict_data()
predict_result_list = []
for index,row in predict_data.iterrows():
    uid = row['uid']
    mid = row['mid']
    forward = user_forward_predict.get(uid,0)
    like = user_like_predict.get(uid,0)
    comment = user_comment_predict.get(uid,0)
    predict_result_list.append(str(uid)+'   '+str(mid)+'    '+str(forward)
                               +','+str(comment)+','+str(like)+'\n')
f = open(predict_result_path,'w')
f.writelines(predict_result_list)
print("完成")
