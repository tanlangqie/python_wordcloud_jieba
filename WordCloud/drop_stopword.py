'''
fun: jieba分词中去除“停用词”，例如：是的、了、我们等无实际意义的词;添加自定义的词
time: 2018-5-28
author: tang
reference: https://blog.csdn.net/fontthrone/article/details/72782499
'''
import sys
import jieba
from os import path


d = path.dirname(__file__)        #d为当前工作的工作目录
stopwords_path = r'.\stopword\stopword1893.txt' # 停用词词表

# 添加自定义中文语句的代码在这里
jieba.add_word(r'一夜爆红')        #添加自定义词
jieba.add_word(r'暗香漂浮')


text_path = r'./txtdata/keyword_test.txt' #设置要分析的文本路径
text = open(path.join(d, text_path),encoding='UTF-8').read()

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path,encoding='UTF-8')
    try:
        f_stop_text = f_stop.read( )
        #f_stop_text = unicode(f_stop_text,'utf-8')
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

text1 = jiebaclearText(text)      # 一夜 爆红 娱乐圈 作者 暗香 漂浮 文案 陆溪 娱乐圈 两年 十八 '''
#print (text1)   输出结果为一长串文本
text_result = text1.split(' ')
for word in text_result:
    print (word)


#strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）。