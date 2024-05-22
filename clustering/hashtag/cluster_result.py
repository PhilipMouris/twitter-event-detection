import json

tweets = []
clusters = []

with open("june_tweets_labelled.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

with open("cluster_counts.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

for cluster in clusters:
    print(cluster["cluster"])
    cluster["tweets"] = []
    for tweet in tweets:
        if tweet["cluster"] == cluster["cluster"]:
            cluster["tweets"].append(tweet["tweet"])

with open("cluster_result.json", "w", encoding="utf8") as outfile:
    json.dump(clusters, outfile, indent=4, ensure_ascii=False)

print("DONE")
