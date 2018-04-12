from nltk.tokenize import RegexpTokenizer

import re
from collections import defaultdict
from bs4 import BeautifulSoup
from NLPUtils import TextIO_helper

''' this collection works slowly
def searching_for_lemma(doc, collection):
            ##specify that s is a blank chracter and not a return character
    request = re.search(r"(\b\w+\b)(\s+)(\b" + doc+r"\b)\r", collection)
    if request is not None:
        return request.group(1)
    else:
        return doc


def lemmatize(collection, dictionary):
    return re.sub(r"\b(\w+)\b", lambda m: searching_for_lemma(m.group(1), dictionary), collection)


def lemmatize_tokens(collection, dictionary):
    for w in collection:
        str.replace(w, w, searching_for_lemma(w, dictionary))
'''

def create_dic_map(dictionary):
    '''Dictionary is a file/text where we obtain a formatted line in this way "lemma word"  by  line'''
    dictionaryMap = defaultdict(str) #we use this kind of Map to avoid key errors
    for line in dictionary.readlines():
        lemma, word = line.split()
        dictionaryMap[word] = lemma
    return dictionaryMap


def get_lemma(wis, dictionaryMap):
    auxLemma = dictionaryMap[wis]
    if auxLemma is not "":
        #print(wis+"  : "+auxLemma)
        wis = auxLemma
    return wis


def lemmatize(text,dictionaryMap):
    return re.sub(r"\b(\w+)\b", lambda w: get_lemma(w.group(1), dictionaryMap), text)


def lemmatize_and_remove_punctuations(text, dictionaryMap):
    '''returns an array of lemmatized tokens of the text'''
    text = RegexpTokenizer(r'\w+').tokenize(text)
    for w in text:
        w = get_lemma(w, dictionaryMap)
    return text


def lemmatize_and_remove_stopwords_punctuations(text, dictionaryMap,stopwords):
    '''
        dictionaryMap should be a dictionary
        stopwords should be an array
        returns an array of lemmatized tokens '''
    text = RegexpTokenizer(r'\w+').tokenize(text) #removing punctuation
    text_aux = []
    for w in text:
        if w not in stopwords: #removing stopwords
            text_aux.append(get_lemma(w, dictionaryMap))
    return text_aux



def parse_html(text):
    return BeautifulSoup(text, 'html.parser').get_text()


if __name__ == '__main__':
    package = input()
    name =input()
    doc = str.lower(TextIO_helper.read_plain_text(package,name))
    dic = TextIO_helper.read_raw_text("Resources_assets","lemmatization-es.txt")
    dictionaryMap = create_dic_map(dic)
    #doc = re.sub(r"\b(\w+)\b", lambda w: get_lemma(w.group(1), dictionaryMap), doc)
    f = TextIO_helper.create_raw_text("Resources_assets","test_"+name)
    f.writelines(lemmatize_and_remove_punctuations(doc, dictionaryMap))
    print("finished")
    f.close()
