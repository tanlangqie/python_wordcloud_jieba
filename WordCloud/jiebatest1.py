'''
fun: 第一次接触到jieba分词，这个用于测试jieba
time： 2018-5-28
author: tang
reference: https://blog.csdn.net/fontthrone/article/details/72782499
'''
import  jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True, HMM=False)
print('Full Model: ' + "/".join(seg_list))      #全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False, HMM=False)
print("Default Mode: " + "/".join(seg_list))    #默认模式

seg_list = jieba.cut("他来到了网易杭研大厦",HMM=False)
print(",".join(seg_list))

# 搜索引擎模式
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", HMM=False)
a =",".join(seg_list)
print(a)

#jieba.cut的默认参数只有三个,jieba源码如下
# cut(self, sentence, cut_all=False, HMM=True)
# 分别为:输入文本 是否为全模式分词 与是否开启HMM进行中文分词