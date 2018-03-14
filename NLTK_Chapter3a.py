import nltk, re, pprint
from urllib.request import urlopen

from nltk.book import *
from bs4 import BeautifulSoup
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk import word_tokenize


SimpleText = 'One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'
url = "https://www.cs.utexas.edu/~vl/notes/dijkstra.html"

def exercise6():
    print("part b")
    nltk.re_show('[A-Z][a-z]*',SimpleText)
    print("part c")
    nltk.re_show('p[aeiou]{,2}t',SimpleText)
    print("part f")
    nltk.re_show('\w+|[^\w\s]+',SimpleText)


def exercise7():
    print("part a")
    nltk.re_show(r'\b(a|an|the)\b',SimpleText)


def unknown1(raw, words_list):

    token_list1 = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw)
    words_list1 = [w for w in token_list1 if w.islower()]
    unknown_w = []
    for w in words_list1:
        if w not in words_list:
            unknown_w.append(w)
    print(unknown_w)

def unknown2(raw, words_list):
    tokens = nltk.word_tokenize(raw)
    wnl = nltk.WordNetLemmatizer()
    token_list2 = set([wnl.lemmatize(t) for t in tokens] )
    words_list2 = [w for w in token_list2 if w.islower()]
    unknown_w = []
    for w in words_list2:
        if w not in words_list:
            unknown_w.append(w)

    print(unknown_w)

def exercise21():
    html = urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html,"html5lib").get_text()
    words_list = [w for w in nltk.corpus.words.words('en') if w.islower()]


    print("With re.findall:")
    unknown1(raw, words_list)
    print("With nltk.word_tokenize():")
    unknown2(raw, words_list)


def word_to_pig_latin(word):
    """takes a word and converts it to pig latin"""

    # matches on a cluster of consonants
    pattern = re.compile(r'^[^aeiouAEIOU]+')

    if re.findall(r'^qu', word):
        # keeps qu together a la quiet
        pattern = re.compile(r'^qu')
        beginning = re.findall(pattern, word)
        word = pattern.sub('', word)
        word += str(beginning[0]) + 'ay'
        return word

    elif re.findall(r'[^aeiouAEIOU]y[^aeiouAEIOU]', word):
        # if y has a consonant on either side it treats it like a vowel
        pattern = re.compile(r'^[^aeiouAEIOUy]+')
        beginning = re.findall(pattern, word)
        word = pattern.sub('', word)
        word += str(beginning[0]) + 'ay'
        return word

    # stores the beginning match
    elif re.findall(pattern, word):
        beginning = re.findall(pattern, word)

        # pulls out those consonants and gets rid of them
        word = pattern.sub('', word)

        # adds the consonants onto the end of the word
        word += str(beginning[0]) + 'ay'
    return word

def convert_all(text):
	"""converts all words in a given text to pig latin"""
	pig_tokens = ''

	#tokenizes the text
	tokens = word_tokenize(text)

	#regex for non-alphabetical characters
	pattern = re.compile(r'[^a-zA-Z]')

	#converts the words to pig latin and appends them to the sentence.
	for token in tokens:
		if not re.findall(pattern, token):
			word = word_to_pig_latin(token)

			if re.findall(r'[A-Z]', word):
				word = word.lower()
				word = word.capitalize()
			pig_tokens += ' ' + word
		else:
			pig_tokens += token

	pig_text = ''.join(pig_tokens)

	return pig_text

def exercise25():
    print(convert_all(SimpleText))
    print(word_to_pig_latin('quiet'))
    print(word_to_pig_latin('yellow'))
    print(word_to_pig_latin('style'))


def exercise(exNum):
    print("Exercise {}".format(exNum))

    globals()["exercise" + str(exNum)]()
    print("")


def main():
    exercise(6)
    exercise(7)
    exercise(21)
    exercise(25)


if __name__ == "__main__":
    main()