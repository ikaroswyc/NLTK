from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen

from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import abc

SimpleText = 'One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'


def exercise1():

    brown_tagged_sents = brown.tagged_sents(categories='news')
    brown_sents = brown.sents(categories='news')
    unigram_tagger_news = nltk.UnigramTagger(brown_tagged_sents)
    news_evaluate = unigram_tagger_news.evaluate(brown_tagged_sents)
    print('news_evaluate: ', news_evaluate)


    brown_tagged_sents = brown.tagged_sents(categories='lore')
    lore_evaluate = unigram_tagger_news.evaluate(brown_tagged_sents)
    print('lore_evaluate: ', lore_evaluate)



    print('we can see that lore_evalute is ', lore_evaluate, 'news_evaluate is ', news_evaluate,'lore is a lower than news')

    lore_tagger = unigram_tagger_news.tag(brown_sents[199])
    print('lore_tagger_200th: ', lore_tagger)

def total_count(cate):
    pp_list = []
    humor_tagged_words = brown.tagged_words(categories = cate)

    for i in humor_tagged_words:
        if i[1].startswith("PP") and not i[1] == 'PP$':
            pp_list.append(i[0])

    male_list = ['himself', 'his', 'him', 'he', "he's", "he'd", "he'll"]
    female_list = ['herself', 'her', 'hers', 'she', "she's", "she'd", "she'll"]

    male_count = 0
    female_count = 0

    for i in pp_list:
        if i.lower() in male_list:
            male_count = male_count + 1
        if i.lower() in female_list:
            female_count = female_count + 1

    total_count_humor = male_count / female_count

    print("the_ratio_of_mas_to_fem: ", cate," ", total_count_humor)


def exercise2():
    print("Part 1: humor")
    tagged_text = brown.tagged_words(categories='humor')
    cfd = nltk.ConditionalFreqDist(tagged_text)
    conditions = cfd.conditions()

    JJ_words = [condition for condition in conditions if cfd[condition]['JJ'] != 0]
    JJ_words.sort()
    print('JJ_words_len: ', len(JJ_words))
    print('JJ_words_humor: ', JJ_words[:5])

    print("Part 1: romance")
    tagged_text = brown.tagged_words(categories='romance')
    cfd = nltk.ConditionalFreqDist(tagged_text)
    conditions = cfd.conditions()

    JJ_words = [condition for condition in conditions if cfd[condition]['JJ'] != 0]
    JJ_words.sort()
    print('JJ_words_len: ', len(JJ_words))
    print('JJ_words_romance: ', JJ_words[:5])

    print("Part 1: government")
    tagged_text = brown.tagged_words(categories='government')
    cfd = nltk.ConditionalFreqDist(tagged_text)
    conditions = cfd.conditions()

    JJ_words = [condition for condition in conditions if cfd[condition]['JJ'] != 0]
    JJ_words.sort()
    print('JJ_words_len: ', len(JJ_words))
    print('JJ_words_government: ', JJ_words[:5])

    print("Part 2: humor")

    tagged_text = brown.tagged_words(categories='humor')
    cfd = nltk.ConditionalFreqDist(tagged_text)
    conditions = cfd.conditions()
    two_words = [condition for condition in conditions if cfd[condition]['NNS'] and cfd[condition]['VBZ']]
    two_words.sort()
    print('two_words_len: ', len(two_words))
    print('two_words_humor:', two_words[:10])

    print("Part 2: romance")

    tagged_text = brown.tagged_words(categories='romance')
    cfd = nltk.ConditionalFreqDist(tagged_text)
    conditions = cfd.conditions()
    two_words = [condition for condition in conditions if cfd[condition]['NNS'] and cfd[condition]['VBZ']]
    two_words.sort()
    print('two_words_len: ', len(two_words))
    print('two_words_romance:', two_words[:10])

    print("Part 2: government")

    tagged_text = brown.tagged_words(categories='government')
    cfd = nltk.ConditionalFreqDist(tagged_text)
    conditions = cfd.conditions()
    two_words = [condition for condition in conditions if cfd[condition]['NNS'] and cfd[condition]['VBZ']]
    two_words.sort()
    print('two_words_len: ', len(two_words))
    print('two_words_government:', two_words[:10])

    print("Part 3: humor")

    three_words = []
    tagged_text = brown.tagged_words(categories='humor')
    trigrams = list(nltk.trigrams(tagged_text))
    for (w1, t1),(w2,t2), (w3,t3) in trigrams:
        if t1 == 'IN' and t2 == 'AT' and t3 == 'NN':
            three_words.append((w1, w2, w3))


    print( nltk.FreqDist(three_words).most_common(3))

    print("Part 3: romance")

    three_words = []
    tagged_text = brown.tagged_words(categories='romance')
    trigrams = list(nltk.trigrams(tagged_text))
    for (w1, t1),(w2,t2), (w3,t3) in trigrams:
        if t1 == 'IN' and t2 == 'AT' and t3 == 'NN':
            three_words.append((w1, w2, w3))


    print( nltk.FreqDist(three_words).most_common(3))

    print("Part 3: government")

    three_words = []
    tagged_text = brown.tagged_words(categories='government')
    trigrams = list(nltk.trigrams(tagged_text))
    for (w1, t1),(w2,t2), (w3,t3) in trigrams:
        if t1 == 'IN' and t2 == 'AT' and t3 == 'NN':
            three_words.append((w1, w2, w3))


    print( nltk.FreqDist(three_words).most_common(3))

    print("Part 4: ")
    total_count('humor')
    total_count('romance')
    total_count('government')


def exercise3():
    print("Part 1")
    count = 0
    brown_news_tagged = brown.tagged_words()
    data = nltk.ConditionalFreqDist((word.lower(), tag)
                                    for (word, tag) in brown_news_tagged)
    for word in sorted(data.conditions()):
        if len(data[word]) == 5:
            tags = [tag for (tag, _) in data[word].most_common()]
            print(word, ' '.join(tags))
            count = count + 1
    print("count:", count)

    print("Part 2")



    brown_news_tagged = brown.tagged_words()
    top_word = {}
    for i in brown_news_tagged:
        if i[0].lower() not in top_word:
            top_word[i[0].lower()] = [i[1]]
        else:
            tmp = top_word[i[0].lower()]
            tmp.append(i[1])
            top_word[i[0].lower()] = list(set(tmp))
    print(max((len(v), k) for k, v in top_word.items()))

    tagged_sents = []
    tmp = []
    for i in brown_news_tagged:
        if i[1] == '.':
            tmp.append(i)
            tagged_sents.append(tmp)
            tmp=[]
        tmp.append(i)
    five_tags = ['CS','DT','WPS','QL','NIL']
    while (len(five_tags) > 0):
        for s in tagged_sents:
            for (w, t) in s:
                if w == 'that' and t in five_tags:
                    print(s)
                    five_tags.remove(t)



def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise" + str(exNum)]()
    print("")


def main():
     exercise(1)
     exercise(2)
     exercise(3)


if __name__ == "__main__":
    main()