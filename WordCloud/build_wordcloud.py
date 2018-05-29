'''
fun: 生成词云,wordcloud.generate 善于对英文进行分词,对中文分词支持不够好
time: 2018-5-28
author: tang
reference: https://blog.csdn.net/fontthrone/article/details/72775865
'''

from wordcloud import WordCloud

f = open(r"./txtdata/Alice's Adventures in Wonderland.txt",'r').read()
wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(f)

# width,height,margin可以设置图片属性

# generate 可以对全部文本进行“自动分词”并构建词云,但是他对中文支持不好,对中文的分词处理请看我的下一篇文章
#wordcloud = WordCloud(font_path = r'D:\Fonts\simkai.ttf').generate(f)
# 你可以通过font_path参数来设置字体集

#background_color参数为设置背景颜色,默认颜色为黑色

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")    #关闭坐标轴
plt.show()