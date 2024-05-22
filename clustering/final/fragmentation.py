import json

clusters = []

with open("final.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)
    print(len(clusters[0]["tweets"]))
    print(len(clusters[1]["tweets"]))

clusters[0]["fragmentation"] = "6/540 1.11%"
clusters[1]["fragmentation"] = "1/71 1.40%"

with open("final.json", "w", encoding="utf8") as outfile:
    json.dump(clusters, outfile, indent=4, ensure_ascii=False)
