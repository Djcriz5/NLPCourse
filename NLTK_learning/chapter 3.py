import codecs
import nltk
import matplotlib
from bs4 import BeautifulSoup

def read_raw_text(where):
    return codecs.open(where, "r",encoding='utf-8', errors='ignore')


def read_plain_text(where):
    return BeautifulSoup(read_raw_text(where), 'html.parser').get_text()

if __name__ == '__main__':
    """in this experiment we are  searching  for  paradigmatic relations among the word 
    "gobierno " and the other words in the text """
    doc = read_plain_text("e960404.htm")
    doc = nltk.word_tokenize(doc)
    doc = [w.lower() for w in doc if w.isalpha()]
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = nltk.BigramCollocationFinder.from_words(doc, 5)
    finder.apply_freq_filter(5)

    print ("Printing Top 1000 Collocations")
    print (finder.nbest(bigram_measures.likelihood_ratio, 1000))