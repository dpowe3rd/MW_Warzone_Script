from bs4 import BeautifulSoup
import requests
import selenium
import json
import pprint

pp = pprint.PrettyPrinter(width=4000)

for num in range(23309):
    num = num + 1
    url = 'https://cod.tracker.gg/warzone/leaderboards/stats/all/Kills?page={}'.format(num)
    res = requests.get(url)
    bs = BeautifulSoup(res.text, 'lxml')
    t_body = bs.find_all(class_='username')
    p = []

    for x in t_body:
        p.append(str(x))

    for j in range(len(p)):
        user = [str(p[j][143:]).split('>')[0]]

        print(user)

