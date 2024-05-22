import json
import pandas
from sklearn import naive_bayes, metrics, linear_model, svm
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from collections import Counter

tweet_texts = []
tweet_labels = []
clusters = []

with open("tweets_preprocessed.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)
    counter = 0
    for tweet in tweets:
        if tweet["label"] == "NEG":
            tweet_texts.append(tweet["tweet"])
            tweet_labels.append(tweet["label"])
        else:
            counter += 1
            if counter < 160000:
                tweet_texts.append(tweet["tweet"])
                tweet_labels.append(tweet["label"])
    print(len(tweet_texts))

with open("../clusters.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)
    # for cluster in raw_clusters:
    #     tweets = []
    #     for tweet in cluster["tweets"]:
    #         if not tweet["username"] in ['youm7', 'alahram', 'shorouk_news', 'cbcegypt', 'almasryalyoum', 'onent', 'tahrirnews', 'elwatannews']:
    #             tweets.append(tweet["clean_tweet"])
    #     clusters.append(" ".join(tweets))

# with open("../summarized_clusters.json", encoding="utf8") as json_file:
#     summarized_clusters = json.load(json_file)
#     counter = 0
#     for cluster in summarized_clusters:
#         clusters[counter]["top_tweet"] = cluster["top_tweet"]
#         counter += 1

train_texts, test_texts, train_labels, test_labels = train_test_split(tweet_texts, tweet_labels, train_size=0.9, test_size=0.1, random_state=31)

trainDF = pandas.DataFrame()
trainDF['text'] = train_texts
trainDF['label'] = train_labels

testDF = pandas.DataFrame()
testDF['text'] = test_texts
testDF['label'] = test_labels

encoder = LabelEncoder()
encoder.fit(trainDF['label'])
print(dict(zip(encoder.classes_, encoder.transform(encoder.classes_))))
encoder.fit(testDF['label'])
print(dict(zip(encoder.classes_, encoder.transform(encoder.classes_))))
encoded_train_labels = encoder.fit_transform(trainDF['label'])
encoded_test_labels = encoder.fit_transform(testDF['label'])

tfidf = TfidfVectorizer(ngram_range=(1,3))
tfidf_train = tfidf.fit_transform(trainDF["text"])
tfidf_test = tfidf.transform(testDF["text"])
# tfidf_clusters = tfidf.transform(clusters)

print("modelling")
# classifier = naive_bayes.MultinomialNB()
# classifier = linear_model.LogisticRegression(max_iter=1000)
classifier = svm.LinearSVC()
classifier.fit(tfidf_train, encoded_train_labels)
predictions = classifier.predict(tfidf_test)
print(metrics.accuracy_score(encoded_test_labels, predictions))
print(metrics.classification_report(encoded_test_labels, predictions))

clusters_predictions = []
for cluster in clusters:
    cluster_predictions = []
    top_tweet_id = cluster["top_tweet"]["id"]
    for tweet in cluster["tweets"]:
        # if tweet["id"] == top_tweet_id:
        # if not tweet["username"] in ['youm7', 'alahram', 'shorouk_news', 'cbcegypt', 'almasryalyoum', 'onent', 'tahrirnews', 'elwatannews']:
            tfidf_tweet = tfidf.transform([tweet["clean_tweet"]])
            prediction = classifier.predict(tfidf_tweet)
            cluster_predictions += prediction.tolist()
    clusters_predictions += Counter(cluster_predictions).most_common(1)

# cluster_predictions = classifier.predict(tfidf_clusters)
# print(cluster_predictions)
print(clusters_predictions)