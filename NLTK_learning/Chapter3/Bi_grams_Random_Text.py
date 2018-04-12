import nltk

import NLPUtils
from NLPUtils import TextIO_helper
import re
from NLPUtils import NormalizeText


from NLPUtils import ArticleSeparator

debug = False

def printDebug(something):
    if(debug):
        print(something)

def generate_model(conditional_freqDist,word,num=15):
    for i in range(num):
        print(word)
        word=conditional_freqDist[word].max()

if __name__ == '__main__':
    '''Generate Random Text using bigrams and cond freq dist'''
    doc = TextIO_helper.read_raw_text("Resources_assets", "e960404.htm").read()
    rex = re.compile(r'<title.*?>(.*?)<hr>(?P<Article>.*?)<hr>', re.S | re.M)
    articles = NLPUtils.ArticleSeparator.get_raw_articles_list(doc, rex)
    articleTen = NormalizeText.parse_html(articles.__getitem__(1).group("Article"))
    articleTen = nltk.word_tokenize(articleTen)
    bigrams=nltk.bigrams(articleTen)
    condFreqDist=nltk.ConditionalFreqDist(bigrams)
    printDebug(condFreqDist['Jueves'].items())
    generate_model(condFreqDist, "Jueves")


