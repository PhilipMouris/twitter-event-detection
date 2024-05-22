import json

clusters = []
final_clusters = []

with open("clusters_labelled.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

with open("final_cluster_counts.json", encoding="utf8") as json_file:
    final_clusters = json.load(json_file)

for final_cluster in final_clusters:
    print(final_cluster["final_cluster"])
    final_cluster["tweets"] = []
    for cluster in clusters:
        if cluster["final_cluster"] == final_cluster["final_cluster"]:
            final_cluster["tweets"] += cluster["tweets"]

with open("final_cluster_result.json", "w", encoding="utf8") as outfile:
    json.dump(final_clusters, outfile, indent=4, ensure_ascii=False)

print("DONE")
