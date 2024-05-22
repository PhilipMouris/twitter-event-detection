import json

clusters = []
output = []

with open("final_cluster_result.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)
    print(len(clusters))

for cluster in clusters:
    usernames = []
    for tweet in cluster["tweets"]:
        usernames.append(tweet["username"])
    usernames = list(dict.fromkeys(usernames))
    for name in usernames:
        if not name in ['youm7', 'alahram', 'shorouk_news', 'cbcegypt', 'almasryalyoum', 'onent', 'tahrirnews', 'alsisiofficial', 'elwatannews']:
            output.append(cluster)
            break

with open("final.json", "w", encoding="utf8") as outfile:
    json.dump(output, outfile, indent=4, ensure_ascii=False)

print(len(output))
