import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import joblib
import operator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from ar_wordcloud import ArabicWordCloud
import arabic_reshaper
from bidi.algorithm import get_display

clusters = []
tweets_before_lem = []

with open("final.json", encoding="utf8") as json_file:
    clusters = json.load(json_file)

with open("tweets_before_lem.json", encoding="utf8") as json_file:
    tweets_before_lem = json.load(json_file)

africa_tweets = clusters[0]["tweets"]
morsi_tweets = clusters[1]["tweets"]
africa_tweets_text = []
morsi_tweets_text = []

def find_tweet_before_lem(id):
    for tweet in tweets_before_lem:
        if tweet["id"] == id:
            return tweet["clean_tweet"]

def generate_word_cloud(keyphrases):
    text = {}
    if "الام" in keyphrases:
        keyphrases["الامم"] = keyphrases.pop("الأم")
        keyphrases["الامم"] = keyphrases.pop("الام")
    for key in keyphrases:
        arabic_key = arabic_reshaper.reshape(key)
        arabic_key = get_display(arabic_key)
        text[arabic_key] = keyphrases[key]
    # text = arabic_reshaper.reshape(" ".join(keyphrases))
    # text = get_display(text)
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10,
                font_path="arial").generate_from_frequencies(text)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)

    plt.show()

for tweet in africa_tweets:
    tweet["clean_tweet"] = find_tweet_before_lem(tweet["id"])

for tweet in morsi_tweets:
    tweet["clean_tweet"] = find_tweet_before_lem(tweet["id"])

for tweet in africa_tweets:
    tokens = tweet["clean_tweet"].split(" ")
    bigrams = [tokens[i]+'_'+tokens[i+1] for i in range(len(tokens)-1)]
    trigrams = [tokens[i]+'_'+tokens[i+1]+'_'+tokens[i+2] for i in range(len(tokens)-2)]
    africa_tweets_text.append(" ".join(trigrams))

for tweet in morsi_tweets:
    tokens = tweet["clean_tweet"].split(" ")
    bigrams = [tokens[i]+'_'+tokens[i+1] for i in range(len(tokens)-1)]
    trigrams = [tokens[i]+'_'+tokens[i+1]+'_'+tokens[i+2] for i in range(len(tokens)-2)]
    morsi_tweets_text.append(" ".join(trigrams))

def get_top_keyphrases(tweets_text):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(tweets_text)
    model = LatentDirichletAllocation(n_components=1, random_state=0)
    model.fit(X)
    words = vectorizer.get_feature_names()
    weights = model.components_[0]
    result = {}
    for index, word in enumerate(words):
        result[word] = weights[index]
    result = dict(sorted(result.items(), key=operator.itemgetter(1),reverse=True))
    keyphrases = list(result.keys())
    for index, keyphrase in enumerate(keyphrases):
        keyphrases[index] = " ".join(keyphrase.split("_"))
    # generate_word_cloud(result)
    return [keyphrases[0], keyphrases[1], keyphrases[2]]

clusters[0]["top_phrases_trigram"] = get_top_keyphrases(africa_tweets_text)
clusters[1]["top_phrases_trigram"] = get_top_keyphrases(morsi_tweets_text)

with open("final.json", "w", encoding="utf8") as outfile:
    json.dump(clusters, outfile, indent=4, ensure_ascii=False)

print("DONE")
