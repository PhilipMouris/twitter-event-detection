import json
from tashaphyne.stemming import ArabicLightStemmer

tweets = []
stemmer = ArabicLightStemmer()

with open("noStopwordsOrLessThreeTweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    tweet["clean_tweet"] = " ".join([stemmer.light_stem(word) for word in tweet["clean_tweet"].split()])

with open("stems2.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
