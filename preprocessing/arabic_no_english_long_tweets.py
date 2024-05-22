import json
from nltk.tokenize import TweetTokenizer

tweets = []
output_tweets = []
tk = TweetTokenizer(strip_handles=True)

with open("arabicNoEnglishTweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    print(tweet["id"])
    tokens = tk.tokenize(tweet["clean_tweet"])
    if len(tokens) >= 3 or len(tweet["hashtags"]) > 0:
        output_tweets.append(tweet)

with open("arabicNoEnglishLongTweets.json", "w", encoding="utf8") as outfile:
    json.dump(output_tweets, outfile, indent=4, ensure_ascii=False)

print("DONE")
