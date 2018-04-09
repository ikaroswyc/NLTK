import nltk, re, pprint

from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.book import *
from nltk import memoize

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import abc

from timeit import Timer

SimpleText = 'One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'

url = "https://www.cs.utexas.edu/~vl/notes/dijkstra.html"
html = urlopen(url).read().decode('utf8')
TestText = BeautifulSoup(html, "html5lib").get_text()

def synset_sort(synsets, key):
    result = [(s.shortest_path_distance(key), s) for s in synsets]
    result = sorted(result, key=lambda x:x[0])
    return [s for (_,s) in result]


def exercise0():
    synsets = ["minke_whale.n.01", "orca.n.01", "novel.n.01", "tortoise.n.01"]
    synsets_key = 'right_whale.n.01'
    whales = [wn.synset(s) for s in synsets]
    print("sorted synsets : ", synset_sort(whales, wn.synset(synsets_key)))


def recursive_catalan(n):

    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += recursive_catalan(i)*recursive_catalan(n-i-1)
    return res


def dynamic_catalan(n):
    result = 0
    if n <= 1:
        result = 1
    for i in range(2, n):
        for j in range(i):
            result += dynamic_catalan(j) * dynamic_catalan(i - j)
    return result

def exercise26():
    # Example of timer usage:
    # print(Timer(lambda: recursive_catalan(n)).timeit(1))

    print('catalan number results')
    for i in range(0, 16):
        print ("Catalan", i ,recursive_catalan(i))

    print("Performance comparison")
    print("n = 5")
    n = 5
    print('recursive_catalan()', Timer(lambda: recursive_catalan(n)).timeit(1))
    print('dynamic_catalan()', Timer(lambda: dynamic_catalan(n)).timeit(1))
    print("n = 10")
    n = 10
    print('recursive_catalan()', Timer(lambda: recursive_catalan(n)).timeit(1))
    print('dynamic_catalan()', Timer(lambda: dynamic_catalan(n)).timeit(1))
    print("n = 15")
    n = 15
    print('recursive_catalan()', Timer(lambda: recursive_catalan(n)).timeit(1))
    print('dynamic_catalan()', Timer(lambda: dynamic_catalan(n)).timeit(1))


def summarization(text, n):
    tokenized_words = nltk.word_tokenize(text)
    tokenized_sents = nltk.sent_tokenize(text)

    word_list = [word for word in tokenized_words]
    sent_list = [sent for sent in tokenized_sents]

    freq_words = nltk.FreqDist(tokenized_words)


    res = []
    for sents in sent_list:
        sum = 0
        sent_tokenized_words = nltk.word_tokenize(sents)
        for word in sent_tokenized_words:
            sum += freq_words[word]
        res.append((sents, sum))
    result = sorted(res, key = lambda x: x[1], reverse=True)

    return result[:n]


def exercise32():


    highest1 = summarization(TestText, 7)
    print("Sentence with the highest total word frequency (n=7):")
    for (i, j) in highest1:
        print(i, end="\n")
        print()



def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise" + str(exNum)]()
    print("")


def main():
    exercise(0)
    exercise(26)
    exercise(32)


if __name__ == "__main__":
    main()

