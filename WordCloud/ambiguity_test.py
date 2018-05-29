'''
fun: jieba分词中解决中文歧义问题
time: 2018-5-28
author:tang
reference:https://blog.csdn.net/fontthrone/article/details/72782499
'''
import jieba
TestStr = "2010年底部队友谊篮球赛结束"
# 因为在汉语中没有空格进行词语的分隔，所以经常会出现中文歧义，比如年底-底部-部队-队友
# jieba 默认启用了HMM（隐马尔科夫模型）进行中文分词，实际效果不错

seg_list = jieba.cut(TestStr, cut_all=True)
print ("Full Mode:", "/ ".join(seg_list))           # 全模式

seg_list = jieba.cut(TestStr, cut_all=False)
print ("Default Mode:", "/ ".join(seg_list))      # 默认模式
# 在默认模式下有对中文歧义有较好的分类方式

seg_list = jieba.cut_for_search(TestStr)             # 搜索引擎模式
print ("cut for Search","/".join(seg_list))