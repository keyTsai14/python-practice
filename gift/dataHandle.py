from ast import pattern
import jieba
import re

pattern = re.compile(u"\u4e00-\u9fa5+")

with open('./data.txt','r',encoding='utf-8') as f:
    data = re.findall(pattern,f.read())
    data = ''.join(data)
print(data)


with open('./clear_data.txt','w') as w: 
    f.write(data)  