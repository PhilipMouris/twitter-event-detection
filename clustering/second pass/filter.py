import json

clusters = []
big_clusters = [0] * 9
output_clusters = []

with open("clusters_labelled.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

for cluster in clusters:
    print(cluster["cluster"])
    big_clusters[cluster["big_cluster"]] += 1

cluster_index = 0
for cluster_count in big_clusters:
    if cluster_count > 0:
        output_clusters.append({
            "big_cluster": cluster_index,
            "count": cluster_count
        })
    cluster_index += 1

with open("big_cluster_counts.json", "w", encoding="utf8") as outfile:
    json.dump(output_clusters, outfile, indent=4, ensure_ascii=False)

print("DONE")
