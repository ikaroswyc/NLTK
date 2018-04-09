from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen

from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import abc
from nltk.corpus import conll2000


class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

def exercise1():
    print('not implemented')

# 2.	Write tag patterns to match noun phrases containing plural head nouns, e.g. "many/JJ researchers/NNS", "two/CD weeks/NNS", "both/DT new/JJ positions/NNS". Extend the “grammar” defined in Example 3 (Example 2.2 named code_chunkex in the chapter 7).
# 	by your regular expressions. Redefine the “cp” object from this example to use your new 	grammar. Use this object to parse sentenceSample defined as follows
#
# sentenceSample = [("Many", "JJ"), ("little", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("cats", "NNS")]
#
# 	Report your outcome.
def exercise2():
    sentenceSample = [("Many", "JJ"), ("little", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"),
                      ("cats", "NNS")]
    grammar = r"""
                 NP: {<DT>?<JJ>*<NN>}
                     {<VBD>?<IN>?<JJ>*<NNS>}
                    """

    print('sentence sample:')
    cp = nltk.RegexpParser(grammar)
    result2 = cp.parse(sentenceSample)
    print(result2)
    result2.draw()


# 3.	Carry out the following evaluation tasks for the chunker you have developed in question 2.
# a)	Evaluate your chunker on first 100 sentences from a chunked corpus nltk.corpus.conll2000, and report the precision, recall and F-measure.
# b)	Compare the performance of your chunker to the baseline chunker discussed in the evaluation section of 3 (the very first chunker that does nothing).
# c)	Extend the “grammar” of your chunker by at least one more regular expression. Give rationally behind your extension. See whether this extension allows you to boost the performance of your chunker. Evaluate your new chunker on 100 sentences from a chunked corpus nltk.corpus.conll2000, and report the precision, recall and F-measure.
def exercise3():
    print("part a")
    test_sents = conll2000.chunked_sents('train.txt')[:99]
    grammar = r"""
                 NP: {<DT>?<JJ>*<NN>}
                     {<VBD>?<IN>?<JJ>*<NNS>}
                    """
    cp = nltk.RegexpParser(grammar)
    print(cp.evaluate(test_sents))
    print("part b")
    test_sents = "Many little dogs barked at cats"
    cp = nltk.RegexpParser("")
    test_sents = conll2000.chunked_sents('test.txt', chunk_types = ['NP'])
    print("Baseline with no chunks : ", cp.evaluate(test_sents))

    grammar = r"NP: {<[CDJNP].*>+}"
    cp = nltk.RegexpParser(grammar)
    print("IOB tag evaluation: ", cp.evaluate(test_sents))

    print("part c")
    test_sents = conll2000.chunked_sents('train.txt')[:99]
    grammar = r"""
                 NP: {<DT>?<JJ>*<NN>}
                     {<VBD>?<IN>?<JJ>*<NNS>}
                     {<[CDJNP].*>+}
                    """
    cp = nltk.RegexpParser(grammar)
    print(cp.evaluate(test_sents))


def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise"+str(exNum)]()
    print("")


def main():
    # exercise(1)
    # exercise(2)
    exercise(3)


if __name__ == "__main__":
    main()

