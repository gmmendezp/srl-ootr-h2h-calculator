from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import ceil

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(30)

def wait():
  return WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_class_name('testrace')))

URL = 'http://www.speedrunslive.com/races/game/#!/oothacks/'
driver.get(URL + '1')
wait()
soup = BeautifulSoup(driver.page_source, 'html.parser')
pages = ceil(int(soup.find(id='side_gamestats').find_all('strong')[1].text) / 16)

standings = []
standingsWithFF = []
for i in range(1, pages + 1):
  driver.get(URL + str(i))
  wait()
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  races = soup.find_all('table', {'class': 'raceResults testrace'})
  for race in races:
    raceGoal = race.find_all('tr')[1].text.replace(';', '')
    raceNumber = race.find_all('tr')[0].find_all('th')[1].text.replace('#', '')
    pageStandings = [raceNumber, raceGoal]
    pageStandingsWithFF = [raceNumber, raceGoal]

    for row in race.find_all('tr')[2:]:
      tds = row.find_all('td')
      name = tds[1].text
      forfeit = 'Forfeit' in tds[2].text
      if not forfeit:
        pageStandings.append(name)
      pageStandingsWithFF.append(name)
    if len(pageStandings) > 2:
      standings.append(pageStandings)
    if len(pageStandingsWithFF) > 2:
      standingsWithFF.append(pageStandingsWithFF)

with open('standings.txt', 'w') as filehandle:
  filehandle.writelines('%s\n' % ';'.join(s) for s in standings)
with open('standingsWithFF.txt', 'w') as filehandle:
  filehandle.writelines('%s\n' % ';'.join(s) for s in standingsWithFF)

driver.quit()