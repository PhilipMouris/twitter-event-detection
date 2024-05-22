import json

tweets = open(r"dataset.txt","r", encoding="utf-8").readlines()
print(len(tweets))

tweets_json = []

for tweet in tweets:
    tweets_json.append({
        "tweet": " ".join(tweet.split()[2:]),
        "label": tweet.split()[1]
    })
print(len(tweets_json))

with open("tweets.json", "w", encoding="utf8") as outfile:
    json.dump(tweets_json, outfile, indent=4, ensure_ascii=False)
