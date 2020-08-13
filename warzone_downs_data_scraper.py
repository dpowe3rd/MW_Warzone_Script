from bs4 import BeautifulSoup
import requests
import pprint
import csv

pp = pprint.PrettyPrinter(width=4000)  # Pretty Print to make Console text Easy to read
actualFinal = []    # Final list I will append to.

# with open('C:/Users/dpowe_4rzki43/OneDrive/Desktop/CSV/Test2.csv', 'a+') as outcsv:
#     writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
#     writer.writerow(['User', 'Platform', 'Kills', 'Matches Played'])


for num in range(0, 23309):    # A for loop that counts up to 23309, which is the number of pages of data I need.
    # range(x, 23309) where x is the previous page I stopped mining at, x is manually being changed by me as I go
    num += 1  # Incrementing

    url = 'https://cod.tracker.gg/warzone/leaderboards/battle-royale/all/Downs?page={}'.format(num)
    res = requests.get(url)
    html_soup = BeautifulSoup(res.text, 'html.parser')

    userAndPlatform = html_soup.find_all('td', class_='username')
    downs = html_soup.find_all('td', class_="stat")
    matches = html_soup.find_all('td', class_='stat collapse')
    del downs[1::2]

    userInfo = []               # These are the lists that I will use to concatenate elements into my final list
    userDowns = []
    userMatchesPlayed = []

    platform = []
    downs1 = []
    gamesPlayed = []

    final = []

    players = []

    for info in userAndPlatform:
        # This for loop interates through the data of the bs4.Result.Set and appends a string of data to list "players"

        players.append(str(info))

    for j in range(len(players)):
        # This for loop interates through the list "players" and separates the platform they play on
        # from the name of the player themselves, cleans it, appends them to temporary variables "gamers" and "platform"
        # respectively and then appends both temporary lists to the list "userInfo"
        userInfo.append([str(players[j][160:]).split('"')[0].split('/')[1]] + [str(players[j][160:]).split('/')[0]])

    for down in downs:
        # This for loop interates through the data of a bs4.Result.Set and appends a string of data to list "kills1"

        downs1.append(str(down))

    for i in range(len(downs1)):
        # This for loop interates through the variable "kills1" and separates the platform they play on
        # from the name of the player themselves, cleans it, appends it to the temporary list "kills"
        # and then appends them the list "userKills"

        userDowns.append([str(downs1[i])[50:].split('>')[1].split('<')[0].replace(',', '')])

    for match in matches:
    # This for loop interates through the data of a bs4.Result.Set and appends a string of data to list "gamesPlayed"

        gamesPlayed.append(str(match))

    for i in range(len(gamesPlayed)):
        # This for loop interates through the variable "gamesPlayed" and separates the platform they play on
        # from the name of the player themselves, cleans it, appends it to the temporary list "game"
        # and then appends them the list "userMatchesPlayed"

        userMatchesPlayed.append([str(gamesPlayed[i][50:].split('>')[1].split('<')[0].replace(',', ''))])

    for h in range(len(userInfo)):
        final.append(userInfo[h] + userDowns[h] + userMatchesPlayed[h])

    actualFinal.append(final)

    fmt = '{:<14}{:<18}{:15}{:15}{:15}'

    pp.pprint(fmt.format('User', 'Platform', 'Downs', 'Matches Played', 'Page {}'.format(num)))
    pp.pprint(final)

    # with open('C:/Users/dpowe_4rzki43/OneDrive/Desktop/Warzone_CSV_Files/warzone_deaths.csv', 'a+') as outcsv:
    #     # configure writer to write standard csv file
    #     writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    #     for item in final:
    #         # Write item to outcsv
    #         writer.writerow([item[0], item[1], item[2], item[3]])
