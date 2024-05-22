import json

unbalanced_test = open(r"4class-unbalanced-test.txt","r", encoding="utf-8").readlines()
unbalanced_validation = open(r"4class-unbalanced-validation.txt","r", encoding="utf-8").readlines()
unbalanced_train = open(r"4class-unbalanced-train.txt","r", encoding="utf-8").readlines()
tweets = open(r"Tweets.txt","r", encoding="utf-8").readlines()

tweets_json = []
for tweet in tweets:
    tweet_text = tweet.split("\t")[0]
    tweet_label = tweet.split("\t")[1][:-1]
    tweets_json.append({
        "tweet": tweet_text,
        "label": tweet_label
    })

test_tweets_json = []
for index in unbalanced_test:
    test_tweets_json.append(tweets_json[int(index)])

train_tweets_json = []
for index in unbalanced_train:
    train_tweets_json.append(tweets_json[int(index)])
for index in unbalanced_validation:
    train_tweets_json.append(tweets_json[int(index)])

with open("tweets.json", "w", encoding="utf8") as outfile:
    json.dump(tweets_json, outfile, indent=4, ensure_ascii=False)

with open("train_tweets.json", "w", encoding="utf8") as outfile:
    json.dump(train_tweets_json, outfile, indent=4, ensure_ascii=False)

with open("test_tweets.json", "w", encoding="utf8") as outfile:
    json.dump(test_tweets_json, outfile, indent=4, ensure_ascii=False)
