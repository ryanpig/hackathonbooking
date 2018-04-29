import random, json
from pprint import pprint

str1 = "usr_first"
str2 = "usr_home"

part_nums = ['ECA-1EHG102','CL05B103KB5NNNC','CC0402KRX5R8BB104']

def json_list(list):
    lst = []
    d = {}
    for pn in list:
        d['mpn']=pn
        lst.append(d)
    return json.dumps([dict(mpn=pn) for pn in lst])

def writejson(data):
    with open('profile_1.txt', 'w') as outfile:
        json.dump(data, outfile)
def appendjson(v1,v2):
    with open('profile_1.txt', mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)
    with open('profile_1.txt', mode='w', encoding='utf-8') as feedsjson:
        entry = {'usr_first': v1, 'usr_home': v2}
        feeds.append(entry)
        json.dump(feeds, feedsjson)


def readjson():
    with open('profile_1.txt', 'r') as outfile:
        data = json.load(outfile)
    return data


v1 = 'chang'
v2 = 'taiwan'

t = {
    "usr_first": v1,
    "usr_home": v2
}
t2 = {
    "usr_first": v2,
    "usr_home": v1
}

#print(json_list(part_nums))
#t = json_list(part_nums)
writejson(t)
data =readjson()
pprint(data["usr_first"])
#appendjson('111','222')
#data =readjson()
#pprint(data)

#print(data["maps"][0]["id"])


