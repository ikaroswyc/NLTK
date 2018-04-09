from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen
import operator
from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import abc

SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'


def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag,word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

def exercise1():
    # 1.	Write programs to process the Brown Corpus and find answers to the following questions:
    # a)	Which nouns are more common in their plural form, rather than their singular form (Use the parts of speech tags in the corpus to identify plural versus singular nouns and use nltk.WordNetLemmatizer() to get the singular form of a noun from its plural form). List the five most frequent nouns that feature this property.
    # print("Part a")
    #
    # tagdict = findtags('NNS', nltk.corpus.brown.tagged_words())
    # total_list = []
    # for tag in sorted(tagdict):
    #     total_list.append(tagdict[tag])
    # print("total_list: ", total_list)
    # total_list_w = list(nltk.chain.from_iterable(total_list))
    # print("total_list-w: ", total_list_w)
    # # sort_total_list_w = sorted(total_list_w, key = lambda x:x[1],reverse = True)
    # sort_total_list_w = sorted(total_list_w, key= operator.itemgetter(1), reverse = True)
    # print("sort_total_list_w: ", sort_total_list_w)
    #
    # lem = nltk.WordNetLemmatizer()
    # words= []
    # first_element = [w for (w,_) in sort_total_list_w]
    # cf = nltk.FreqDist(brown.words())
    # for i in first_element:
    #     singular = lem.lemmatize(i)
    #     freq_sing = cf[singular]
    #     freq_plu = cf[i]
    #     if freq_plu > freq_sing:
    #         words.append(i)
    # print("words: ", words[:10])
    #
    # print("Part b")
    # # b)	List the 5 most frequent tags in order of decreasing frequency. What do the tags represent?
    # tags = nltk.bigrams(brown.tagged_words())
    # preceders = nltk.FreqDist([a[1] for (a,b) in tags]).most_common(5)
    # print("preceders: ", preceders)



    print("Part c")
    # c)	 Which three tags precede nouns tagged with the 'NN' tag most commonly? What do these three tags represent? Report your findings separately for the following categories of Brown corpus: humor, romance, government.
    categories = ['government']
    for cate in categories:
        category_tags = brown.tagged_words(categories = cate)
        print("category_tags: ", category_tags)
        ab = nltk.FreqDist([a[1] for (a , b) in nltk.bigrams(category_tags) if b[1] == 'NN']).most_common()
        first_element = [x for (x, _) in list(ab)]
        res = ','.join(first_element[:3])
        print("res: ", res)
    #     tagList = [a[0][1] for (a,b) in nltk.bigrams(category_tags) if a[1][0] == 'NN']
    # fd = nltk.FreqDist(tagList).most_common()
    # first_element = [x for (x, _) in list(fd)]
    # print(first_element[:3])


def exercise2():
    # 2.	In the “Combining Taggers” Subsection of Section 5.5 of the textbook, an example of a backoff tagger is provided. Extend that example by defining a TrigramTagger called t3 which backs off to t2. Train this tagger on all of the sentences from the Brown corpus with the category news. Then
    # a)	evaluate your tagger using “evaluate” function on all of the sentences from the Brown corpus with the category lore. Report the number. How does this number compare to when this tagger is evaluated on all of the sentences from the Brown corpus with the category news.

    brown_tagged_sents = brown.tagged_sents(categories='news')
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(brown_tagged_sents, backoff=t0)
    t2 = nltk.BigramTagger(brown_tagged_sents,backoff=t1)
    t3 = nltk.TrigramTagger(brown_tagged_sents,backoff=t2)
    news_tagged = t3.evaluate(brown_tagged_sents)
    print(news_tagged)
    print("Part a")
    lore_tagged_sents = brown.tagged_sents(categories = 'lore')
    lore_tagged = t3.evaluate(lore_tagged_sents)
    print("lore evaluate: ", lore_tagged)
    # b)	Provide the output of your tagger on the 200th sentence of the lore category of the Brown Corpus (note how brown.sents(categories='lore')[199] produces the 200th sentence).  Would you tag this sentence in the same manner?
    print("Part b")
    print(t3.tag(brown.sents(categories='lore')[199]))

# 3.	Compare the given TrigramTagger from the previous question with a TrigramTagger where no backoff is provided. Train this tagger on all of the sentences from the Brown corpus with the category news. Then evaluate your tagger using “evaluate” function on all of the sentences from the Brown corpus with the category lore. Report the numbers. Which tagger performs better? Why?

def exercise3():
    news_tagged_sents = brown.tagged_sents(categories='news')


    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(news_tagged_sents,backoff=t0)
    t2 = nltk.BigramTagger(news_tagged_sents, backoff=t1)
    t3 = nltk.TrigramTagger(news_tagged_sents,backoff=t2)

    lore_tagged_sents = brown.tagged_sents(categories='lore')
    lore_evaluation = t3.evaluate(lore_tagged_sents)
    print("lore_evaluation: ", lore_evaluation)
    t4 = nltk.TrigramTagger(news_tagged_sents)
    lore_without = t4.evaluate(lore_tagged_sents)
    print("lore_without: ", lore_without)


# 4.	The majority of WordNet's senses are marked by four POS categories: noun, verb, adjective, and adverb. Determine the percentage of words from the WordNet corpus that have senses in more than one of these categories. For example, type has senses which connect to both “noun” and “verb” POS (positive case), whereas typewriter has only senses which connect to “noun” POS (negative case).

def exercise4():
    wn_words = wn.all_synsets()

    lemma_str = []
    for i in wn_words:
        for lemma in i.lemma_names():
            lemma_str.append(lemma)
    lemma_str_set = list(set(lemma_str))
    print("lemma_str: ", lemma_str_set)
    total_count = 0
    for i in lemma_str_set:
        count = 0
        if len(wn.synsets(i, pos = 'a')) > 0:
            count += 1
        if len(wn.synsets(i, pos = 'v')) > 0:
            count += 1
        if len(wn.synsets(i, pos = 'n')) > 0:
            count += 1
        if len(wn.synsets(i, pos = 'r')) > 0:
            count += 1
        if count > 1:
            total_count += 1
    res = total_count / len(lemma_str_set)
    print("res: ", res)




def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise"+str(exNum)]()
    print("")


def main():
    # exercise(1)
    # exercise(2)
    # exercise(3)
    exercise(4)


if __name__ == "__main__":
    main()

