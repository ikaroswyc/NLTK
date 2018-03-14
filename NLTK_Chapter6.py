from __future__ import division
import nltk, re, pprint
import random
from urllib.request import urlopen
from nltk.corpus import names
from nltk.book import *
from nltk.classify import MaxentClassifier
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import abc
from nltk.classify.util import apply_features
from nltk.corpus import wordnet as wn
from nltk.corpus import movie_reviews

class ConsecutivePosTagger(nltk.TaggerI): # [_consec-pos-tagger]

    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)




# for exercise 2
def gender_features(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

# exercise 7


def extract_features(post):
    features = {}
    for word in nltk.word_tokenize(post.text):
        features['contains({})'.format(word.lower())] = True
    return features
def fpost_list(posts):
    fposts = []
    for p in posts:
        fposts.append((extract_features(p), p.get('class')))
    return fposts

def pos_features(sentence, i, history): # [_consec-pos-tag-features]
    features = {
            "suffix(1)": sentence[i][-1:],
            "suffix(2)": sentence[i][-2:],
            "suffix(3)": sentence[i][-3:],
            "suffix(4)": sentence[i][-4:],
            "suffix(5)": sentence[i][-5:],
        }
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i - 1]
        features["prev-tag"] = history[i - 1]
    return features



# for exercise 9
def noun_features(inst):
    features = {}
    features['noun1'] = inst.noun1
    return features

def exercise2():
    from nltk.corpus import names
    names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in
                                                                     names.words('female.txt')])
    random.shuffle(names)
    test, devtest, training = names[:500],names[500:1000],names[1000:]

    featuresets = [(gender_features(n), gender) for (n, gender) in names]
    train_set, test_set = featuresets[:500], featuresets[500:1500]


    # naviebayes
    classifier1 = nltk.NaiveBayesClassifier.train(train_set)
    print ("naive bayes vs train_set ",nltk.classify.accuracy(classifier1, train_set))
    print("naive bayes vs test_set ",nltk.classify.accuracy(classifier1, test_set))
    print (classifier1.show_most_informative_features(5))

    # decision tree
    classifier2 = nltk.DecisionTreeClassifier.train(train_set)
    print("decision tree vs train_set ", nltk.classify.accuracy(classifier2, train_set))
    print("decision tree vs test_set ", nltk.classify.accuracy(classifier2, test_set))

    # Maxent
    algorithm = nltk.classify.MaxentClassifier.ALGORITHMS[0]
    classifier3 = nltk.MaxentClassifier.train(train_set, algorithm, trace=0,max_iter=5)
    print("maxent vs train_set ", nltk.classify.accuracy(classifier3, train_set))
    print("maxent vs test_set ", nltk.classify.accuracy(classifier3, test_set))

def exercise4():
    from nltk.corpus import movie_reviews
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    # random.shuffle(documents)

    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = list(all_words.keys())[:2000]

    def document_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains({})'.format(word)] = (word in document_words)
        return features

    featuresets = [(document_features(d), c) for (d, c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print (nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(30)


def exercise7():
    # Design at least 5 features and report what these features capture.
    # Report the accuracy of your classifier. Place your classifier code into the report
    tagged_sents = brown.tagged_sents(categories='news')
    size = int(len(tagged_sents) * 0.1)
    train_sents, test_sents = tagged_sents[size:], tagged_sents[:size]
    tagger = ConsecutivePosTagger(train_sents)
    print()
    print (tagger.evaluate(test_sents))

def synsets(words):
    syns = set()
    for w in words:
        syns.update(str(s) for s in nltk.corpus.wordnet.synsets(w))

    return syns


def document_features(document):
    document_words = set(document)
    document_synsets = synsets(document_words)

    for word in document_words:
        document_synsets.update(str(s) for s in nltk.corpus.wordnet.synsets(word))

    features = dict()

    all_words = nltk.FreqDist(w.lower() for w in nltk.corpus.movie_reviews.words())
    word_features = list(all_words.keys())[:2000]
    synset_features = synsets(word_features)

    for synset in synset_features:
        features[synset] = (synset in document_synsets)

    return features


def exercise0():

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

    from nltk.corpus import ppattach

    training_ppattach_corpus = ppattach.attachments('training')
    noun_ppattach_corpus = [inst for inst in training_ppattach_corpus if inst.attachment == 'N']

    features = [(noun_features(inst), inst.prep) for inst in noun_ppattach_corpus]
    cutoff = int(len(features) / 4)
    train_set, test_set = features[:cutoff], features[cutoff:]

    # Naive Bayes Classifier
    classifier1 = nltk.NaiveBayesClassifier.train(train_set)

    # Decision Tree Classifier
    classifier2 = nltk.DecisionTreeClassifier.train(train_set)

    print("Naive Bayes classifier")
    print("Accuracy", nltk.classify.accuracy(classifier1, test_set))
    print("team", classifier1.classify({'noun1': 'team'}), "researchers")
    print("Decision Tree classifier")
    print("Accuracy", nltk.classify.accuracy(classifier2, test_set))
    print("team", classifier2.classify({'noun1': 'team'}), "researchers")

    print("5 features:")
    print (classifier1.show_most_informative_features(5))


def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise"+str(exNum)]()
    print("")


def main():
     # exercise(2)
     exercise(4)
     # exercise(7)
     # exercise(0)
     # exercise(9)


if __name__ == "__main__":
    main()

