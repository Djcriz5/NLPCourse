import nltk
from nltk.corpus import cess_esp as corpus
from nltk import UnigramTagger as unigramTagger

from NLPUtils import TextIO_helper

if __name__ == '__main__':
    corpus_tagged = corpus.tagged_sents()
    tagger = unigramTagger(corpus_tagged)
    doc = TextIO_helper.read_plain_text("Resources_assets", "e960401.htm")
    spanish_tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
    sent_tokenize_list = spanish_tokenizer.tokenize(doc)
    sentenceten = sent_tokenize_list[10]
    print(sentenceten)
    print("Oracion etiquetada")
    tagged_sentence = tagger.tag(sentenceten.split())
    print(tagged_sentence)
    print("sustantivos")
    nouns = [tup[0] for tup in tagged_sentence if tup[1] is not None and tup[1].startswith("n")]
    print(nouns)
