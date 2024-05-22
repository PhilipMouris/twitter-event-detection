import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

clusters = []
clusters_tweets = []
hashtags = []
transformed_hashtags = []

with open("drive/My Drive/first_cluster_result.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

for cluster in clusters:
    clean_tweets = []
    tweet_hashtags = []
    for tweet in cluster["tweets"]:
        clean_tweets.append(tweet["clean_tweet"])
        tweet_hashtags += tweet["hashtags"]
    hashtags += tweet_hashtags
    clusters_tweets.append(" ".join(clean_tweets) + " " + " ".join(tweet_hashtags))

print(len(clusters))
print(len(clusters_tweets))
print(clusters_tweets[0])

def transform_hashtag(hashtag):
    return "".join(ch for ch in hashtag if ch != '#')

for hashtag in hashtags:
    transformed_hashtags.append(transform_hashtag(hashtag))

transformed_hashtags = list(dict.fromkeys(transformed_hashtags))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(clusters_tweets)

for hashtag in transformed_hashtags:
    position = vectorizer.vocabulary_[hashtag]
    X[:, position] *= 2.0

dist = 1 - cosine_similarity(X)

joblib.dump(X, 'tfidf.pkl')
joblib.dump(dist, 'cosine.pkl')

print("DONE")
