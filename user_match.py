""" HackDelft 2018
    Booking.comk Tinder extension
    v0.8
"""

###### PRE-STUFF --------------------------------------------------------------
### IMPORTS ------------------------------------------------------------------

from random import randrange, choice, sample, uniform
import numpy as np
from math import radians, atan2, cos, sin, sqrt
from datetime import datetime, timedelta
import json
import urllib


### CLASSES ------------------------------------------------------------------

class user:
    "Constructs a random user profile a user"
    
    def __init__(self):
        self.gender = choice(genders[:2]) ## assign gender and an according name
        if self.gender == "Male": 
            self.name = choice(names_m)
        elif self.gender == "Female":
            self.name = choice(names_f)
        self.surname = choice(surnames)
        self.age = randrange(18,80) ## set the age
        self.food = choice(eat) ## interested in eating out
        self.activity = sample(todo, randrange(3)+1) ## interested activities
        self.day_in = datetime(2018,randrange(3,8),randrange(30)+1) ## length of stay
        self.day_out = self.day_in + timedelta(days=randrange(9)+1)
        self.days_stay = stay_dur(self.day_in,self.day_out)
        self.language = sample(languages, randrange(4)+1) ## languages spoken
        self.loc_lat = uniform(41.3238,41.4838)
        self.loc_lon = 2.170738
        self.noft = randrange(6)+1
        self.budget = choice(wallet)
        self.netrate = randrange(-3, 11)


class me:
    "defines me"
    age = 33 ## my age
    def __init__(self):
        self.language = sample(languages, randrange(4)+1) ## languages I speak
        self.day_in = datetime(2018,4,29) ## how long I stay
        self.day_out = datetime(2018,5,1)
        self.days_stay = stay_dur(self.day_in,self.day_out)
        self.loc_lat = 41.3994
        self.loc_lon = 2.170738
        self.maxdist = 3
        self.activity = sample(todo, randrange(3)+1) ## interested activities
        self.gender_pref = "Female"
        self.size_pref = choice(["1","2","3-5","5+"])
        self.budget = choice(wallet)

### FUNCTIONS ----------------------------------------------------------
        
def dtd(dms):
    "convert dms to dd"
    dd = dms//1 + ((dms % 1)//0.01)/60 + ((dms % 0.01)//0.0001)/3600
    return dd
        
def compare(list1,list2):
    "returns number of common elements between two lists"
    comm = 0 
    if len(list1) > len(list2):
        for elem in list2:
            if elem in list1:
                comm += 1
    else:
        for elem in list1:
            if elem in list2:
                comm += 1
    return comm

def distance(coo11,coo12,coo21,coo22):
    coo11, coo12, coo21, coo22 = dtd(coo11),dtd(coo12),dtd(coo21),dtd(coo22)
    coo11, coo12, coo21, coo22 = radians(coo11),radians(coo12),radians(coo21),radians(coo22)
    R = 6378
    a = (0.5*(coo21-coo11))**2 + cos(coo11)*cos(coo21)*(0.5*(coo22-coo12))**2
    c = 2*atan2(sqrt(a),sqrt(1-a))
    d = R*c
    return d

def stay_dur(day_in,day_out):
    day_now = day_in
    days = []
    while day_now < day_out:
        days.append(day_now)
        day_now += timedelta(days=1)
    return days

def gender_pref(mypref,gend):
    if mypref == "No preference":
        pref = 0
    elif mypref == gend:
        pref = 1
    else:
        pref = -1
    return pref
    
def group_pref(mypref,grpsz):
    if int(eval(mypref))== grpsz:
        pref = 0
    elif mypref == gend:
        pref = 1
    else:
        pref = -1
    return pref

def readjson():
    with open('profile_1.txt', 'r') as outfile:
        data = json.load(outfile)
    return data
### BASE INFO ----------------------------------------------------------------

surnames = []
with open("surnames.csv") as f:
    for row in f:
        surnames.append(row.split(",")[0])
names = []
with open("names.csv") as f:
    for row in f:
        names.append(row.split(",")[0])
names_m = names[17653:]
names_f = names[:17653]

eat = ["yes","no"]
todo = ["museums", "sport", "relax","OOT","CMG","gastro"]
languages = ["hindi","english","chinese","russian","german","french"]
wallet = ["empty","small","full","overloaded"]
genders = ["Male","Female","No preference"]

def match_process():
    ###### CORE PROGRAM -----------------------------------------------------------

    nofu = 10000 # number of users to be generated
    users = []

    ### GENERATE PEOPLE ---------------------------------------------------------
    for i in range(nofu): #generate random dataset for other users
        users.append(user())

    iam = me() # generate mock main user
    read_from_data = True
    if read_from_data:
        data = readjson()
        if 'lang' in data:
            print(data['lang'])
            iam.language = data['lang']
    #iam.language = ["hindi","english"]
    ### FILTER RELEVANT PEOPLE ----------------------------
    "indices of users that travel to the same place at the same time and have a common language"
    same = []
    for i in range(nofu):
        if distance(iam.loc_lat,iam.loc_lon,users[i].loc_lat,users[i].loc_lon) < iam.maxdist:
            if compare(iam.days_stay,users[i].days_stay) > 0:
                if compare(iam.language,users[i].language) > 0:
                    same.append(i)
    print("Random profiles are generated..")

    ### EVALUATE COMMONALITY ----------------------------------------------------
    lan_comm = [(compare(iam.language,users[s].language))/len(iam.language) for s in same]  #number of common languages
    age_diff = [abs(users[s].age - iam.age) for s in same] #age difference
    act_comm = [compare(iam.activity,users[s].activity) for s in same]  #number of common activities
    gen_pref = [gender_pref(iam.gender_pref,users[s].gender) for s in same]
    days_comm = [(compare(iam.days_stay,users[s].days_stay))/len(iam.days_stay) for s in same]
    #grp_pref = [group_pref(iam.size_pref,users[s].noft) for s in same]
    bud_comm = [abs(wallet.index(iam.budget) - wallet.index(users[s].budget)) for s in same]

    rating = [np.sign(users[s].netrate) * (abs(users[s].netrate) ** (1 / 3)) for s in same]

    w_a, w_l, w_b, w_d, w_g, w_act, w_r = 1.2, 0.8, -1 / 6, 1, 1 / 2, 2 / 3, 1 / 3  # sets weight for commonality factors
    common = list(w_l * np.array(lan_comm) + w_a * 1 / np.array(age_diff) + w_act * np.array(act_comm) + w_g * np.array(
        gen_pref) + w_d * np.array(days_comm)) + w_b * np.array(bud_comm) + w_r * np.array(rating)  # commonality metric
    list1, list2 = zip(*sorted(zip(common, same)))  # order by commonality matrix

#    w_a, w_l, w_b, w_d, w_g, w_act = 0, 1, 0, 0, 0, 0 # sets weight for commonality factors

    print("Matching process finished..")

    ### RETURN SUGGESTED MATCHES --------------------------------------------
    count = 0
    usr_names = []
    usr_langs = []
    usr_gender = []
    usr_stayperiod = []
    usr_location = []
    for i in list2[::-1]:
        #print(users[i].name,users[i].surname, users[i].age-iam.age, users[i].language) # print suitable users ordered by degree of commonality
        if count<5:
            str_stay = str(users[i].day_in.strftime("%d-%m")) + "~" + str(users[i].day_out.strftime("%d-%m"))
            print(users[i].name, users[i].surname, users[i].age - iam.age,
                  users[i].language, users[i].gender, str_stay)  # print suitable users ordered by degree of commonality
            ##random location
            #lnk = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
            #page = urllib.request.urlopen(lnk)
            #txt = page.read()
            #WORDS = txt.splitlines()
            #hotelname = str(choice(WORDS))[2:-1].title()
            #hotelname += " Hotel"
            usr_names.append(users[i].name)
            usr_langs.append(users[i].language)
            usr_gender.append(users[i].gender)
            usr_stayperiod.append(str_stay)
            #usr_location.append(hotelname)
            count += 1
    return usr_names, usr_langs, usr_gender, usr_stayperiod