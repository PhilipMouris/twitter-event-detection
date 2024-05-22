import json
import unicodedata
from polyglot.detect import Detector
import polyglot
import demoji
demoji.download_codes()

tweets = []
output_tweets = []

def replace_char(ch):
    if unicodedata.category(ch)[0]!="C":
        return ch
    else:
        return " "

with open("../final datasets/twintDataset.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    tweet["clean_tweet"] = demoji.replace("".join(replace_char(ch) for ch in tweet["tweet"]), " ")
    try:
        if any(language.name == "Arabic" or language.name == "Persian" or language.name == "Kurdish" or language.name == "Azerbaijani" or language.name == "Sindhi" or language.name == "Balochi" or language.name == "Pashto" or language.name == "Lurish" or language.name == "Urdu" or language.name == "Mandinka" for language in Detector(tweet["clean_tweet"]).languages):
            output_tweets.append(tweet)
    except polyglot.detect.base.UnknownLanguage:
        continue

with open("arabicTweets.json", "w", encoding="utf8") as outfile:
    json.dump(output_tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
