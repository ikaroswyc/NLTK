from nltk.book import *
import numpy
import matplotlib
import tkinter


def exercise4():
    print(len(text2))
    print(len(set(text2)))



def exercise5():
    print("humor")


def exercise6():
    text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])
    print("implemented")


def exercise7():
    text5.collocations()
    print("Elinor and Marianne show a lot in the book. When Edward shows, Willoughby does not show. Elinor and Marianne might be the couple.")


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


print("implemented")


def exercise22():
    FreqDist([w for w in text5 if len(w) == 4 and w.isalpha()])
    FreqDist([w for w in text5 if len(w) == 4 and w.isalpha()]).most_common(5)

    fdist['JOIN']
    fdist.freq('JOIN')

    fdist['PART']
    fdist.freq('PART')

    fdist['that']
    fdist.freq('that')

    fdist['what']
    fdist.freq('what')

    fdist['here']
    fdist.freq('here')


print("implemented")


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