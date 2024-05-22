import json
from polyglot.detect import Detector
import polyglot
import unicodedata
import re
from pyarabic.araby import strip_tatweel
from pyarabic.araby import strip_tashkeel
from nltk.tokenize import TweetTokenizer

clusters = []

with open("clusters.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

def replace_control(ch):
    if unicodedata.category(ch)[0]!="C":
        return ch
    else:
        return " "

def no_control(tweet):
    tweet["clean_tweet"] = "".join(replace_control(ch) for ch in tweet["tweet"])

def no_english(tweet):
    tk = TweetTokenizer(strip_handles=True)
    tokens = tk.tokenize(tweet["clean_tweet"])
    output_tokens = []
    for token in tokens:
        try:
            if any(language.name == "Arabic" or language.name == "Persian" or language.name == "Kurdish" or language.name == "Azerbaijani" or language.name == "Sindhi" or language.name == "Balochi" or language.name == "Pashto" or language.name == "Lurish" or language.name == "Urdu" or language.name == "Mandinka" for language in Detector(token).languages):
                output_tokens.append(token)
        except polyglot.detect.base.UnknownLanguage:
            continue
    tweet["clean_tweet"] = " ".join(output_tokens)

def replace_char(ch):
    if ch.isalpha():
        return ch
    else:
        return ' '

def no_special_char(tweet):
    tweet["clean_tweet"] = " ".join(("".join(replace_char(ch) for ch in strip_tashkeel(tweet["clean_tweet"]))).split())

def no_repetition_tatweel(article):
    tweet["clean_tweet"] = re.sub(r'(.)\1+', r'\1', strip_tatweel(tweet["clean_tweet"]))

for cluster in clusters:
    for tweet in cluster["tweets"]:
        no_control(tweet)
        no_english(tweet)
        no_special_char(tweet)
        no_repetition_tatweel(tweet)

with open("clusters_preprocessed.json", "w", encoding="utf8") as outfile:
    json.dump(clusters, outfile, indent=4, ensure_ascii=False)
