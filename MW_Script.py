from bs4 import BeautifulSoup
import requests
import selenium
import json
import pprint

pp = pprint.PrettyPrinter(width=4000)  # Pretty Print to make Console text Easy to read

players = []
use = []
temp = []
gamers = []
platform = []

for num in range(23309):
    num += 1  # Incrementing

    url = 'https://cod.tracker.gg/warzone/leaderboards/stats/all/Kills?page={}'.format(num)
    res = requests.get(url)  # Using Requests to get a response model
    bs = BeautifulSoup(res.text, 'lxml')

    url2 = 'https://cod.tracker.gg/warzone/leaderboards/stats/all/Kills?page={}'.format(num)
    res2 = requests.get(url2)
    html_soup = BeautifulSoup(res2.text, 'html.parser')

    userAndPlatform = bs.find_all('td', class_='username')
    killsAndMatches = html_soup.find_all('td', class_='stat')

    for x in userAndPlatform:
        players.append((str(x)))

    for j in range(len(players)):
        platform = [str(players[j][160:]).split('/')[0]]
        gamers = [str(players[j][160:]).split('>')[0].split('/')[1]]
        use.append(gamers+platform)

        # for i in range(len(killsAndMatches) - 1):
        #     kills = str(killsAndMatches[i])[50:].split('>')[1].split('<')[0]
        #     matches = str(killsAndMatches[i + 1])[50:].split('>')[1].split('<')[0]
        #
        #     print([kills, matches])
        #     if kills > matches:  # TODO Fix list out of bounds error
        #         # print([kills, matches])
        #         # use[i].append(kills, matches)
        #         # print(use)
        #         pass
        #     else:
        #         pass

    # use.append(user[0].split('/'))
    print(use)
