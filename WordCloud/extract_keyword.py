'''
fun: 利用jieba提取关键词
time: 2018-5-28
authoe: tang
reference: https://blog.csdn.net/fontthrone/article/details/72782499
'''
from os import path
import jieba.analyse as analyse

d = path.dirname(__file__)

text_path = r'./txtdata/keyword_test.txt' #设置要分析的文本路径
text = open(path.join(d, text_path),encoding='UTF-8').read()          #读取txt文件

for key in analyse.extract_tags(text,50, withWeight=False):
# 使用jieba.analyse.extract_tags()参数提取关键字,默认参数为50
    print (key)
    # 设置输出编码为utf-8不然在因为win下控制台默认中文字符集为gbk,所以会出现乱码
    # 当withWeight=True时,将会返回number类型的一个权重值(TF-IDF)