class file_read:
	def __init__(self, filename):
		#SEARCH FOR human=yes
		print("file processing beginning...")
		file_read = open(filename, 'r', encoding='utf-8')
		lines = file_read.readlines()

		self.important_info = []

		iterator = 0
		reading = True
		temp = ""
		for line in lines:
			if "map_area_data{" in line:
				self.important_info.append(temp)
				reading = False
				temp = ""
			if reading == True:
				temp += line
			if "human=yes" in line:
				reading = True
			if "government_reform_progress=" in line and reading==True:
				self.important_info.append(temp)
				reading = False
				temp = ""

	def campaign_stats(self):

		campaign_info = self.important_info[0]
		campaign_info_arr = campaign_info.splitlines() #puts info into array based on newline, not quite sure i want to go this route

		campaign_stats_arr = []
		temp = ""
		reading = False
		for line in campaign_info_arr:
			if "key=" in line:
				reading = True
			if "}" in line and reading==True:
				reading = False
				temp = " ".join(temp.split())
				campaign_stats_arr.append(temp)
				temp = ""
			if reading == True:
				temp += " " + line 

		return campaign_stats_arr

	def country_stats(self):

		country_info  = self.important_info[1]
		country_info_arr  = country_info.splitlines()

		return " "

	def process(self):

		#im currently parsing twice blocks out of the code, hence two strings in the array
		campaign = self.campaign_stats()
		country  = self.country_stats()		

		print(campaign)
		print(country)