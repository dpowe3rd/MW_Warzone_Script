from bs4 import BeautifulSoup
import requests
import selenium
import json
import pprint

pp = pprint.PrettyPrinter(width=4000)  # Pretty Print to make Console text Easy to read

for num in range(23309):
    num += 1  # Incrementing

    url = 'https://cod.tracker.gg/warzone/leaderboards/stats/all/Kills?page={}'.format(num)
    res = requests.get(url)  # Using Requests to get a response model
    bs = BeautifulSoup(res.text, 'lxml')

    url2 = 'https://cod.tracker.gg/warzone/leaderboards/stats/all/Kills?page=1'
    res2 = requests.get(url2)
    html_soup = BeautifulSoup(res2.text, 'html.parser')

    users = bs.find_all(class_='username')
    stats = html_soup.find_all('td', class_='stat')

    players = []
    use = []
    temp = []
    k = 2 in range(len(stats))

    for x in users:
        players.append(str(x))

        for j in range(len(players)):
            user = [str(players[j][160:]).split('>')[0]]

            for i in range(len(stats)):
                kills = str(stats[i])[50:].split('>')[1].split('<')[0]
                matches = str(stats[i:k])[50:].split('>')[1].split('<')[0]

                if kills > matches:                 # TODO Fix list out of bounds error
                    # print([kills, matches])
                    temp[i].append(kills, matches)
                else:
                    pass

        print(user[0].split('/') + temp)

    # use.append(user[0].split('/'))
