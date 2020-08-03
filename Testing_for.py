import requests
from bs4 import BeautifulSoup
import pprint

pp = pprint.PrettyPrinter(width=4000)

# for num in range(23309):
#     num += 1
players = []
use = []
gamers = []
platform = []
kills = []
matchesPlayed = []
temp0 = []
final = []

url = 'https://cod.tracker.gg/warzone/leaderboards/stats/all/Kills?page=1'
res = requests.get(url)  # Using Requests to get a response model
bs = BeautifulSoup(res.text, 'lxml')

url2 = 'https://cod.tracker.gg/warzone/leaderboards/stats/all/Kills?page=1'
res2 = requests.get(url2)
html_soup = BeautifulSoup(res2.text, 'html.parser')

userAndPlatform = bs.find_all('td', class_='username')
killsAndMatches = html_soup.find_all('td', class_='stat')

for x in userAndPlatform:
    players.append((str(x)))

for j in range(len(players)):
    platform = [str(players[j][160:]).split('/')[0]]
    gamers = [str(players[j][160:]).split('>')[0].split('/')[1]]
    use.append(gamers + platform)
# print(use)
for i in range(len(killsAndMatches) - 1):
    kills = str(killsAndMatches[i])[50:].split('>')[1].split('<')[0].replace(',', '')
    matchesPlayed = str(killsAndMatches[i+1])[50:].split('>')[1].split('<')[0].replace(',', '')

    if int(kills) > int(matchesPlayed):  # TODO Fix list out of bounds error
        temp1 = [kills, matchesPlayed]
        temp0.append(temp1)
    if int(matchesPlayed) > int(kills):
        temp2 = [matchesPlayed, kills]
        temp0.append(temp2)
for i in range(len(use)):
    final.append(use[i] + temp0[i])

for x in range(len(final)):
    print(final[x])
