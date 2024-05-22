import unicodedata
import json
import re
from pyarabic.araby import strip_tashkeel
from nltk.corpus import stopwords
from nltk.stem.arlstem import ARLSTem
from tashaphyne.stemming import ArabicLightStemmer

# def replace_char(ch):
#     if unicodedata.category(ch)[0]!="C":
#         return ch
#     else:
#         return " "
#
# print("".join(ch for ch in "new\"test\"" if unicodedata.category(ch)[0]!="C"))
tweets = []
output_tweets = []
# stemmer = ArabicLightStemmer()
# stemmer = ARLSTem()
# def stem(word):
#     stemmer.light_stem(word)
#     return stemmer.get_stem()
#
# print(" ".join([stem(word) for word in "يتعافي المرأ باصدقائه".split()]))

# with open("arabicNoEnglishTweets.json", encoding="utf8") as json_file:
#     tweets = json.load(json_file)

with open("stems.json", encoding="utf8") as json_file:
    tweets = json.load(json_file)

# print(len(tweets) - len(output_tweets))

# for tweet in output_tweets:
    # if len(tweet["hashtags"]) > 0:

# for tweet in tweets:
#     print(tweet["id"])
#     output_tweets.append({
#         "id": tweet["id"],
#         "clean_tweet": tweet["clean_tweet"]
#     })
#
with open("test.json", "w", encoding="utf8") as outfile:
    json.dump(tweets[0], outfile, indent=4, ensure_ascii=False)

print("DONE")
# print(re.sub(r'(.)\1+', r'\1', strip_tatweel("هذا رااااائـــئـــع")))

# stopwords = stopwords.words('arabic')

# stopwords_file = open("stopwords0.txt", "r", encoding="utf8")
# stopwords += stopwords_file.read().splitlines()
# stopwords_file.close()

# new_stopwords_file = open("stopwords.txt", "w", encoding="utf8")
# for word in stopwords:
#     new_stopwords_file.write(strip_tashkeel(word) + '\n')
# new_stopwords_file.close()

# stopwords_file = open("stopwords.txt", "r", encoding="utf8")
# print(len(stopwords_file.read().splitlines()))
