import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

tweets = []
tweets_text = []
hashtags= []
transformed_hashtags = []

with open("june_tweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    tweets_text.append(tweet["clean_tweet"] + " " + " ".join(tweet["hashtags"]))
    hashtags += tweet["hashtags"]

def transform_hashtag(hashtag):
    return "".join(ch for ch in hashtag if ch != '#')

for hashtag in hashtags:
    transformed_hashtags.append(transform_hashtag(hashtag))

transformed_hashtags = list(dict.fromkeys(transformed_hashtags))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tweets_text)

for hashtag in transformed_hashtags:
    position = vectorizer.vocabulary_[hashtag]
    X[:, position] *= 2.0

dist = 1 - cosine_similarity(X)

joblib.dump(X, 'tfidf.pkl')
joblib.dump(dist, 'cosine.pkl')

print("DONE")
