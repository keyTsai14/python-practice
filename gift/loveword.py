import imp
from urllib.request import DataHandler
import jieba
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale
from wordcloud import WordCloud
from collections import Counter


def word_cloud(data_path,mask_path):
    with open(data_path,'r') as f:
        data = f.read()

    mask = plt.imread(mask_path)
    cut_data = jieba.cut(data)
    str_cut_data = ' '.join(cut_data)
    list_cut_data = str_cut_data.split(' ')

    my_wordcloud = WordCloud(font_path='./love.jpeg',mask=mask,background_color='pink').generate(str_cut_data)

    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.show()
        