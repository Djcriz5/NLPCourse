import codecs
import nltk
import matplotlib

def searching_for_lemma(doc,collection):
    request = re.search("(\w+)(\s+)"+doc, collection)
    if request is not None:
        return request.group(1)
    else:
        return doc

def lemmatize(collection,dictionary):
    return re.sub(r"\b(\w+)\b", lambda m:searching_for_lemma(m.group(1), dictionary), collection)

def lemmatize_tokens(collection, dictionary):
    '''This one works whit an array of tokens '''
    return [str.replace(w, w, searching_for_lemma(w, dictionary)) for w in collection]


if __name__ == '__main__':
    sentence = ["Tom's", "boat", "is", "blue"]
    mydict = "l s b boat c is d blue"
    import re
    ##sentence = re.sub("(\S+)'s boat is (\w+)", lambda m:print(re.search("(\w+)(\s+)"+m.group(1), mydict).group(1)), sentence)
    ##sentence = re.sub(r"\b(\w+)\b", lambda m:searching_for_lemma(m.group(1), mydict), sentence)
    sentence = lemmatize_tokens(sentence, mydict)
    print(sentence)