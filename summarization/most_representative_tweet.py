import json

clusters = []

with open("final.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

africa = clusters[0]["tweets"][0]
africa_counts = []
for tweet in clusters[0]["tweets"]:
    if int(tweet["retweets_count"]) > int(africa["retweets_count"]):
        africa = tweet
    africa_counts.append(int(tweet["retweets_count"]))
print(max(africa_counts))

morsi = clusters[1]["tweets"][0]
morsi_counts = []
for tweet in clusters[1]["tweets"]:
    if int(tweet["retweets_count"]) > int(morsi["retweets_count"]):
        morsi = tweet
    morsi_counts.append(int(tweet["retweets_count"]))
print(max(morsi_counts))

clusters[0]["top_tweet"] = africa
clusters[1]["top_tweet"] = morsi

with open("final.json", "w", encoding="utf8") as outfile:
    json.dump(clusters, outfile, indent=4, ensure_ascii=False)
