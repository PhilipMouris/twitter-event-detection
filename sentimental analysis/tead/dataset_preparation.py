import json

pos_tweets = open(r"data_final_positive_clean.txt","r", encoding="utf-8").readlines()
neg_tweets = open(r"data_final_negative_clean.txt","r", encoding="utf-8").readlines()

pos_tweets_json = []

for tweet in pos_tweets:
    pos_tweets_json.append({
        "tweet": tweet[:-1],
        "label": "POS"
    })

neg_tweets_json = []

for tweet in neg_tweets:
    neg_tweets_json.append({
        "tweet": tweet[:-1],
        "label": "NEG"
    })

with open("dataset.json", "w", encoding="utf8") as outfile:
    json.dump(pos_tweets_json + neg_tweets_json, outfile, indent=4, ensure_ascii=False)
