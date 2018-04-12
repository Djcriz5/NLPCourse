import nltk
from nltk.corpus import cess_esp as corpus
from nltk import UnigramTagger as unigramTagger
import re
from NLPUtils import TextIO_helper, ArticleSeparator
from NLPUtils import NormalizeText


if __name__ == '__main__':
    corpus_tagged = corpus.tagged_sents()
    tagger = unigramTagger(corpus_tagged)
    doc = TextIO_helper.read_raw_text("Resources_assets", "e960404.htm").read()
    rex = re.compile(r'<title.*?>(.*?)<hr>(?P<Article>.*?)<hr>', re.S | re.M)
    articles = ArticleSeparator.get_normalized_articles(doc, rex, "Resources_assets", "stopwords_es.txt",
                                  "Resources_assets", "lemmatization-es.txt")
    tagged_sentences = [tagger.tag(sentenceten) for sentenceten in articles]
    print("Ejemplo etiquetado de articulo")
    print(tagged_sentences[1])
    print("Sustantivos")
    nouns= list()
    for tagged_sentence in tagged_sentences:
        for tup in tagged_sentence:
            if tup[1] is not None and tup[1].startswith("n"):
                ##print(format(tup[0])+" : "+tup[1])
                nouns.append(tup[0])
    nouns= sorted(set(nouns))
    print(nouns.__len__())

