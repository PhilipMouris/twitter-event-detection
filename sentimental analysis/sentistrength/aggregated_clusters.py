import json

clusters = []
clusters_text = []

with open("clusters.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

for cluster in clusters:
    text = ""
    for tweet in cluster["tweets"]:
        text += tweet["clean_tweet"] + " "
    clusters_text.append(text)

with open("clusters_preprocessed_text.json", "w", encoding="utf8") as outfile:
    json.dump(clusters_text, outfile, indent=4, ensure_ascii=False)
