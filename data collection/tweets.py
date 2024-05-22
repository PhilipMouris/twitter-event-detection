import twint
import json
import sys

# usernames = ["MoSalah", "Byoussef", "amrkhaled", "amrdiab", "youm7", "MustafaHosny", "HamzaNamira", "amrwaked", "OfficialHenedy", "ElBaradei", "Donia", "NaguibSawiris", "ahelmy", "nabilelhalfawy", "HendSabry", "AlAhly", "AlAhram", "Hamaki", "trikaofficial", "midoahm", "HamzawyAmr", "GalalAmer", "alsha3rawy", "ElNennY", "Amradib", "ZSCOfficial", "Shorouk_News", "CBCEgypt", "AhmedFathi", "belalfadl", "YosriFouda", "Hassanelshafei", "MoezMasoud", "AlMasryAlYoum", "ONENT", "KhaledElNabawy", "GameelaIsmail", "HamdeenSabahy", "AlaaAswany", "TahrirNews", "DrAbolfotoh", "AlsisiOfficial", "Sakiatweets", "ahmadesseily", "Bey2ollak", "tamerhosny", "abdrhmanabnody", "ElSherif", "ElwatanNews"]
outputTweets = []

def tweet_to_dict(tweet):
    return tweet.__dict__

# for username in usernames:
#     print("fetched ", len(outputTweets), " tweets")
#     print("fetching ", username)
c = twint.Config()
c.Username = sys.argv[1]
c.Store_object = True
c.Since = "2019-01-01"
c.Format = "Fetching " + sys.argv[1] + " tweets"
# c.Hide_output = True
twint.run.Search(c)
tweets = twint.output.tweets_list
outputTweets += list(map(tweet_to_dict, tweets))

with open(sys.argv[1]+".json", "w", encoding="utf8") as outfile:
    json.dump(outputTweets, outfile, indent=4, ensure_ascii=False)

print("JSON file ready")
