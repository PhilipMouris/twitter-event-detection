import json
import re

tweets = []

with open("noStopwordsTweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    tokens = tweet["clean_tweet"].split()
    output_tokens = []
    for token in tokens:
        if len(token) >= 3:
            output_tokens.append(token)
    tweet["clean_tweet"] = " ".join(output_tokens)

with open("noStopwordsOrLessThreeTweets.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
