import json

cluster_labels = []
clusters = []

with open("big_cluster_result.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)
    print(len(clusters))

with open("cluster_labels.json", encoding="utf8") as json_file:
    cluster_labels = json.load(json_file)
    cluster_labels = cluster_labels["cluster_labels"]
    print(len(cluster_labels))

count = 0
for cluster in clusters:
    print(cluster["big_cluster"])
    cluster["final_cluster"] = cluster_labels[count]
    count += 1

with open("clusters_labelled.json", "w", encoding="utf8") as outfile:
    json.dump(clusters, outfile, indent=4, ensure_ascii=False)

print("DONE")
