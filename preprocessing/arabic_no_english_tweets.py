import json
import unicodedata
from polyglot.detect import Detector
import polyglot
from nltk.tokenize import TweetTokenizer

tweets = []
tk = TweetTokenizer(strip_handles=True)

with open("arabicTweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    tokens = tk.tokenize(tweet["clean_tweet"])
    output_tokens = []
    for token in tokens:
        try:
            if any(language.name == "Arabic" or language.name == "Persian" or language.name == "Kurdish" or language.name == "Azerbaijani" or language.name == "Sindhi" or language.name == "Balochi" or language.name == "Pashto" or language.name == "Lurish" or language.name == "Urdu" or language.name == "Mandinka" for language in Detector(token).languages):
                output_tokens.append(token)
        except polyglot.detect.base.UnknownLanguage:
            continue
    tweet["clean_tweet"] = " ".join(output_tokens)

with open("arabicNoEnglishTweets.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
