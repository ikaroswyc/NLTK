from nltk.book import *
import numpy
import matplotlib
import tkinter
from matplotlib import*
import nltk

def exercise4():
    print(len(text2))
    print(len(set(text2)))



def exercise5():

    print("The lexical diversity of humor is 0.231, while romance is 0.121. Therefore, humor is more lexically diverse.")



def exercise6():
    # text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])
    print()


def exercise7():
    print("text 5: ")
    text5.collocations()


def exercise17():
    text9.index('sunset')
    text9[613:644]
    print("implemented")


def exercise18():
    len(set(sent1))
    len(set(sent2))
    len(set(sent3))
    len(set(sent4))
    len(set(sent5))
    len(set(sent6))
    len(set(sent7))
    len(set(sent8))

    len(sent1)
    len(sent2)
    len(sent3)
    len(sent4)
    len(sent5)
    len(sent6)
    len(sent7)
    len(sent8)

    set(sent1)
    set(sent2)
    set(sent3)
    set(sent4)
    set(sent5)
    set(sent6)
    set(sent7)
    set(sent8)





def exercise22():
    print("part1: ")
    word = nltk.FreqDist([w for w in text5 if len(w) == 4 and w.isalpha()])
    print("four-letter word: ",word)
    most = nltk.FreqDist([w for w in text5 if len(w) == 4 and w.isalpha()]).most_common(5)
    print("most_common 5: ", most)





def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise" + str(exNum)]()
    print("")


def main():
    exercise(4)
    exercise(5)
    exercise(6)
    exercise(7)
    exercise(17)
    exercise(18)
    exercise(22)


if __name__ == "__main__":
    main()