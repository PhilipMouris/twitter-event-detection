import json

clusters = []

with open("clusters0.json", encoding="utf8") as json_file:
    new_clusters = json.load(json_file)
    clusters += new_clusters

with open("clusters1.json", encoding="utf8") as json_file:
    new_clusters = json.load(json_file)
    clusters += new_clusters

with open("clusters.json", "w", encoding="utf8") as outfile:
    json.dump(clusters, outfile, indent=4, ensure_ascii=False)
