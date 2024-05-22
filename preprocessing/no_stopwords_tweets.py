import json
import re

tweets = []
stopwords_file = open("stopwords.txt", "r", encoding="utf8")
stopwords = stopwords_file.read().splitlines()

with open("noRepetitionOrTatweelTweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    tokens = tweet["clean_tweet"].split()
    output_tokens = []
    for token in tokens:
        if token not in stopwords:
            output_tokens.append(token)
    tweet["clean_tweet"] = " ".join(output_tokens)

with open("noStopwordsTweets.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
