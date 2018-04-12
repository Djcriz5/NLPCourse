
import nltk

from nltk.corpus import brown

if __name__ == '__main__':


    '''Conditional frecuency distribution'''
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    genre_word = [(genre, word)
                      for genre in ['news', 'romance']
                        for word in brown.words(categories=genre)]
    pcfd = nltk.ConditionalFreqDist(genre_word)
    print(pcfd)
    pcfd.plot(samples=days)
    pcfd.tabulate(conditions=["romance", "news"],samples=days)