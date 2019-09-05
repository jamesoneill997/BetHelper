from bs4 import BeautifulSoup
import string
import requests


class EPL:

	#function to easily utilise the BS4 module
	def make_soup(self, url):
		open_page = requests.get(url).text
		soupdata = BeautifulSoup(open_page,'html.parser')
		return soupdata

	def get_teams(self):
		teams = []
		soup = self.make_soup("https://www.premierleague.com/tables")
		
		#team names
		for team in soup.findAll("span", {"class" : "long"}):
			teams.append(team.text)
		teams = teams[:20]

		return teams


	#optimisation on print required goal difference needs to work
	def get_table(self):
		#lists to store data
		teams = []
		points = []
		table_entry = []

		#posts request to server
		soup = self.make_soup("https://www.premierleague.com/tables")
		
		#team names - Using previous function
		for team in self.get_teams():
			teams.append(team)
		

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

		


	def get_game_weeks(self, team = None, week = None):
		game_weeks = []
		team_game_weeks = []
		soup = self.make_soup("https://www.cbssports.com/soccer/news/premier-league-game_weeks-results-schedule-scores-liverpool-alone-in-first-manchester-united-and-chelsea-struggle/")

		for week in soup.findAll("h3"):
			game_weeks.append(week.text)

		#some tidying up
		game_weeks = game_weeks[:35]

					


def main():
	epl = EPL()
	epl.get_table()

if __name__ == '__main__':
	main()






"""
TO DO:

	

	def get_odds(team):

	def make_acca(match_result):

	def get_fixture(home_team, away_team):

	def get_results():

	def get_result(home_team, away_team):

	def get_scores():

	def get_corners():

	def get_cards():

	def add_to_calendar():

	def add_to_my_games():

	


"""
