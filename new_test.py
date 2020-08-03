import requests
from bs4 import BeautifulSoup
import pprint

pp = pprint.PrettyPrinter(width=4000)

# for num in range(23309):
#     num += 1

url = 'https://cod.tracker.gg/warzone/leaderboards/stats/all/Kills?page=1'
res = requests.get(url)
html_soup = BeautifulSoup(res.text, 'html.parser')

userAndPlatform = html_soup.find_all('td', class_='username')
kills = html_soup.find_all('td', class_="stat")
matches = html_soup.find_all('td', class_='stat collapse')
del kills[1::2]


userInfo = []
userKills = []
userMatchesPlayed = []

platform = []
kills1 = []


final = []

players = []

gamesPlayed = []
tired = []  # Remove this




for info in userAndPlatform:
    # This for loop interates through the data of the bs4.Result.Set and appends a string of data to list "players"

    players.append(str(info))

for j in range(len(players)):
    # This for loop interates through the list "players" and separates the platform they play on
    # from the name of the player themselves, cleans it, appends them to temporary variables "gamers" and "platform"
    # respectively and then appends both temporary lists to the list "userInfo"

    gamers = [str(players[j][160:]).split('>')[0].split('/')[1]]
    platform = [str(players[j][160:]).split('/')[0]]
    userInfo.append(gamers + platform)

for kill in kills:
    # This for loop interates through the data of a bs4.Result.Set and appends a string of data to list "kills1"

    kills1.append(str(kill))

for i in range(len(kills1)):
    # This for loop interates through the variable "kills1" and separates the platform they play on
    # from the name of the player themselves, cleans it, appends it to the temporary list "kills"
    # and then appends them the list "userKills"

    kills = [str(kills1[i])[50:].split('>')[1].split('<')[0].replace(',', '')]
    userKills.append(kills)

for match in matches:
    # This for loop interates through the data of a bs4.Result.Set and appends a string of data to list "gamesPlayed"

    gamesPlayed.append(str(match))

for i in range(len(gamesPlayed)):
    # This for loop interates through the variable "gamesPlayed" and separates the platform they play on
    # from the name of the player themselves, cleans it, appends it to the temporary list "game"
    # and then appends them the list "userMatchesPlayed"

    game = [str(gamesPlayed[i][50:].split('>')[1].split('<')[0].replace(',', ''))]
    userMatchesPlayed.append(game)

for h in range(len(userInfo)):

    final.append(userInfo[h] + userKills[h] + userMatchesPlayed[h])

pp.pprint(final)

