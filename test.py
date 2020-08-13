from multiprocessing import Pool, freeze_support
from bs4 import BeautifulSoup
import requests
import pprint
import csv
import time

pp = pprint.PrettyPrinter(width=4000)  # Pretty Print to make Console text Easy to read
start_time = time.time()
base_url = 'https://cod.tracker.gg/warzone/leaderboards/battle-royale/all/Kills?page='
url_list = []
done = []
missed_pages = []
missed_url_list = []
completed_urls = []


def create_urls():
    for i in range(1, 100):
        url_list.append(base_url + str(i))


def missed_urls():
    for i in range(len(missed_pages)):
        missed_url_list.append(base_url + str(missed_pages[i]))


def warzone_scraper(site):
    """
     A function that takes the parameter 'url' and a page number to start from, from the parameter 'start', and scrapes
     the page for a table of Call of Duty: Warzone Battle Royale statistics by player. The statistic that I am scraping
     for is determined by the url parameter.


    :param site: The url that I want to data scrape from.
    :return: A list of data that will be appended to a csv file.
    """

    url = str(site)
    res = requests.get(url)

    page_number = url[73:]

    html_soup = BeautifulSoup(res.text, 'html.parser')

    user_and_platform = html_soup.find_all('td', class_='username')
    kills = html_soup.find_all('td', class_="stat")
    matches = html_soup.find_all('td', class_='stat collapse')
    del kills[1::2]

    user_info = []  # These are the lists that I will use to concatenate elements into my final list
    user_stats = []
    user_matches_played = []

    kills1 = []
    games_played = []

    final = []
    players = []

    for info in user_and_platform:
        # This for loop interates through the data of the bs4.Result.Set and appends a string of data to list "players"

        players.append(str(info))

    for j in range(len(players)):
        # This for loop interates through the list "players" and separates the platform they play on
        # from the name of the player themselves, cleans it, appends them to temporary variables "gamers" and "platform"
        # respectively and then appends both temporary lists to the list "userInfo"
        user_info.append([str(players[j][160:]).split('"')[0].split('/')[1]] + [str(players[j][160:]).split('/')[0]])

    for kill in kills:
        # This for loop interates through the data of a bs4.Result.Set and appends a string of data to list "kills1"

        kills1.append(str(kill))

    for i in range(len(kills1)):
        # This for loop interates through the variable "kills1" and separates the platform they play on
        # from the name of the player themselves, cleans it, appends it to the temporary list "kills"
        # and then appends them the list "userKills"

        user_stats.append([str(kills1[i])[50:].split('>')[1].split('<')[0].replace(',', '')])

    for match in matches:
        # This for loop interates through the data of a bs4.Result.Set and appends a string of data to list
        # "gamesPlayed"

        games_played.append(str(match))

    for i in range(len(games_played)):
        # This for loop interates through the variable "gamesPlayed" and separates the platform they play on
        # from the name of the player themselves, cleans it, appends it to the temporary list "game"
        # and then appends them the list "userMatchesPlayed"

        user_matches_played.append([str(games_played[i][50:].split('>')[1].split('<')[0].replace(',', ''))])

    for h in range(len(user_info)):
        final.append(user_info[h] + user_stats[h] + user_matches_played[h])

    fmt = '{:<14}{:<18}{:<15}{:<15}{:<15}'
    # pp.pprint(fmt.format('User', 'Platform', 'Kills', 'Matches Played', 'Page ' + page_number))
    # pp.pprint('Page ' + page_number)

    if not final:
        print("The page, " + page_number + " has not been recorded.")
        missed_pages.append(str(page_number))
        print(page_number + " has been added to the missing pages list, and is ready to be added. \n")

    else:
        print("The page, " + page_number + " has been recorded. \n")
        for i in range(len(final)):
            done.append(final[i])


create_urls()

if __name__ == "__main__":
    freeze_support()
    p = Pool(10)
    p.map(warzone_scraper, url_list)
    p.terminate()
    p.join()
    print(done)

# pp.pprint(done)
missed_urls()

if len(missed_url_list) > 0:
    if __name__ == "__main__":
        freeze_support()
        p = Pool(10)
        p.map(warzone_scraper, missed_url_list)
        p.terminate()
        p.join()
        print(done)
