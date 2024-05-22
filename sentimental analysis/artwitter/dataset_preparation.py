import json

tweets = open(r"dataset.txt","r", encoding="utf-8").readlines()

pos_count = 0
neg_count = 0
tweets_json = []
for tweet in tweets:
    tweet_text = tweet.split(",")[1][:-1]
    tweet_label = tweet.split(",")[0]
    if tweet_label == "1":
        tweet_label = "POS"
        pos_count += 1
    else:
        tweet_label = "NEG"
        neg_count += 1
    tweets_json.append({
        "tweet": tweet_text,
        "label": tweet_label
    })

print("positive:")
print(pos_count)
print("negative:")
print(neg_count)
with open("tweets.json", "w", encoding="utf8") as outfile:
    json.dump(tweets_json, outfile, indent=4, ensure_ascii=False)
