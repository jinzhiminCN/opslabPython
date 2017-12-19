# coding:utf-8
import sys
from gensim.models import Word2Vec
import logging
import gensim
import os

# 模型的加载
model = Word2Vec.load('word2vector.model')
# 比较两个词语的相似度,越高越好
print('"唐山" 和 "中国" 的相似度:' + str(model.similarity('唐山', '中国')))
print('"中国" 和 "祖国" 的相似度:' + str(model.similarity('祖国', '中国')))
print('"中国" 和 "中国" 的相似度:' + str(model.similarity('中国', '中国')))
# 使用一些词语来限定,分为正向和负向的
result = model.most_similar(positive=['中国', '城市'], negative=['学生'])
print('同"中国"与"城市"二词接近,但是与"学生"不接近的词有:')
for item in result:
    print('   "' + item[0] + '"  相似度:' + str(item[1]))

result = model.most_similar(positive=['男人', '权利'], negative=['女人'])
print('同"男人"和"权利"接近,但是与"女人"不接近的词有:')
for item in result:
    print('   "' + item[0] + '"  相似度:' + str(item[1]))

result = model.most_similar(positive=['女人', '法律'], negative=['男人'])
print('同"女人"和"法律"接近,但是与"男人"不接近的词有:')
for item in result:
    print('   "' + item[0] + '"  相似度:' + str(item[1]))
# 从一堆词里面找到不匹配的
print("老师 学生 上课 校长 , 有哪个是不匹配的? word2vec结果说是:" +
      model.doesnt_match("老师 学生 上课 校长".split()))
print("汽车 火车 单车 相机 , 有哪个是不匹配的? word2vec结果说是:" +
      model.doesnt_match("汽车 火车 单车 相机".split()))
print("大米 白色 蓝色 绿色 红色 , 有哪个是不匹配的? word2vec结果说是:" +
      model.doesnt_match("大米 白色 蓝色 绿色 红色 ".split()))
# 直接查看某个词的向量
print('中国的特征向量是:')
print(model['中国'])
