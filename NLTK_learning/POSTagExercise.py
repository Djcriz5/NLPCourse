import nltk
from nltk.tag.stanford import StanfordTagger
from NLPUtils import TextIO_helper

def demo():
    doc = TextIO_helper.read_plain_text("Resources_assets", "e960401.htm")
    spanish_tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
    sent_tokenize_list = spanish_tokenizer.tokenize(doc)
    print(sent_tokenize_list[10])
    spanish_postagger= StanfordPOSTagger(tagger,jar)

    post_tagged_list = spanish_postagger.tag(sent_tokenize_list[10].split())
    print(post_tagged_list)



if __name__ == '__main__':
    demo()