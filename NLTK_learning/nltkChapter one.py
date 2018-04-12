import codecs
import nltk
import matplotlib


def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage_taken_by_a_word_in_text(text, word):
    return (text.count(word)/len(text))*100


from nltk.book import *
if __name__ == '__main__':

    ''' calculating text richness  covering percentage of the words in text3 (que tanto porcentage de uso se hace de las palabras) '''
    rch3=len(text3)/len(set(text3))
    print("**** text richness of text 3 : "+format(rch3)+" %")
    '''how often a word occurs in a text, and compute what percentage of the text is taken up by a specific word'''
    print("*****how often a word occurs in a text  (god in text3) : "+format(text3.count("God")))

    print("*****what percentage of the text is taken up by a specific word  "
          "(god in text3) : "+format(percentage_taken_by_a_word_in_text(text3 , "God")))

    '''Paradigmatic relations '''
    print("*****Paradigmadic related words of \"terrible\" in text2 (used in a similar context (same class))******")
    text2.similar("terrible")

    '''common context  in this case be terrible for , be better for '''
    print("***** Common context where terrible and big appears *****")
    text2.common_contexts(["terrible","better"])

    ''' ^^^^^ Python stuff Slicing  "great" array from element 1 to 3 ^^^^ '''
    print("****Slicing the  \"great\" array from element 1 to 3 (remember first letter stars in 0) : "+"great"[1:3])



    '''******  Frecuency Distribution  it create a Hashmap (dictionary) 
        where the keys are the words in the text and the values its number of apperence in the text ***********'''

    fdist6 = nltk.FreqDist(text6)
    print("****frencuency distribution of  raw text6: "+format(fdist6))
    '''Showing number of apperences of word hello in text 6'''
    print("****Showing number of apperences of word hello in text 6 : "+format(fdist6["hello"]))

    '''Getting words larger than 5 '''
    long_words = [word for word in text6 if len(word) > 5]
    print("****Words larger than 15 ")
    print(long_words)

    ''' talking about frecuency distribution if we input a raw text into nlkt's FreqDist we will obtain a poor quality dictionary of the text
        so, we can make a simple text normalization process eliminating repetition of words which are the same but ntlk things that are different beause of capitalization
        for example Hello and hello are the same word but nltk thinks they are different words because it words whit tokens 
        so, perhaps we made a better text normalization process we can't obtain better precision in our tests '''
    #v = (w.lower() for w in text6)
    ##another way to improve the text is to eliminating puntuaction
    v = (w.lower() for w in text6 if w.isalpha())
    freqDistCorrec = nltk.FreqDist(set(v))
    print("***^^ Improved frecuency distribution without punctuation")
    print(freqDistCorrec.keys())

    '''Now we will get unrelevant words like too large words which aren't enought 
     frequently in the corpus '''

    unrelevant_words = [word for word in freqDistCorrec.keys() if(len(word) > 7) and (freqDistCorrec[word] < 3)]
    print("*****Unrelevant words: ")
    print(unrelevant_words)

    '''Measuring  how many words'''

    '''selecting words which are larger than 7 characters and appers more than 7 times in text 5'''

    freqDist5 = FreqDist(text5)
    print("*****selecting words which are larger than 7 characters and appers more than 7 times in text 5")
    largeAndFrecuent = [word for word in set(freqDist5.keys()) if len(word)>7 and freqDist5[word] > 7]
    print(largeAndFrecuent)

    '''Mining for big rams '''

    ''' Big rams help us to find  pair of words and then searching for the most common pairs in order we can find
        something called  Collocations which basically are  words than occur unsually often  thus red wine and collocations are 
         resistant to substitution with words that have similar meanings for example  marron wine sounds very odd compared whit red wine '''
    sentence_Alice = ["how", "long", "is", "forever", "?"]
    sentence_Hatter = ["sometimes", "it", "is", "just", "a", "second"]


    print("******Big rams in sentence \"How long is forever ?\" ")
    for i in bigrams(sentence_Alice):
        print(i)

    '''Filtering words in text (is digit can also works for filtering numbers '''
    print("Filtering words in text (words which ends whit ableness)")
    print(sorted([w for w in set(text1) if w.endswith("ableness")]))
    print("***finding words wit contains  \"-\" ")
    print(sorted([w for w in set(text7) if '-' in w and 'index' in w]))













