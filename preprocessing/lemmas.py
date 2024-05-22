import json

tweets = []
lemma_tweets = []

with open("noStopwordsOrLessThreeTweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

with open("lemmas.json", encoding="utf8") as json_file:
    lemma_tweets = json.load(json_file)

count = 0
for tweet in tweets:
    print(tweet["id"])
    parallel_tweet = lemma_tweets[count]
    if tweet["id_str"] != parallel_tweet["id"]:
        print("ERRORRR!!!!")
        break
    tweet["clean_tweet"] = parallel_tweet["clean_tweet"]
    count += 1

with open("lemmas_final.json", "w", encoding="utf8") as outfile:
    json.dump(tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
