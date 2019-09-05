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


	#optimisation on print required - None type printing at end of list, goal difference needs to work
	def get_table(self):
		#lists to store data
		teams = []
		points = []
		table_entry = []

		#posts request to server
		soup = self.make_soup("https://www.premierleague.com/tables")
		
		#team names
		for team in soup.findAll("span", {"class" : "long"}):
			teams.append(team.text)
		
		#ensures tot_teams == 20
		teams = teams[:20]

		#points total
		for points_tot in soup.findAll("td", {"class" : "points"}):
			points.append(points_tot.text)

		#tot_teams == num_points_totals
		points = points[:20]

		#Note to developer: Get goal difference to work

		#compile the above into one element of a list
		for i in range(19):
			table_entry.append(teams[i] + " " + str(points[i]))

		for entry in table_entry:
			print(entry)


def main():
	epl = EPL()
	print(epl.get_table())

if __name__ == '__main__':
	main()






"""
TO DO:

	

	def get_fixtures(team = None):

	def get_odds(team):

	def make_acca(match_result):

	def get_fixture(home_team, away_team):

	def get_results():

	def get_result(home_team, away_team):

	def get_scores():

	def get_corners():

	def get_cards():




"""
