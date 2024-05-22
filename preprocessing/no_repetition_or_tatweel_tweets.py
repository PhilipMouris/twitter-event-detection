import json
import re
from pyarabic.araby import strip_tatweel

tweets = []

with open("noSpecialCharTweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    tweet["clean_tweet"] = re.sub(r'(.)\1+', r'\1', strip_tatweel(tweet["clean_tweet"]))

with open("noRepetitionOrTatweelTweets.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
