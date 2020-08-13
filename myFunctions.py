from bs4 import BeautifulSoup
import requests
import pprint
import csv

pp = pprint.PrettyPrinter(width=4000)  # Pretty Print to make Console text Easy to read


def warzone_scraper(url, num):
    """
     A function that takes the parameter 'url' and a page number to start from, from the parameter 'start', and scrapes
     the page for a table of Call of Duty: Warzone Battle Royale statistics by player. The statistic that I am scraping
     for is determined by the url parameter.


    :param url: The url that I want to data scrape from.
    :param num: What page number of the url I want to start from.
    :return: A list of data that will be appended to a csv file.
    """

    x = url + '{}'  # I was forced to add a temp variable here, to increment the value of the end of the string

    for num in range(num, 24900):  # A for loop that counts up to 24900, which is the number of pages of data I need.
        # range(x, 23309) where x is the previous page I stopped mining at, x is manually being changed by me as I go
        num += 1   # Incrementing

        url = x.format(num)

        res = requests.get(url)

        print(url)
        #
        # html_soup = BeautifulSoup(res.text, 'html.parser')
        #
        # userAndPlatform = html_soup.find_all('td', class_='username')
        # kills = html_soup.find_all('td', class_="stat")
        # matches = html_soup.find_all('td', class_='stat collapse')
        # del kills[1::2]
        #
        # userInfo = []  # These are the lists that I will use to concatenate elements into my final list
        # userKills = []
        # userMatchesPlayed = []
        #
        # platform = []
        # kills1 = []
        # gamesPlayed = []
        #
        # final = []
        #
        # players = []
        #
        # for info in userAndPlatform:
        #     # This for loop interates through the data of the bs4.Result.Set and appends a string of data to list "players"
        #
        #     players.append(str(info))
        #
        # for j in range(len(players)):
        #     # This for loop interates through the list "players" and separates the platform they play on
        #     # from the name of the player themselves, cleans it, appends them to temporary variables "gamers" and "platform"
        #     # respectively and then appends both temporary lists to the list "userInfo"
        #     userInfo.append([str(players[j][160:]).split('"')[0].split('/')[1]] + [str(players[j][160:]).split('/')[0]])
        #
        # for kill in kills:
        #     # This for loop interates through the data of a bs4.Result.Set and appends a string of data to list "kills1"
        #
        #     kills1.append(str(kill))
        #
        # for i in range(len(kills1)):
        #     # This for loop interates through the variable "kills1" and separates the platform they play on
        #     # from the name of the player themselves, cleans it, appends it to the temporary list "kills"
        #     # and then appends them the list "userKills"
        #
        #     userKills.append([str(kills1[i])[50:].split('>')[1].split('<')[0].replace(',', '')])
        #
        # for match in matches:
        #     # This for loop interates through the data of a bs4.Result.Set and appends a string of data to list "gamesPlayed"
        #
        #     gamesPlayed.append(str(match))
        #
        # for i in range(len(gamesPlayed)):
        #     # This for loop interates through the variable "gamesPlayed" and separates the platform they play on
        #     # from the name of the player themselves, cleans it, appends it to the temporary list "game"
        #     # and then appends them the list "userMatchesPlayed"
        #
        #     userMatchesPlayed.append([str(gamesPlayed[i][50:].split('>')[1].split('<')[0].replace(',', ''))])
        #
        # for h in range(len(userInfo)):
        #     final.append(userInfo[h] + userKills[h] + userMatchesPlayed[h])
        #
        # fmt = '{:<14}{:<18}{:15}{:15}{:15}'
        #
        # pp.pprint(fmt.format('User', 'Platform', 'Kills', 'Matches Played', 'Page {}'.format(num)))
        # pp.pprint(final)


warzone_scraper('https://cod.tracker.gg/warzone/leaderboards/battle-royale/all/Kills?page=', 5)
