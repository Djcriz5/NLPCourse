from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
exercises=list()

if __name__ == '__main__':
    ##print(stopwords.words("spanish"))
    car = wn.synsets('car')
    print("Synonym sets")
    print(car)
    print("Synonym set")
    print(car.__getitem__(1))
    print("Definition")
    print(car.__getitem__(1).definition())
    print("lemmas (synonyms)")
    print(car.__getitem__(1).lemmas())
    print("more specific Hyponyms (types of)")
    print(car.__getitem__(1).hyponyms())
    from urllib import urlopen

    url = "http://www.gutenberg.org/files/2554/2554.txt"
    raw = urlopen(url).read()
