import json

tweets = []
clusters = [0] * 8000
output_clusters = []

with open("june_tweets_labelled.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    clusters[tweet["cluster"]] += 1

cluster_index = 0
for cluster_count in clusters:
    if cluster_count > 2:
        output_clusters.append({
            "cluster": cluster_index,
            "count": cluster_count
        })
    cluster_index += 1

with open("cluster_counts.json", "w", encoding="utf8") as outfile:
    json.dump(output_clusters, outfile, indent=4, ensure_ascii=False)

print("DONE")
