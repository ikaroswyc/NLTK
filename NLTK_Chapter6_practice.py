from __future__ import division
import nltk, re, pprint,random

from urllib.request import urlopen
from nltk.corpus import names
from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import abc

# 1.	exercise 2.  Design at least 5 features and report what these features capture. Additionally, use three classifiers, namely, nltk.NaiveBayesClassifier, nltk.DecisionTreeClassifier,  nltk.MaxentClassifier. Compare the performance of the three classifiers by analyzing the accuracy. Report the accuracy of each classifier built using all of the features that you designed.
#
# ☼ Using any of the three classifiers described in this chapter, and any features you can think of, build the best name gender classifier you can. Begin by splitting the Names Corpus into three subsets: 500 words for the test set, 500 words for the dev-test set, and the remaining 6900 words for the training set. Then, starting with the example name gender classifier, make incremental improvements. Use the dev-test set to check your progress. Once you are satisfied with your classifier, check its final performance on the test set. How does the performance on the test set compare to the performance on the dev-test set? Is this what you'd expect?

def gender_features(word):
    features = {}
    features["firstletter"]  = word[0].lower()
    features["lastletter"] = word[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = word.lower().count(letter)
        features["has({})".format(letter)] = (letter in word.lower())
    return features

def exercise2():
    from nltk.corpus import names
    names = ([(name,'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(names)
    featuresets = [(gender_features(n),gender) for n,gender in names]
    train_set,test_set = featuresets[:500], featuresets[500:1500]

    #naivebayes
    classifier1 = nltk.NaiveBayesClassifier.train(train_set)
    print("navie vs train", nltk.classify.accuracy(classifier1, train_set))
    print("navie vs test", nltk.classify.accuracy(classifier1, test_set))
    print(classifier1.show_most_informative_features(5))

    #decisiontree
    classifier2 = nltk.DecisionTreeClassifier.train(train_set)
    print("decision vs train", nltk.classify.accuracy(classifier2,train_set))
    print("decision vs test", nltk.classify.accuracy(classifier2,test_set))

    #maxent
    algorithm = nltk.classify.MaxentClassifier.ALGORITHMS[0]
    classifier3 = nltk.MaxentClassifier.train(train_set,algorithm)
    print("maxent vs train", nltk.classify.accuracy(classifier3,train_set))
    print("maxent vs test", nltk.classify.accuracy(classifier3,test_set))



# 2.	exercise 4. To report, pick any 5 features out of the computed 30 and describe their relevance.
# ☼Using the movie review document classifier discussed in this chapter, generate a list of the 30 features that the classifier finds to be most informative. Can you explain why these particular features are informative? Do you find any of them surprising?
def exercise4():
    from nltk.corpus import movie_reviews
    documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = list(all_words)[:2000]
    def document_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains({})', format(word)] = (word in document_words)
        return features
    featuresets=[(document_features(d),c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(30)

def exercise7():
    print('not implemented')

# 4.	exercise 0 (0 is a dummy number in this case). Word features can be very useful for performing document classification, since the words that appear in a document give a strong indication about what its semantic content is. However, many words occur very infrequently, and some of the most informative words in a document may never have occurred in our training data. One solution is to make use of a lexicon, which describes how different words relate to one another. Using WordNet lexicon, augment the movie review document classifier presented in Chapter 6 to use the following two features on the intersection of words appearing in a document to classify and words appearing in “word_features”:
# a)	Make a binary feature which reports “KNOWN” if the word is found in WordNet (i.e. wn.synsets is non-empty) and “UNK” if it is not found.
# b)	Make a lemma name feature. Select the first synset from wn.synsets and choose the first lemma name from synset.lemma_names as the appropriate lemma. Report “UNK” if it is not found.
# Report the accuracy of your classifier: use nltk.NaiveBayesClassifier, your test set should contain the first 100 instances in documents  defined as follows:
# 	from nltk.corpus import movie_reviews
# 		documents = [(list(movie_reviews.words(fileid)), category)
# 		     for category in movie_reviews.categories()
# 		     for fileid in movie_reviews.fileids(category)]
# The remaining instances in documents should be part of your training set.
# How does this accuracy compare to the accuracy of the classifier trained on the original feature set from the book? (Note that accuracy may not improve.) Why do you think you observe the behavior you observe?
def exercise0():
    from nltk.corpus import movie_reviews
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    def feature1(document):
        document_words = set(document)
        features = {}
        for word in document_words:
            if len(wn.synsets(word)) != 0:
                features["{}".format(word)] = "<KNOWN>"
            else:
                features["{}".format(word)] = "<UNK>"
        return features
    def feature2(document):
        document_words = set(document)
        features = {}
        for word in document_words:
            synsets = wn.synsets(word)
            if len(synsets) != 0:
                lemma = synsets[0].lemma_names()[0]
                features["{lemmaNameIs}"] = lemma
            else:
                features["{}".format(word)] = "<UNK>"
        return features
    feature_dict = {"feature1": feature1, "feature2": feature2}
    feature_list = sorted(feature_dict.keys())

    for key in feature_list:
        featuresets = [(feature_dict.get(key)(d), c) for (d, c) in documents]
        train_set, test_set = featuresets[100:], featuresets[:100]
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        print("{} has accuracy {}".format(key, nltk.classify.accuracy(classifier, test_set)))

def exercise9():
    print('Extra Credit')
    print('not implemented')


def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise"+str(exNum)]()
    print("")


def main():
    # exercise(2)
    # exercise(4)
    # exercise(7)
    exercise(0)
    exercise(9)


if __name__ == "__main__":
    main()

