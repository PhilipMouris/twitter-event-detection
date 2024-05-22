import json

cluster_labels = []
tweets = []

with open("june_tweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)
    print(len(tweets))

with open("cluster_labels.json", encoding="utf8") as json_file:
    cluster_labels = json.load(json_file)
    cluster_labels = cluster_labels["cluster_labels"]
    print(len(cluster_labels))

count = 0
for tweet in tweets:
    print(tweet["id"])
    tweet["cluster"] = cluster_labels[count]
    count += 1

with open("june_tweets_labelled.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
