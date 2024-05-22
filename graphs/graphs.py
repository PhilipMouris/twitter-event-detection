import json
import plotly.express as px
import requests
from bs4 import BeautifulSoup

tweets = []

usernames = ["MoSalah", "Byoussef", "amrkhaled", "amrdiab", "youm7", "MustafaHosny", "HamzaNamira", "amrwaked", "OfficialHenedy", "ElBaradei", "Donia", "NaguibSawiris", "ahelmy", "nabilelhalfawy", "HendSabry", "AlAhly", "AlAhram", "Hamaki", "trikaofficial", "midoahm", "HamzawyAmr", "GalalAmer", "alsha3rawy", "ElNennY", "Amradib", "ZSCOfficial", "Shorouk_News", "CBCEgypt", "AhmedFathi", "belalfadl", "YosriFouda", "Hassanelshafei", "MoezMasoud", "AlMasryAlYoum", "ONENT", "KhaledElNabawy", "GameelaIsmail", "HamdeenSabahy", "AlaaAswany", "TahrirNews", "DrAbolfotoh", "AlsisiOfficial", "Sakiatweets", "ahmadesseily", "Bey2ollak", "tamerhosny", "abdrhmanabnody", "ElSherif", "ElwatanNews"]

def username_to_object(username):
    return {
        "username": username.lower(),
        "count": 0
    }

tweets_count = list(map(username_to_object, usernames))

with open("../final datasets/twintDataset.json") as json_file:
    tweets = json.load(json_file)

for tweet in tweets:
    for tweet_count in tweets_count:
        if tweet_count["username"] == tweet["username"]:
            tweet_count["count"] = tweet_count["count"] + 1
            break

high_profile_tweet_counts = []

for count in tweets_count:
    if count["username"] == "youm7" or count["username"] == "alahram" or count["username"] == "shorouk_news" or count["username"] == "elwatannews" or count["username"] == "almasryalyoum" or count["username"] == "tahrirnews":
        high_profile_tweet_counts.append(count)

def list_diff(list1, list2):
    out = [item for item in list1 if not item in list2]
    return out

user_profile_tweet_counts = list_diff(tweets_count, high_profile_tweet_counts)

fig = px.bar(tweets_count, x = "username", y = "count")
fig.show()

fig = px.bar(high_profile_tweet_counts, x = "username", y = "count")
fig.show()

fig = px.bar(user_profile_tweet_counts, x = "username", y = "count")
fig.show()

youm7_categories = []

with open("categories.json", encoding="utf8") as json_file:
    youm7_categories = json.load(json_file)

fig = px.pie(youm7_categories, values='count', names='category', title='Categories of latest 500 tweets by youm7')
fig.show()

# youm7_tweets = [tweet for tweet in tweets if tweet["username"] == "youm7"][0:500]
# print(len(youm7_tweets))
# youm7_categories = []
# count = 1
#
# for tweet in youm7_tweets:
#     print(count)
#     count += 1
#     if len(tweet["urls"]) == 0:
#         continue
#     url = tweet["urls"][0]
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text)
#     metas = soup.find_all('meta')
#     if len([meta.attrs['content'] for meta in metas if 'property' in meta.attrs and meta.attrs['property'] == 'article:section']) == 0:
#         print("no meta")
#         continue
#     category = [meta.attrs['content'] for meta in metas if 'property' in meta.attrs and meta.attrs['property'] == 'article:section'][0]
#     if any(elem["category"] == category for elem in youm7_categories):
#         for item in youm7_categories:
#             if item["category"] == category:
#                 item["count"] = item["count"] + 1
#     else:
#         youm7_categories.append({
#             "category": category,
#             "count": 1,
#         })
#
# with open("categories.json", "w", encoding="utf8") as outfile:
#     json.dump(youm7_categories, outfile, indent=4, ensure_ascii=False)
