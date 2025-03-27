from cambridge import CDictionary
'''
英文语料库介绍
https://zhuanlan.zhihu.com/p/55468476
GBC: Google Book's Corpus， 官网：https://googlebooks.byu.edu/，拥有 1550 亿美国英语词汇
BNC: British National Corpus，是有同等影响力的权威语料库，只不过它的选词是来自于英国英语，主要取自 1980 年的各类英文材料
COHA: Corpus of Historical American English
COCA: Corpus os Contenporary American English
COHA/COCA 作为美国当代英语语料库，于 2008年 2月 20日推出，起初包含的词汇量在 3.2 亿左右，并且每年以 2000 万的速度增加，2017 年已达到 4.5 亿甚至更多
语料库列表
https://www.corpusdata.org/formats.asp
免费词频数据 5000个免费，完整要付费
https://www.wordfrequency.info/samples.asp
'''
domain = 'https://dictionary.cambridge.org'
w = CDictionary(domain)

words = ['sunny','word','funny']
w.Serach(words)
w.Save()