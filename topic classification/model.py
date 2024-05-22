import json
import pandas
from sklearn import naive_bayes, metrics, linear_model, svm
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

articles = []
test_articles = []
clusters = []

with open("combined_train_dataset_lemmatized.json", encoding="utf8") as json_file:
    articles = json.load(json_file)

with open("combined_test_dataset_lemmatized.json", encoding="utf8") as json_file:
    test_articles = json.load(json_file)

with open("clusters.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)
    africa_tweets = []
    for tweet in clusters[0]["tweets"]:
        africa_tweets.append(tweet["clean_tweet"])
    morsi_tweets = []
    for tweet in clusters[1]["tweets"]:
        morsi_tweets.append(tweet["clean_tweet"])
    clusters = [" ".join(africa_tweets), " ".join(morsi_tweets)]

texts = []
labels = []

for article in articles:
    texts.append(article["article"])
    labels.append(article["class"])

trainDF = pandas.DataFrame()
trainDF['text'] = texts
trainDF['label'] = labels

test_texts = []
test_labels = []

for article in test_articles:
    test_texts.append(article["article"])
    test_labels.append(article["class"])

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

tfidf = TfidfVectorizer(ngram_range=(1,2), max_features=5000)
tfidf_train = tfidf.fit_transform(trainDF["text"])
tfidf_test = tfidf.transform(testDF["text"])
tfidf_clusters = tfidf.transform(clusters)

print("modelling")
# classifier = naive_bayes.MultinomialNB()
# classifier = linear_model.LogisticRegression(max_iter=1000)
classifier = svm.LinearSVC()
classifier.fit(tfidf_train, encoded_train_labels)
predictions = classifier.predict(tfidf_test)
print(metrics.accuracy_score(encoded_test_labels, predictions))
print(metrics.classification_report(encoded_test_labels, predictions))
cluster_predictions = classifier.predict(tfidf_clusters)
print(cluster_predictions)
