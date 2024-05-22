import json
from collections import Counter

clusters = []
africa_hashtags = []
morsi_hashtags = []

with open("final.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

for tweet in clusters[0]["tweets"]:
    africa_hashtags += tweet["hashtags"]

for tweet in clusters[1]["tweets"]:
    morsi_hashtags += tweet["hashtags"]

africa_hashtags = Counter(africa_hashtags).most_common(3)
morsi_hashtags = Counter(morsi_hashtags).most_common(3)

clusters[0]["top_hashtags"] = africa_hashtags
clusters[1]["top_hashtags"] = morsi_hashtags

with open("final.json", "w", encoding="utf8") as outfile:
    json.dump(clusters, outfile, indent=4, ensure_ascii=False)
