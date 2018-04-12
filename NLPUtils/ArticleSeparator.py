import nltk
import re
from NLPUtils import NormalizeText, TextIO_helper


def get_raw_articles(collection, regex):
    """
    :param collection: the text where you want to extract the articles
    :param regex: this is the regular expression which defines where are the articles
           the group which contains the articles has to be named as "Article" (?P<Article> ----- )
    :return: collections.Iterable[__Match[T]] which contains the articles in a raw format
    """
    return regex.finditer(collection)

def get_raw_articles_list(collection, regex):
    """
    :param collection: the text where you want to extract the articles
    :param regex: this is the regular expression which defines where are the articles
           the group which contains the articles has to be named as "Article" (?P<Article> ----- )
    :return: a list which contains the articles in a raw format
    you also need to .group("Article") if you want the article content
    """
    return list(regex.finditer(collection))


def get_lemmatized_articles(collection, regex,package_lemma,lemmatization_dictionary):
    """
    :param collection: the text where you want to extract the articles
    :param regex: this is the regular expression which defines where are the articles
           the group which contains the articles has to be named as "Article" (?P<Article> ----- )
    :return: collections.Iterable[__Match[T]] which contains the articles in a raw format
    """
    match = get_raw_articles(collection, regex)
    dictionaryMap = NormalizeText.create_dic_map(TextIO_helper.read_raw_text(package_lemma, lemmatization_dictionary))
    articles=[NormalizeText.lemmatize(NormalizeText.parse_html(m.group("Article")).lower(), dictionaryMap)
                                                               for m in match]
    return articles




def get_normalized_articles(collection, regex,package_stopwords, stopwords,package_lemma, lemmatization_dictionary):
    """
    :param collection: this is the path of the collection where we will search for the articles
    :param regex: this is the regular expression which defines where are the articles
           the group which contains the articles has to be named as "Article" (?P<Article> ----- )
    :param stopwords: this is a collection of stopwords that will be removed
    :param lemmatization_dictionary: the path of a text file which contains lemmas for a collection of words
    :return: articles: an array of articles in the collection
    """
    match = get_raw_articles(collection, regex)
    dictionaryMap = NormalizeText.create_dic_map(TextIO_helper.read_raw_text(package_lemma, lemmatization_dictionary))
    stopwordsdic = TextIO_helper.read_raw_text(package_stopwords, stopwords).read()
    articles = [
        NormalizeText.lemmatize_and_remove_stopwords_punctuations(NormalizeText.parse_html(m.group("Article")).lower(), dictionaryMap, stopwordsdic) for m in match]
    return articles


def get_most_commmon_words_in_article(corpus, regex,package_stopwords,stopwords, package_lemma, lemmatization_dictionary, n):
    """
     :param corpus: this is the path for the corpus where we will search for the articles
     :param regex:  regular expression which defines a search pattern for matching articles.
            The group which contains the articles has to be named as "Article" (?P<Article> ----- )
     :param stopwords: this is a collection of stopwords that will be removed from the collection
     :param lemmatization_dictionary: the path of a text file which contains a lemmas dictionary
     :return: most_common: an array which contains the "n" most common words in the collection articles
    """
    match = get_raw_articles(corpus, regex)
    dictionaryMap = NormalizeText.create_dic_map(TextIO_helper.read_raw_text(package_lemma, lemmatization_dictionary))
    stopwordsdic = TextIO_helper.read_raw_text(package_stopwords, stopwords).read()
    most_common = [nltk.FreqDist(
        NormalizeText.lemmatize_and_remove_stopwords_punctuations(NormalizeText.parse_html(m.group("Article")).lower(), dictionaryMap, stopwordsdic)).most_common(n) for m in match]
    return most_common


def demo():
    """
    This is a test of the app which separate by articles the e960404.htm corpus
    and then it returns the most common words in each article
    in this corpus we found the articles between an <article> tag and a <hr> tag
    the searched text is represented by the name group (?P<text>.*?)
    where .*? is any character and ?P<text> is the name given (article)
    """
    doc = TextIO_helper.read_raw_text("Resources_assets","e960404.htm").read()
    rex = re.compile(r'<title.*?>(.*?)<hr>(?P<Article>.*?)<hr>', re.S | re.M)
    ##print(get_most_commmon_words_in_article(doc, rex, "Resources_assets", "stopwords_es.txt",
                                                   ##   "Resources_assets", "lemmatization-es.txt", 5)[2])
    #print(list(get_n_article(doc, rex)).__getitem__(1).group("Article"))
    print(get_normalized_articles(doc,rex,"Resources_assets", "stopwords_es.txt",
                                                     "Resources_assets", "lemmatization-es.txt")[1])


if __name__ == '__main__':
    demo()
