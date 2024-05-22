import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from yellowbrick.text import TSNEVisualizer

tsne = TSNEVisualizer(alpha=0.2)
tweets = []
tweets_text = []

with open("june_tweets.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    tweets_text.append(tweet["clean_tweet"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tweets_text)
tsne.fit(X)
tsne.show()
dist = 1 - cosine_similarity(X)

joblib.dump(X, 'tfidf.pkl')
joblib.dump(dist, 'cosine.pkl')

print("DONE")
