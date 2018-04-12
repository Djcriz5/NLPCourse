import codecs

import math
import nltk
import re
from collections import defaultdict
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
import nltk.data

def read_raw_text(where):
    return codecs.open(where, "r",encoding='utf-8', errors='ignore')


def read_plain_text(where):
    return BeautifulSoup(read_raw_text(where), 'html.parser').get_text()


def number_of_segments(doc,collection):
    """ returns the number of segments that contain the word (doc) in a given collection (list of senteces) """
    count=0 #number of segments counter
    for sentence in collection:
        if doc in sentence:
            count += 1
    return count


def number_of_segments_of_two_words(doc1, doc2, collection):
    """ returns the number of segments that contain the word (doc) in a given collection (list of senteces) """
    count=0 #number of segments counter
    for sentence in collection:
        if doc1 in sentence and doc2 in sentence:
            count += 1
    return count


def word_probability_smoothing(word, collection):
    return (number_of_segments(word, collection)+0.5)/(len(collection)+1)


def word_absence_probability_smoothing(word, collection):
    return 1 - word_probability_smoothing(word, collection)


def words_conditional_probability_smoothing_both(word1, word2, collection):
    return (number_of_segments_of_two_words(word1, word2, collection)+0.25)/(len(collection)+1)


def words_absence_conditional_probability_smoothing_both(word1,word2, collection):
    return  word_absence_probability_smoothing(word2,collection)-words_absence_conditional_probability_smoothing_oneWord(word1,word2,collection)


def words_absence_conditional_probability_smoothing_oneWord(word, absented_word, collection):
    return word_probability_smoothing(word,collection)-words_conditional_probability_smoothing_both(word, absented_word, collection)


def word_raw_probability(word, collection):
    return number_of_segments(word, collection)/(len(collection))

def calculate_stand_alone_entropy(words_conditional_probability,word1_probability,word2_probability):
    return words_conditional_probability*math.log2(words_conditional_probability/(word1_probability*word2_probability))

def calculate_mutual_information(word1,word2,collection):
    mi = 0
    #when p(w1=1)
    probability_of_w1 = word_probability_smoothing(word1, collection)
    # when p(w2=1)
    probability_of_w2 = word_probability_smoothing(word2, collection)
    # when p(w1=0)
    probability_of_absence_w1 = 1-probability_of_w1
    # when p(w2=0)
    probability_of_absence_w2 = 1-probability_of_w2
    # when p(w1=1,w2=1)
    conditional_probability_of_w1_and_w2 = words_conditional_probability_smoothing_both(word1, word2, collection)
    # when p(w1=1,w2=0)
    conditional_probability_of_w1_and_w2absented = probability_of_w1 - conditional_probability_of_w1_and_w2
    #when  p(w1=0,w2=1)
    conditional_probability_of_w1absented_and_w2 = probability_of_w2 - conditional_probability_of_w1_and_w2
    # when p(w1=0,w2=0)
    conditional_probability_of_w1_and_w2_absented_both = probability_of_absence_w2 - conditional_probability_of_w1_and_w2absented

    '''
        00
        01
        10
        11
    '''
    ##I(0,0)
    mi += calculate_stand_alone_entropy(conditional_probability_of_w1_and_w2_absented_both, probability_of_absence_w1, probability_of_absence_w2)
    #print(mi)
    ##I(0,1)
    mi += calculate_stand_alone_entropy(conditional_probability_of_w1absented_and_w2, probability_of_absence_w1,
                                        probability_of_w2)
    #print(mi)
    ##I(1,0)
    mi += calculate_stand_alone_entropy(conditional_probability_of_w1_and_w2absented, probability_of_w1,
                                        probability_of_absence_w2)
    print(format(conditional_probability_of_w1_and_w2absented)+"  " + format(probability_of_absence_w1)+"   "+ format( probability_of_absence_w2))
    print("cond "+ format( conditional_probability_of_w1_and_w2absented))
    print("div "+ format(probability_of_absence_w1*probability_of_absence_w2))
    print("log arg: "+format(conditional_probability_of_w1_and_w2absented/(probability_of_absence_w1*probability_of_absence_w2)))
    print("log op :"+format(-math.log2((conditional_probability_of_w1_and_w2absented/(probability_of_absence_w1*probability_of_absence_w2)))))
    print(mi)
    ##I(1,1)
    mi += calculate_stand_alone_entropy(conditional_probability_of_w1_and_w2, probability_of_w1,
                                        probability_of_w2)
    return mi














if __name__ == '__main__':
    ##name = input()
    doc = read_raw_text("normalized_e960404.htm").read()
    spanish_tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
    sent_tokenize_list = spanish_tokenizer.tokenize(doc)
    ##print(number_of_segments("gobierno", sent_tokenize_list))
    ##print(word_probability_smoothing("gobierno", sent_tokenize_list))
    #checar si conviene lemmatizar las paalbras que ingresemos alegriamos -> alegar
    ##print(number_of_segments_of_two_words("alegar", "gobierno",sent_tokenize_list))

    mi=calculate_mutual_information("cristo","gobierno",sent_tokenize_list)
    print(mi)

