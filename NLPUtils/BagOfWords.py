import codecs
import nltk
import re

from bs4 import BeautifulSoup


def clean_text(text):
    return nltk.FreqDist(text.lower())

'''
def get_context_dict(keyword, text, size_of_window):
    keyword = keyword.lower()
    dict = {}
    tokens = nltk.word_tokenize(text.lower())
    total_words = len(tokens)
    for index in range(total_words):
        if tokens[index] == keyword:
            for word in tokens[index+1-(size_of_window+1):index+(size_of_window+1)]:
                if word != keyword:
                    if word in dict:
                        dict[word] += 1/total_words
                    else:
                        dict[word] = 1/total_words
    return dict

'''

def get_context_dict(keyword, tokens, size_of_window):
    keyword = keyword.lower()
    dic = {}
    total_words = len(tokens)
    context_size = 0
    for index in range(total_words):
        if tokens[index] == keyword:
            for word in tokens[index+1-(size_of_window+1):index+(size_of_window+1)]:
                if word != keyword:
                    context_size += 1.00
                    if word in dic:
                        dic[word] += 1.00
                    else:
                        dic[word] = 1.00
    dic = {k: v / total for total in (context_size,) for k, v in dic.items()}
    return dic



def similarity_percentage(word1, word2, doc, window_size):
    """this one works better using plain_text input instead of raw_text input use read_plain_text() function
    in order to obtain  a better performance """
    word1_v = get_context_dict(word1, doc, window_size)
    word2_v = get_context_dict(word2, doc, window_size)
    similarity = 0
    for word in word1_v.keys():
        if word in word2_v:
            similarity += (word1_v[word]*word2_v[word])
    return similarity


def aux_similarity_percentage(word1_context_v, word2, tokens, window_size):
        '''this one  obtain the similarity percentage between two words using the  normalized context vector
            of one word and compute the context vector of the second '''
        similarity = 0
        word2_v=get_context_dict(word2, tokens, window_size)
        for word in word1_context_v.keys():
            if word in word2_v:
                similarity += (word1_context_v[word]*word2_v[word])
        return similarity


def got_words_which_ends_whit(where, search):
    text = codecs.open(where, encoding='utf-8')
    for line in text:
        for word in line.split():
            if word.endswith(search):
                print(word)


def read_raw_text(where):
    return codecs.open(where, "r",encoding='utf-8', errors='ignore')


def read_plain_text(where):
    return BeautifulSoup(read_raw_text(where), 'html.parser').get_text()


def searching_for_lemma(doc, collection):
            ##specify that s is a blank chracter and not a return character
    request = re.search(r"(\b\w+\b)(\s+)(\b" + doc+r"\b)\r", collection)
    if request is not None:
        return request.group(1)
    else:
        return doc


def lemmatize(collection, dictionary):
    '''This one works whit a whole document '''
    return re.sub(r"\b(\w+)\b", lambda m: searching_for_lemma(m.group(1), dictionary), collection)


def lemmatize_tokens(collection, dictionary):
    '''This one works whit an array of tokens '''
    for w in collection:
        print(w +" : "+format(searching_for_lemma(w, dictionary)))
    ##return [str.replace(w, w, searching_for_lemma(w, dictionary)) for w in collection]

if __name__ == '__main__':
    """in this experiment we are  searching  for  paradigmatic relations among the word 
    "gobierno " and the other words in the text """
    doc = read_plain_text("e960401.htm")
    doc = nltk.word_tokenize(doc)
    doc = [w.lower() for w in doc if w.isalpha()]
    dic = read_raw_text("lemmatization-es.txt").read()
    lemmatize_tokens(doc,dic)
   ## doc_vocabulary = sorted(list(set(doc)))
   ## print("in this experiment we are  searching  for  paradigmatic relations among the word  \" gobierno \" and the other words in the text ")
    ##context_v_searched_word = get_context_dict("gobierno", doc, 8)
   ## for word in doc_vocabulary:
     ##   print(word +" : "+ format(aux_similarity_percentage(context_v_searched_word, word, doc, 8)))