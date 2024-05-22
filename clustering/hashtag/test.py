import json

tweets = []
output_tweets = []

with open("june_tweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)
    print(len(tweets))

# for tweet in tweets:
#     print(tweet["id"])
#     if "مرسي" in tweet["tweet"]:
#         output_tweets.append(tweet["tweet"])
#
# with open("test.json", "w", encoding="utf8") as outfile:
#     json.dump(output_tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
