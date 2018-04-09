import nltk, re, pprint

from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import abc

SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'
AppleText = 'all apes ate apples'
test = "chat chien chair chic"

url = "https://www.cs.utexas.edu/~vl/notes/dijkstra.html"
html = urlopen(url).read().decode('utf8')
TestText = BeautifulSoup(html, "html.parser").get_text()
snippet = "to begin with I would like to thank the College of Natural Sciences for the most honouring Invitation to address its newest flock of Bachelors on this most festive day. I shall do my best"

def novel10(text):

	cut = int(0.9 * len(text))

	first_part, second_part = text[:cut], text[cut:]
	unique_first_part = set(first_part)
	unique_second_part = set(second_part)

	return [word for word in unique_second_part if word not in unique_first_part]


def exercise14():
    tokens = nltk.word_tokenize(TestText)
    lowerlist = [w.lower() for w in tokens]
    result = novel10(lowerlist)
    result = sorted(result)[:10]

    print("first ten element: ", result)



def shorten(text, n):

    tokens = nltk.word_tokenize(text)
    fd = FreqDist(tokens)
    charlist= [w for (w,n) in fd.most_common(n)]
    str = []
    for t in tokens:
        if t not in charlist:
            str.append(t)
    str = ' '.join(str)
    return str

def exercise17():

    print("Part a")
    print("n = 20")
    print (shorten(TestText, 20))
    print("n = 35")
    print (shorten(TestText, 35))
    print("n = 50")
    print (shorten(TestText, 50))
    print("n = 65")
    print (shorten(TestText, 65))

    print("Part b")
    print(shorten(snippet, 20))
    print("length: ",len(shorten(snippet,20)))



def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value


def compressedword(trie, token):

    step = 0
    subtrie = trie

    for character in token:
        subtrie = subtrie.get(character)
        print("subtrie:", subtrie)
        subtrie_keys = list(subtrie.keys())
        step += 1
        if(len(subtrie_keys) == 1 ):
            break


    return step



def exercise30():
    tokens = nltk.word_tokenize(test)
    trie = {}

    for word in tokens:
        insert(trie, word, ' ')
    trie = dict(trie)  # for nicer printing
    pprint.pprint(trie)

    unique_chars = []  # define a list of unique character output
    for word in tokens:
        lens = compressedword(trie, word)
        print (word, '=>', lens)

        output = word[:lens]
        unique_chars.append(output)
        print (word, '=>', 'output', output)
    unique = ' '.join(unique_chars)
    compression = len(unique) / len(test)
    print (unique_chars)
    print ('compression', compression)



def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise"+str(exNum)]()
    print("")


def main():
     exercise(14)
     exercise(17)
     exercise(30)


if __name__ == "__main__":
    main()

