import json
from pyarabic.araby import strip_tashkeel

def replace_char(ch):
    if ch.isalpha():
        return ch
    else:
        return ' '

tweets = []

with open("arabicNoEnglishLongTweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    tweet["clean_tweet"] = " ".join(("".join(replace_char(ch) for ch in strip_tashkeel(tweet["clean_tweet"]))).split())

with open("noSpecialCharTweets.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
