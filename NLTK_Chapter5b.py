from __future__ import division

import operator

import nltk, re, pprint

from urllib.request import urlopen
from collections import defaultdict
from nltk.book import *
from collections import Counter
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import abc
from operator import itemgetter
from itertools import chain

SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word.lower()) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())



def exercise1():
    print("Part a")

    # brown_words = brown.words()
    # brown_tags = brown.tagged_words()
    # tagdict = findtags('NNS', nltk.corpus.brown.tagged_words())  # a dictionary with a list of words have 'NNS' tag
    # lem = nltk.WordNetLemmatizer()
    # words = []
    # cf = nltk.FreqDist(brown_words)
    # # print brown_words[:50]
    #
    # tag = 'NNS'
    # for plural in tagdict[tag]:
    #     singular = lem.lemmatize(plural.lower())
    #     freq_sing = cf[singular]
    #     freq_plur = cf[plural]
    #     if freq_plur > freq_sing:
    #         words.append(plural)
    #         words.sort(key=lambda a: cf[a], reverse=True)
    # print (tag, "5 plural nouns more common:", words[:5])  # last elements

    brown_words = brown.words()
    brown_tags = brown.tagged_words()
    tagdict = findtags('NNS', nltk.corpus.brown.tagged_words())  # a dictionary with a list of words have 'NNS' tag

    total_list = []
    for tag in sorted(tagdict):
        total_list.append(tagdict[tag])
    print("total_list: ", total_list)

    total_list_w = list(chain.from_iterable(total_list))
    print("total_list_w:", total_list_w)
    total_list_sorted = sorted(total_list_w, key= operator.itemgetter(1), reverse = True)
    print("total_list_sorted" , total_list_sorted)

    lem = nltk.WordNetLemmatizer()
    words = []
    first_element = [x for x,_ in total_list_sorted]

    print("first element", first_element)
    cf = nltk.FreqDist(brown_words)
    for i in first_element:
        singular = lem.lemmatize(i)
        freq_sing = cf[singular]
        freq_plur = cf[i]
        if freq_plur > freq_sing:
             words.append(i)
    print("words:", words[:5])


    print("Part b")
    tags = [b[1] for (a, b) in nltk.bigrams(brown_tags)]
    fd = nltk.FreqDist(tags)
    print(fd.most_common(5))
    print("The tags represent the decrease in frequency.")

    print("Part c")
    categories = ['humor', 'romance', 'government']

    for category in categories:

        category_tags = brown.tagged_words(categories=category)
        tagList = [a[1] for (a, b) in nltk.bigrams(category_tags) if b[1].startswith('N') and b[1] != 'N']
        fd = nltk.FreqDist(tagList).most_common()
        first_element = [x for x, _ in list(fd)]
        print (category, ', '.join(first_element[:3]))


def exercise2():
    news_tagged_sents = brown.tagged_sents(categories='news')
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(news_tagged_sents, backoff=t0)
    t2 = nltk.BigramTagger(news_tagged_sents, backoff=t1)
    t3 = nltk.TrigramTagger(news_tagged_sents, backoff=t2)
    news_test_sents = t3.evaluate(news_tagged_sents)
    print (news_test_sents)

    print("Part a")
    lore_tagged_sents = brown.tagged_sents(categories='lore')

    lore_tagger = t3.evaluate(lore_tagged_sents)

    print("Compare DefaultTagger of lore and news:",lore_tagger, news_test_sents)


    print("Part b")
    lore_size = 199  # 200th sentence
    lore_train_sents = lore_tagged_sents[:lore_size]
    lore_test_sents = lore_tagged_sents[lore_size:]

    unigram_tagger = nltk.UnigramTagger(lore_tagged_sents)
    unigram_val = unigram_tagger.evaluate(lore_tagged_sents)

    bigram_tagger = nltk.BigramTagger(lore_train_sents)
    bigram_val = bigram_tagger.evaluate(lore_test_sents)

    trigram_tagger = nltk.BigramTagger(lore_train_sents)
    trigram_val = trigram_tagger.evaluate(lore_test_sents)
    print(t3.tag(brown.sents(categories='lore')[199]))
    # print(brown.sents(categories='lore')[199])
    print("Unigram", unigram_val, 'vs.Bigram', bigram_val, 'vs.Trigram', trigram_val)



def exercise3():
    news_tagged_sents = brown.tagged_sents(categories='news')


    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(news_tagged_sents,backoff=t0)
    t2 = nltk.BigramTagger(news_tagged_sents, backoff=t1)
    t3 = nltk.TrigramTagger(news_tagged_sents,backoff=t2)


    # category lore
    lore_tagged_sents = brown.tagged_sents(categories='lore')
    lore_trigram_val = t3.evaluate(lore_tagged_sents)

    t4 = nltk.TrigramTagger(news_tagged_sents)
    lore_trigram_val_without = t4.evaluate(lore_tagged_sents)

    print("Brown corpus category lore value", lore_trigram_val)
    print("Brown corpus category lore value without", lore_trigram_val_without)

    print ("Category news tagger peforms better because it evaluates tags of the same category,")
    print ("thus yielding more accurate results. It performs better if evaluate tags in the same category")


def exercise4():
    wn_words = wn.all_synsets()# list of words

    lemma_str = []
    for i in wn_words:
        for lemma in i.lemma_names():
            lemma_str.append(lemma)

    lemma_str_set = list(set(lemma_str))

    total_count = 0
    for i in lemma_str_set:
        count = 0
        if len(wn.synsets(i, pos='a')) > 0:
            count += 1
        if len(wn.synsets(i, pos='n')) > 0:
            count += 1
        if len(wn.synsets(i, pos='v')) > 0:
            count += 1
        if len(wn.synsets(i, pos='r')) > 0:
            count += 1
        if count > 1:
            total_count += 1

    result = total_count / len(lemma_str_set)
    print(result)


def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise"+str(exNum)]()
    print("")


def main():
     exercise(1)
     # exercise(2)
     # exercise(3)
     # exercise(4)


if __name__ == "__main__":
    main()

