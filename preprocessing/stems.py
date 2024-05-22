import json
from nltk.stem.arlstem import ARLSTem

tweets = []
stemmer = ARLSTem()

with open("noStopwordsOrLessThreeTweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    tweet["clean_tweet"] = " ".join([stemmer.stem(word) for word in tweet["clean_tweet"].split()])

with open("stems.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
