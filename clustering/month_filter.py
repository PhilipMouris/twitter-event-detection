import json
import datetime

tweets = []
output_tweets = []

def has_duplicates(target):
    for tweet in output_tweets:
        if tweet["clean_tweet"] == target["clean_tweet"]:
            return True
    return False

with open("../preprocessing/lemmas_final.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    if datetime.date.fromisoformat(tweet["datestamp"]) > datetime.date.fromisoformat("2019-06-16") and datetime.date.fromisoformat(tweet["datestamp"]) < datetime.date.fromisoformat("2019-06-22") and not has_duplicates(tweet):
        output_tweets.append(tweet)

with open("june_tweets.json", "w", encoding="utf8") as outfile:
    json.dump(output_tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
