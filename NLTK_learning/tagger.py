
import nltk
from nltk.corpus import cess_esp as cess
from nltk import UnigramTagger as ut
from nltk import BigramTagger as bt

# Read the corpus into a list,
# each entry in the list is one sentence.
from NLPUtils import TextIO_helper
print('hi')
cess_sents = cess.tagged_sents()
print('h2')

# Train the unigram tagger
uni_tag = ut(cess_sents)
print('h3')
doc = TextIO_helper.read_plain_text("Resources_assets", "e960401.htm")
spanish_tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
sent_tokenize_list = spanish_tokenizer.tokenize(doc)
sentence = sent_tokenize_list[10]
print(sentence)

# Tagger reads a list of tokens.
uni_tag.tag(sentence.split(" "))

# Split corpus into training and testing set.
train = int(len(cess_sents)*90/100) # 90%

# Train a bigram tagger with only training data.
bi_tag = bt(cess_sents[:train])

# Evaluates on testing data remaining 10%
bi_tag.evaluate(cess_sents[train+1:])

# Using the tagger.
print('hi')
print(bi_tag.tag(sentence.split(" ")))