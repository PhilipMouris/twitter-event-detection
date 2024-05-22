import json
from polyglot.detect import Detector
import polyglot
from nltk import word_tokenize
import re
from pyarabic.araby import strip_tatweel
from pyarabic.araby import strip_tashkeel
import unicodedata

tweets = []
train_tweets = []
test_tweets = []
stopwords_file = open("stopwords.txt", "r", encoding="utf8")
stopwords = stopwords_file.read().splitlines()

with open("tweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

def replace_char(ch):
    if ch.isalpha():
        return ch
    else:
        return ' '

def no_special_char(tweet):
    tweet["tweet"] = " ".join(("".join(replace_char(ch) for ch in strip_tashkeel(tweet["tweet"]))).split())

def no_repetition_tatweel(tweet):
    tweet["tweet"] = re.sub(r'(.)\1+', r'\1', strip_tatweel(tweet["tweet"]))

def no_stopwords(tweet):
    tokens = tweet["tweet"].split()
    output_tokens = []
    for token in tokens:
        if token not in stopwords:
            output_tokens.append(token)
    tweet["tweet"] = " ".join(output_tokens)

def no_less_three(tweet):
    tokens = tweet["tweet"].split()
    output_tokens = []
    for token in tokens:
        if len(token) >= 3:
            output_tokens.append(token)
    tweet["tweet"] = " ".join(output_tokens)

def replace_control(ch):
    if unicodedata.category(ch)[0]!="C":
        return ch
    else:
        return " "

def no_control(tweet):
    tweet["tweet"] = "".join(replace_control(ch) for ch in tweet["tweet"])

counter = 1
for tweet in tweets:
    print(counter)
    counter += 1
    no_control(tweet)
    no_special_char(tweet)
    no_repetition_tatweel(tweet)
    no_stopwords(tweet)
    no_less_three(tweet)

with open("tweets_preprocessed.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)
