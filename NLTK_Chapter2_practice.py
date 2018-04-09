import nltk, re, pprint

from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

def exercise2():
#     Use the corpus module to explore austen-persuasion.txt. How many word tokens does this book have? How many word types?
    print("word tokens len: ",len(nltk.corpus.gutenberg.words('austen-persuasion.txt')))
    print("word tokens type: ", len(set(nltk.corpus.gutenberg.words('austen-persuasion.txt'))))

def exercise5():
# 2.	exercise 5 In this question, consider at least 10 pairs of nouns that you believe lexically related via holonym-meronym relation. List these pairs. Then verify your assumption using Wordnet related methods of NLTK. Provide output by NLTK. Provide summary on how often NLTK supported your conjecture.
#  Investigate the holonym-meronym relations for some nouns. Remember that there are three kinds of holonym-meronym relation, so you need to use: member_meronyms(), part_meronyms(), substance_meronyms(), member_holonyms(), part_holonyms(), and substance_holonyms().
    computer = [('computer','busbar'),('computer','cathode-ray_tube'), ('computer','central_processing_unit'), ('computer','chip'), ('computer','computer_accessory'), ('computer','computer_circuit'), ('computer','data_converter'),('computer','disk_cache'), ('computer','diskette'), ('computer','hardware')]
    for group in computer:
        print(group[0],group[1])
        for sa in wn.synsets(group[0]):
            for sb in wn.synsets(group[1]):
                if sb in sa.member_holonyms():
                    print("member_holonyms")
                if sb in sa.part_holonyms():
                    print("part_holonyms")
                if sb in sa.substance_holonyms():
                    print("substance_holonyms")
                if sb in sa.member_meronyms():
                    print("member_meronyms")
                if sb in sa.part_meronyms():
                    print("part_meronyms")
                if sb in sa.substance_meronyms():
                    print("substance_meronyms")

def exercise9():
    # 3.	exercise 9 In this question, consider text1 and text7. Find at least three pairs of words which have quite different meanings across the two texts. Support your conjecture by your NLTK-based findings.
    # ◑ Pick a pair of texts and study the differences between them, in terms of vocabulary, vocabulary richness, genre, etc. Can you find pairs of words which have quite different meanings across the two texts, such as monstrous in Moby Dick and in Sense and Sensibility?
    text1.concordance("right")
    text7.concordance("right")
    text1.concordance("left")
    text7.concordance("left")
    text1.concordance("light")
    text7.concordance("light")



def exercise11():
    # Investigate the table of modal distributions and look for other patterns. Try to explain them in terms of your own impressionistic understanding of the different genres. Can you find other closed classes of words that exhibit significant differences across different genres?
    cfd = nltk.ConditionalFreqDist(
        (genre,word)
        for genre in brown.categories()
        for word in brown.words(categories = genre)
    )
    genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    cfd.tabulate(conditions = genres, samples = modals)


def exercise13():
    # ◑ What percentage of noun synsets have no hyponyms? You can get all noun synsets using wn.all_synsets('n').
    n_length = len([w for w in list(wn.all_synsets('n'))])
    no_hy = len([w for w in list(wn.all_synsets('n')) if len(list(w.hyponyms())) == 0])
    print("ratio: ", no_hy / n_length)

def exercise18():
    # 6.	exercise 18 In addition to omitting stopwords also omit punctuation. Run your function on Brown corpus. What are the first 5 bigrams your function outputs.
    # ◑ Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.

    word = nltk.corpus.brown.words(categories='news')
    stop = stopwords.words('english')
    res = nltk.FreqDist(nltk.bigrams(w for w in word if w.isalpha() and w not in stop)).most_common(50)
    print("res: ", res)
def exercise27():
    # 7.	exercise 27 What are the values you have computed. Note that the same lemma may occur in different synsets. Your code should account for this fact
    # ★ The polysemy of a word is the number of senses it has. Using WordNet, we can determine that the noun dog has 7 senses with: len(wn.synsets('dog', 'n')). Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.
    tag = ['n','v','a', 'r']
    avg  = 0.0
    poly = 0.0
    total = 0.0
    for e in tag:

        for synset in wn.all_synsets(e):
            sense = []
            for lemma in synset.lemma_names():
                sense.append(lemma)
            for n in sense:
                poly += len(wn.synsets(n, e))
                total += 1
            avg = poly / total
        print(avg)





def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise"+str(exNum)]()
    print("")


def main():
    # exercise(2)
    # exercise(5)
    # exercise(9)
    #  exercise(11)
    # exercise(13)
    #  exercise(18)
     exercise(27)


if __name__ == "__main__":
    main()

