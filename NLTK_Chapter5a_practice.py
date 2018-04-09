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
    # 1.	Train a unigram tagger on all of the sentences from the Brown corpus with the category news just as described in the “Unigram” Subsection of Section 5.1 of the textbook.
    # a)	Evaluate your tagger using “evaluate” function on all of the sentences from the Brown corpus with the category lore.
    # b)	How does this number compare to when this tagger is evaluate on all of the sentences from the Brown corpus with the category news.
    # c)	Provide the output of your tagger on the 200th sentence of the lore category of the Brown Corpus, (note how brown.sents(categories='lore')[199] produces the 200th sentence).
    print('part a')
    brown_tagged_sents = brown.tagged_sents(categories = 'news')
    unigram_tagger_news = nltk.UnigramTagger(brown_tagged_sents)
    news_evaluate = unigram_tagger_news.evaluate(brown_tagged_sents)
    print("news_evaluate: ", news_evaluate)

    brown_tagged_sents_lore = brown.tagged_sents(categories = 'lore')
    lore_evaluate = unigram_tagger_news.evaluate(brown_tagged_sents_lore)
    print("lore_evaluate: " , lore_evaluate)



def exercise2():
    # 2.	Write code to search the Brown Corpus for particular words and phrases according to tags, to answer the questions a-d. Report your findings separately for the following categories of Brown corpus: humor, romance, government.
    # a)	Produce an alphabetically sorted list of the distinct words tagged as JJ. Report the number of distinct words tagged as JJ and the first five words in the sorted list.
    # b)	Identify words that can be plural nouns or third person singular verbs (e.g. deals, flies).  Sort these words alphabetically. Report the first 10 elements of the sorted list.
    # c)	Identify three-word prepositional phrases of the form IN + AT + NN (eg. at the house). Report the 3 most frequent three-word prepositional phrases (break ties alphabetically).
    # d)	What is the ratio of masculine pronouns
    #   himself, his, him , he, he's, he'd, he'll
    # to feminine pronouns
    # herself, her, hers, she, she's, she'd, she'll,
    # where both are used with tag PP?
    # What are the differences that you observe with respect to different categories of Brown corpus.
    print("Part 1")
    tagged_text = brown.tagged_words(categories='humor')
    cfd = nltk.ConditionalFreqDist(tagged_text)
    conditions = cfd.conditions()
    print("conditions: ", conditions)
    JJ_words = [condition for condition in conditions if cfd[condition]['JJ'] != 0]

    JJ_words.sort()
    print("JJ_words: ", JJ_words[:5])



    print("Part 2")
    tagged_text = brown.tagged_words(categories='humor')
    cfd = nltk.ConditionalFreqDist(tagged_text)
    conditions = cfd.conditions()
    print("conditions: ", conditions)
    p_words = [condition for condition in conditions if cfd[condition]['NNS'] and cfd[condition]['VBZ']]

    p_words.sort()
    print("p_words: ", p_words[:10])

    print("Part 3")
    tagged_text = brown.tagged_words(categories='humor')
    three_words = []
    trigrams = list(nltk.trigrams(tagged_text))
    for (w1, t1), (w2, t2), (w3, t3) in trigrams:
        if t1 == 'IN' and t2 == 'AT' and t3 == 'NN':
            three_words.append((w1, w2, w3))
    print(nltk.FreqDist(three_words).most_common(3))


    print("Part 4")
    tagged_text = brown.tagged_words(categories='humor')
    pp_list = []

    for word in tagged_text:
        if word[1].startswith("PP") and not word[1] == "PP$":
            pp_list.append(word[0])
    male_list = ['himself', 'his', 'him', 'he', "he's", "he'd", "he'll"]
    female_list = ['herself', 'her', 'hers', 'she', "she's", "she'd", "she'll"]
    male_count = 0
    female_count = 0
    for i in pp_list:
        if i.lower() in male_list:
            male_count += 1
        if i.lower() in female_list:
            female_count += 1

    ratio = male_count/female_count
    print("ratio: ", ratio)


def exercise3():
    # 3.	Utilizing the complete Brown corpus report the following:
    # a)	Analyze the tagged words to determine the number of distinct words that have exactly 5 possible tags. For example: The word read has 4 possible tags (NP, VB, VBN, VBD) found in the Brown corpus, whereas debt only has one possible tag (NN).
    # b)	Determine which word(s) has the most distinct tags.  Chose one of these word(s) and find sentences demonstrating the use of at least 5 distinct tags from the possible tags for the selected word.
    print("Part 1")
    # count = 0
    # brown_tagges = brown.tagged_words()
    # data  = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_tagges)
    # for word in data.conditions():
    #     if len(data[word]) == 5:
    #         tags = [tag for (tag, _) in data[word].most_common()]
    #         print(word, ' '.join(tags))
    #         count += 1
    # print('count: ', count)



    print("Part 2")
    brown_news_tagged = brown.tagged_words()
    # top_word= {}
    # for i in brown_news_tagged:
    #     if i[0].lower() not in top_word:
    #         top_word[i[0].lower()] = [i[1]]
    #     else:
    #         tmp = top_word[i[0].lower()]
    #         tmp.append(i[1])
    #         top_word[i[0].lower()] = list(set(tmp))
    # print(max((len(v), k) for k,v in top_word.items()))

    tagged_sents = []
    tmp = []
    for i in brown_news_tagged:
        if i[1] == '.':
            tmp.append(i)
            tagged_sents.append(tmp)
            tmp = []
        tmp.append(i)
    five_tags =  ['CS','DT','WPS','QL','NIL']
    while(len(five_tags) > 0):
        for sent in tagged_sents:
            for (w, t) in sent:
                if w == 'that' and t in five_tags:
                    print(sent)
                    five_tags.remove(t)





def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise" + str(exNum)]()
    print("")


def main():
    # exercise(1)
    # exercise(2)
    exercise(3)


if __name__ == "__main__":
    main()

