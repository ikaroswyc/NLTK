from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen

from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

SimpleText = 'One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'


def exercise1():

    size2 = len([w for w in text2 if re.findall(r'what|where|when|which|who|whom|whose|why',w)])
    print("text2: ", size2)

    size7 = len([w for w in text7 if re.findall(r'what|where|when|which|who|whom|whose|why',w)])
    print("text7: ", size7)


def average_num_words_per_sentence(text, category):

	sent_num = len(text.sents(categories=category))
	word_num = len(text.words(categories=category))
	return word_num / sent_num

def average_num_letters(text, category):

	word_num = len(text.words(categories=category))
	smash_text = ''.join(text.words(categories=category))
	letters_len = len(smash_text)

	return letters_len / word_num

def ari(text, category):

	uw = average_num_letters(text, category)
	us = average_num_words_per_sentence(text, category)
	ari = (4.71 * uw ) + ( 0.5 * us ) - 21.43
	return ari

def exercise29():

    for category in brown.categories():
        print(category + ': ' + str(ari(brown, category)))




def exercise30():

    porter = nltk.PorterStemmer()
    lancaster = nltk.LancasterStemmer()
    port_list = []
    lan_list = []
    print(SimpleText)

    Simple = nltk.word_tokenize(SimpleText)
    for word in Simple:
        port = porter.stem(word)
        port_list.append(port)
        lan = lancaster.stem(word)
        lan_list.append(lan)
    print("porter: ", port_list)
    print("lancaster: ", lan_list)

def ARI(raw):
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sents = [nltk.word_tokenize(s) for s in sent_tokenizer.tokenize(raw)]

    words = nltk.word_tokenize(raw)
    summation_w = 0.0
    for w in words:
        summation_w += len(w)
    summation_s = 0.0
    for s in sents:
        summation_s += len(s)

    av_wordlength = summation_w / len(words)
    av_sentlength = summation_s / len(sents)
    return (4.71 * av_wordlength) + (0.5 * av_sentlength) - 21.43

def exercise40():
    print ("rural: ", ARI(nltk.corpus.abc.raw("rural.txt")))
    print ("Science: ", ARI(nltk.corpus.abc.raw("science.txt")))


def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise" + str(exNum)]()
    print("")


def main():
     exercise(1)
     exercise(29)
     exercise(30)
     exercise(40)


if __name__ == "__main__":
    main()