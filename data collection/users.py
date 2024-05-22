import twint
import json
import sys
import pprint

# usernames = ["MoSalah", "Byoussef", "amrkhaled", "amrdiab", "youm7", "MustafaHosny", "HamzaNamira", "amrwaked", "OfficialHenedy", "ElBaradei", "Donia", "NaguibSawiris", "ahelmy", "nabilelhalfawy", "HendSabry", "AlAhly", "AlAhram", "Hamaki", "trikaofficial", "midoahm", "HamzawyAmr", "GalalAmer", "alsha3rawy", "ElNennY", "Amradib", "ZSCOfficial", "Shorouk_News", "CBCEgypt", "AhmedFathi", "belalfadl", "YosriFouda", "Hassanelshafei", "MoezMasoud", "AlMasryAlYoum", "ONENT", "KhaledElNabawy", "GameelaIsmail", "HamdeenSabahy", "AlaaAswany", "TahrirNews", "DrAbolfotoh", "AlsisiOfficial", "Sakiatweets", "ahmadesseily", "Bey2ollak", "tamerhosny", "abdrhmanabnody", "ElSherif", "ElwatanNews"]

print("Fetching User")

c = twint.Config()
c.Username = sys.argv[1]
c.Store_object = True
# c.Hide_output = True

twint.run.Lookup(c)
user = twint.output.users_list

with open(sys.argv[1]+".json", "w", encoding="utf8") as outfile:
    json.dump(user[0].__dict__, outfile, indent=4, ensure_ascii=False)

print("JSON file ready")
