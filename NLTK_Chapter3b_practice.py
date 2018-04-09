from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen

from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

SimpleText = 'One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'


def exercise1():
    # 1.	Wh-words in English are used in questions, relative clauses and exclamations. Consider the set of wh-words to consist exactly of the following members: what, where, when, which, who, whom, whose, why.
    # a)	Report how many wh-words occurred in text2.
    # b)	Repeat the exercise for text7. Report how many wh-words occurred in text 7.
    size2 = len([w.lower() for w in text2 if re.findall(r'what|where|when|which|who|whom|whose|why', w)])
    print("text2: ", size2)

def avg_letter(text,category):
    word_num = len(text.words(categories = category))
    smash_text = ''.join(text.words(categories = category))
    len_smash = len(smash_text)
    avg = len_smash / word_num
    return avg

def avg_word(text, category):
    sent_num = len(text.sents(categories = category))
    word_num = len(text.words(categories = category))
    avg = word_num / sent_num
    return avg
def ari(text, category):
    uw = avg_letter(text,category)
    us = avg_word(text,category)
    ari = (4.71 * uw) + (0.5 * us) - 21.43
    return ari

def exercise29():
    # Readability measures are used to score the reading difficulty of a text, for the purposes of selecting texts of appropriate difficulty for language learners. Let us define μw to be the average number of letters per word, and μs to be the average number of words per sentence, in a given text. The Automated Readability Index (ARI) of the text is defined to be: 4.71 μw + 0.5 μs - 21.43. Compute the ARI score for various sections of the Brown Corpus, including section f (lore) and j (learned). Make use of the fact that nltk.corpus.brown.words() produces a sequence of words, while nltk.corpus.brown.sents() produces a sequence of sentences
    for category in brown.categories():
        print(category+ ':' + str(ari(brown,category)))



def exercise30():
    # 3.	exercise 30.  In this question, consider SimpleText for reporting your results.
    # ◑ Use the Porter Stemmer to normalize some tokenized text, calling the stemmer on each word. Do the same thing with the Lancaster Stemmer and see if you observe any differences.
    tokens = nltk.word_tokenize(SimpleText)
    porter = nltk.PorterStemmer()
    lancaster = nltk.LancasterStemmer()
    porter_list = [porter.stem(t) for t in tokens]
    lancaster_list = [lancaster.stem(t) for t in tokens]
    print("porter: ", porter_list)
    print("lancaster: ", lancaster_list)

def ARI(raw):
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    sents = [nltk.word_tokenize(s) for s in sent_tokenizer.tokenize(raw)]
    words = nltk.word_tokenize(raw)
    print('words', words)
    w = ''.join(words)
    uw = len(w)/len(words)
    us = len(words)/len(sents)
    return (4.71 * uw) + (0.5 * us) - 21.43

def exercise40():
    # 4.	exercise 40.  Section 3.8 in “Sentence Segmentaion” lists an example of using Punkt. Use nltk.word_tokenize() function to tokenize given text into words.
    # a)	Test your code on “ABC rural News”.  Command   nltk.corpus.abc.raw('rural.txt') allows one to access “ABC rural News” as a string. Report your results on this text.
    # b)	Report what your code computes for “ABC Science news” from ntlk.corpus.abc .
    # ★ Obtain raw texts from two or more genres and compute their respective reading difficulty scores as in the earlier exercise on reading difficulty. E.g. compare ABC Rural News and ABC Science News (nltk.corpus.abc). Use Punkt to perform sentence segmentation.
    print("rural: ", ARI(nltk.corpus.abc.raw('rural.txt')))


def exercise(exNum):

    print("Exercise {}".format(exNum))

    globals()["exercise" + str(exNum)]()
    print("")


def main():
    # exercise(1)
    # exercise(29)
    #  exercise(30)
     exercise(40)


if __name__ == "__main__":
    main()

