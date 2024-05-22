import json

clusters = []
big_clusters = []

with open("clusters_labelled.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

with open("big_cluster_counts.json", encoding="utf8") as json_file:
    big_clusters = json.load(json_file)

for big_cluster in big_clusters:
    print(big_cluster["big_cluster"])
    big_cluster["tweets"] = []
    for cluster in clusters:
        if cluster["big_cluster"] == big_cluster["big_cluster"]:
            big_cluster["tweets"] += cluster["tweets"]

with open("big_cluster_result.json", "w", encoding="utf8") as outfile:
    json.dump(big_clusters, outfile, indent=4, ensure_ascii=False)

print("DONE")
