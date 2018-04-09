from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

SimpleText = 'One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'
url = "https://www.cs.utexas.edu/~vl/notes/dijkstra.html"

def exercise6():
    print("part b")
    print("not implemented")
    print("part c")
    print("not implemented")
    print("part f")
    print("not implemented")


def exercise7():
    print("part a")
    print("not implemented")

def unknown1(raw, word_list):
    find = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw)
    res = [w for w in find if w not in word_list]
    print(res)
    print(len(res))

def unknown2(raw, word_list):
    tokens = nltk.word_tokenize(raw)
    wnl = nltk.WordNetLemmatizer()

    token_list = set([wnl.lemmatize(t) for t in tokens])

    res = [w for w in token_list if w not in word_list]
    print("res_length: ", len(res))
def exercise21():
    # 3.	exercise 21: In this question, use URL https://www.cs.utexas.edu/~vl/notes/dijkstra.html
    # What kind of differences do you see in the tokens you retrieve if you use nltk.word_tokenize instead of re.findall(). Use nltk.WordNetLemmatizer() on your tokens before checking them against the Words Corpus. Do you find fewer or more unknown words? Why?
    # Write a function unknown() that takes a URL as its argument, and returns a list of unknown words that occur on that webpage. In order to do this, extract all substrings consisting of lowercase letters (using re.findall()) and remove any items from this set that occur in the Words Corpus (nltk.corpus.words). Try to categorize these words manually and discuss your findings.
    html = urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html,"html5lib").get_text()
    words_list = [w for w in nltk.corpus.words.words('en') if w.islower()]
    unknown1(raw,words_list)
    unknown2(raw,words_list)
    print("not implemented")

def pig_latin_word(word):
    charlist = [ch for ch in word]
    for i in charlist:
        if word[i] in "aeiou":
            return word + "yay"
        else:
            return word[i+1:] + word[i]+'ay'




def exercise25():
    # Pig Latin is a simple transformation of English text. Each word of the text is converted as follows: move any consonant (or consonant cluster) that appears at the start of the word to the end, then append ay, e.g. string → ingstray, idle → idleay. http://en.wikipedia.org/wiki/Pig_Latin
    # a.	Write a function to convert a word to Pig Latin.
    # b.	Write code that converts text, instead of individual words.
    # c.	Extend it further to preserve capitalization, to keep qu together (i.e. so that quiet becomes ietquay), and to detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style).
    word = nltk.word_tokenize(SimpleText)
    pig_latin_word('apple')
    print("not implemented")



def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise" + str(exNum)]()
    print("")


def main():
    # exercise(6)
    # exercise(7)
    # exercise(21)
    exercise(25)


if __name__ == "__main__":
    main()

