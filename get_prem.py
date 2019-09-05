import urllib
import urllib.request
from bs4 import BeautifulSoup
import string


class EPL:

	#function to easily utilise the BS4 module
	def make_soup(self, url):
		open_page = urllib.request.urlopen(url)
		soupdata = BeautifulSoup(open_page,'html.parser')
		return soupdata


	def get_table(self):
		soup = self.make_soup("https://www.premierleague.com.tables")

		for team_position in soup.findAll("tr", {"class":"tableDark"}):
			return team_position.text




def main():
	epl = EPL()
	print(epl.get_table())

if __name__ == '__main__':
	main()






"""
TO DO:

	

	def get_fixtures(team = None):

	def get_odds():

	def make_acca(match_result):

	def get_fixture(home_team, away_team):

	def get_results():

	def get_result(home_team, away_team):

	def get_scores():

	def get_corners():

	def get_cards():




"""