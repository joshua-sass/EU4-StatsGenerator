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
			if "id=" in line:
				reading = True
			if "}" in line and reading==True:
				reading = False
				temp = " - ".join(temp.split())
				campaign_stats_arr.append(temp)
				temp = ""
			if reading == True:
				temp += " " + line

		campaign_stats_tples = []		
		for stat in campaign_stats_arr:
			#print(stat)
			iterator = stat.find('key="')
			if iterator == -1:
				continue
			end_iterator = stat[iterator+5:].find('"')
			key = stat[iterator+5:iterator+5+end_iterator]
			#print(key)

			iterator = stat.find('localization="')
			localization = None
			if iterator != -1:
				end_iterator = stat[iterator+14:].find('"')
				localization = stat[iterator+14:iterator+14+end_iterator]
			#print(localization)

			iterator = stat.find('value=')
			value = None
			if iterator != -1:
				end_iterator = stat[iterator+6:].find(' ')
				if end_iterator == -1:
					value = stat[iterator+6:]
				else:
					value = stat[iterator+6:iterator+6+end_iterator]
			#print(value)

			temp_arr = []
			temp_arr.append(key)
			if localization is not None:
				temp_arr.append(localization)
			if value is not None:
				temp_arr.append(value)
			if len(temp_arr) > 1:
				campaign_stats_tples.append(tuple(temp_arr))
			else:
				campaign_stats_tples.append(temp_arr)
			temp_arr[:]

		return campaign_stats_tples

	def country_stats(self):

		country_info  = self.important_info[1]
		country_info_arr  = country_info.splitlines()

		return country_info_arr

	def process(self):

		#im currently parsing two blocks out of the code, hence two strings in the array
		campaign = self.campaign_stats()
		country  = self.country_stats()		

		#print(campaign)
		print(country)