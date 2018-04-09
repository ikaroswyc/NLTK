import nltk, re, pprint

from nltk.book import *
from nltk.corpus import stopwords
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

book = nltk.corpus.genesis
text = book.words("english-web.txt")
stop_words = nltk.corpus.stopwords.words("english")

def exercise2():

    print("word tokens: ", len(nltk.corpus.gutenberg.words('austen-persuasion.txt')))
    print("word types: " , len(set(nltk.corpus.gutenberg.words('austen-persuasion.txt'))))


def exercise5():

    list_computer = [("computer","busbar"),("computer","cathode-ray_tube"), ("computer","central_processing_unit"),
                     ("computer", "chip"), ("computer","computer_accessory"), ("computer","computer_circuit"),
                     ("computer", "data_converter"), ("computer", "disk_cache"), ("computer", "diskette"),
                     ("computer", "hardware")]
    for group in list_computer:
        print(group[0],group[1])
        for sa in wn.synsets(group[0]):
            for sb in wn.synsets(group[1]):
                if sb in sa.member_meronyms():
                    print("member meronyms")
                if sb in sa.part_meronyms():
                    print("part_meronyms")
                if sb in sa.substance_meronyms():
                    print("substance_meronyms")
                if sb in sa.member_holonyms():
                    print("member_holonyms")
                if sb in sa.part_holonyms():
                    print("part_holonyms")
                if sb in sa.substance_holonyms():
                    print("substance_holonyms")

def exercise9():


    print("text1 vocabulary: " , len(text1))
    print("text1 vocabulary richness: " , len(set(text1))/len(text1))
    print("text7 vocabulary: " , len(text7))
    print("text7 vocabulary richness: " , len(set(text7))/len(text7))
    print("light in text 1: ")
    text1.concordance("light")
    print("light in text 7: ")
    text7.concordance("light")
    print("right in text 1: ")
    text1.concordance("right")
    print("right in text 7: ")
    text7.concordance("right")
    print("hand in text 1: ")
    text1.concordance("hand")
    print("hand in text 7: ")
    text7.concordance("hand")


def exercise11():
    cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))
    genres = ['adventure', 'editorial', 'fiction', 'government', 'mystery']
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    cfd.tabulate(conditions=genres, samples=modals)


def exercise13():
    allword = len([synset for synset in list(wn.all_synsets('n'))])
    n = len([synset for synset in list(wn.all_synsets('n')) if len(list(synset.hyponyms()))==0])
    percentage = n / allword
    print("the percentage is ", percentage)


def exercise18():
    emma = nltk.corpus.gutenberg.words('austen-emma.txt')
    stopen = stopwords.words('english')
    print(nltk.FreqDist(nltk.bigrams(w for w in emma
                                     if w not in stopen
                                     and w.isalpha())).most_common(50))



def exercise27():
    polysemy = 0.00
    num = 0.00

    english = ['n', 'v', 'a', 'r']
    print("n = noun; v = verb, a = adjective, r = adverb")

    for e in english:
        for synset in wn.all_synsets(e):
            lename = []

            for lemma in synset.lemma_names():
                lename.append(lemma)


            for n in lename:
                polysemy += len(wn.synsets(n, e))
                num += 1

            average = 0.000
            average = polysemy / num
        print("The average polysemy of {} is {:.3f}".format(e, average))




def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise"+str(exNum)]()
    print("")


def main():
    # exercise(2)
    # exercise(5)
    # exercise(9)
    # exercise(11)
    # exercise(13)
    # exercise(18)
    exercise(27)


if __name__ == "__main__":
    main()
