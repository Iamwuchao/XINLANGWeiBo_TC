from data_process.data_process import *

#train_data = read_train_data()

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

#用户数据分析
predict_data = read_predict_data()
print(predict_data.shape)

#train_user_data = train_data['uid']

predict_user_data = predict_data['uid']
print("预测用户")
print(predict_user_data.drop_duplicates().count())

#train_user_data.d





