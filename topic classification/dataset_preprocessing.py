import json
from polyglot.detect import Detector
import polyglot
from nltk import word_tokenize
import re
from pyarabic.araby import strip_tatweel
from pyarabic.araby import strip_tashkeel
import unicodedata

articles = []
stopwords_file = open("stopwords.txt", "r", encoding="utf8")
stopwords = stopwords_file.read().splitlines()

with open("combined_train_dataset.json", encoding="utf8") as json_file:
    articles = json.load(json_file)

def no_english(article):
    tokens = word_tokenize(article["article"])
    output_tokens = []
    for token in tokens:
        if token not in ["Title", "Body"]:
            output_tokens.append(token)
    article["article"] = " ".join(output_tokens)

def replace_char(ch):
    if ch.isalpha():
        return ch
    else:
        return ' '

def no_special_char(article):
    article["article"] = " ".join(("".join(replace_char(ch) for ch in strip_tashkeel(article["article"]))).split())

def no_repetition_tatweel(article):
    article["article"] = re.sub(r'(.)\1+', r'\1', strip_tatweel(article["article"]))

def no_stopwords(article):
    tokens = article["article"].split()
    output_tokens = []
    for token in tokens:
        if token not in stopwords:
            output_tokens.append(token)
    article["article"] = " ".join(output_tokens)

def no_less_three(article):
    tokens = article["article"].split()
    output_tokens = []
    for token in tokens:
        if len(token) >= 3:
            output_tokens.append(token)
    article["article"] = " ".join(output_tokens)

def replace_control(ch):
    if unicodedata.category(ch)[0]!="C":
        return ch
    else:
        return " "

def no_control(article):
    article["article"] = "".join(replace_control(ch) for ch in article["article"])

counter = 1
for article in articles:
    print(counter)
    counter += 1
    no_control(article)
    no_english(article)
    no_special_char(article)
    no_repetition_tatweel(article)
    no_stopwords(article)
    no_less_three(article)

with open("combined_train_dataset_preprocessed.json", "w", encoding="utf8") as outfile:
    json.dump(articles, outfile, indent=4, ensure_ascii=False)
