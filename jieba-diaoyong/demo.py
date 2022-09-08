from ast import pattern
import jieba
import re
import collections



def wordcloud(string_data):
    # 1、文本预处理
    pattern = re.compile(u'\t|\n|\.|\\|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
    string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除
    # 2、文本分词
    seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
    object_list = []
    remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                    u'通常',u'如果',u'我们',u'需要',u',',u'the',u'/'] # 自定义去除词库
    # remove_words.append(stopwords.words('english'))
    # 3、去停用词
    for word in seg_list_exact: # 循环读出每个分词
        if word not in remove_words: # 如果不在去除词库中
            object_list.append(word) # 分词追加到列表
    # 4、词频统计
    word_counts = collections.Counter(object_list) # 对分词做词频统计
    word_counts_top = word_counts.most_common(50) # 获取前10最高频的词
    return word_counts_top


print(wordcloud(u'Stream 作为 Java 8 的一大亮点，它与 java.io 包里的 InputStream 和 OutputStream 是完全不同的概念。Java 8 中的 Stream 是对集合（Collection）对象功能的增强，它专注于对集合对象进行各种非常便利、高效的聚合操作（aggregate operation），或者大批量数据操作 (bulk data operation)。尤其是对于数据从业人员来说，对数据做各种操作转换是再正常不过的需求，基本每天都会用到。例如下面这么一个简单的小需求：求一个集合中字符串长度小于5的数量。'))