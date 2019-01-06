#-*- coding:utf-8 -*-
import key
import datetime

search = api.search(q="334 or @atagtbrabrtvgd", count=100)
t = 1
now = datetime.datetime.now()
year = now.year
month = now.month
date = now.day
rank = []
for Rize in search:
    time = Rize.created_at + datetime.timedelta(hours=9)
    name = Rize.user.screen_name
    if time >= datetime.datetime(year, month, date, 3, 34, 0, 0) and "@" not in Rize.text and "RT" not in Rize.text:
        twiid = Rize.id
        element = ((twiid >> 22) + 1288834974657) / 1000
        d = datetime.datetime.fromtimestamp(element)
        g = str(d.microsecond).rstrip("000")
        tweet = "@{}---{}\n".format(name, g)
        rank.append(tweet)
    else:
        twiid = Rize.id
        element = ((twiid >> 22) + 1288834974657) / 1000
        d = datetime.datetime.fromtimestamp(element)
        g = str(d.microsecond).rstrip("000")
        fr = "Fr @{}---{}\n".format(name, g)
        break

data = "Result\n"
no = len(rank)
for rize in rank:
    data = "{}位 {}".format(no, rize) + data
    no -= 1

print(data)


while True:
    try:
        twi = data + fr + "\n#334"
        print(twi)
        api.update_status(twi)
        break
    except:
        cre = data.split("\n")
        cre.pop(-1)
        data = ""
        print("unko")
        for rize in cre:
            data =  data + "{}\n".format(rize)
