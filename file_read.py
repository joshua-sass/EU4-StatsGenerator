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
			searching = 'key="'
			iterator = stat.find(searching)
			if iterator == -1:
				continue
			end_iterator = stat[iterator+:].find('"')
			key = stat[iterator+len(searching):iterator+len(searching)+end_iterator]
			#print(key)

			searching = 'localization="'
			iterator = stat.find(searching)
			localization = None
			if iterator != -1:
				end_iterator = stat[iterator+len(searching):].find('"')
				localization = stat[iterator+len(searching):iterator+len(searching)+end_iterator]
			#print(localization)

			searching = 'value='
			iterator = stat.find(searching)
			value = None
			if iterator != -1:
				end_iterator = stat[iterator+len(searching):].find(' ')
				if end_iterator == -1:
					value = stat[iterator+len(searching):]
				else:
					value = stat[iterator+len(searching):iterator+len(searching)+end_iterator]
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
		#potentially track monarchs?!?
		#war="
		#raw_development=
		#technology={
		#estate={
		#score_place=
		#estimated_monthly_income=
		#max_manpower=
		#max_sailors=
		#starting_development=
		#innovativeness=
		#adm_spent_indexed={
		#dip_spent_indexed={
		#mil_spent_indexed={

		country_info  = self.important_info[1]
		country_info_arr  = country_info.splitlines()

		war_arr = []

		for line in country_info_arr:
			searching = 'war="'
			iterator = line.find(searching)
			if iterator != -1:
				end_iterator = line[iterator+len(searching):].find('"')
				war_var = line[iterator+len(searching):iterator+len(searching)+end_iterator]	
				war_arr.append(war_var)
				print(war_var)

			searching = 'development='
			iterator = line.find(searching)
			if iterator != -1:
				#end_iterator = line[iterator+len(searching):].find('"')
				development_var = line[iterator+len(searching):]	

		war_arr = list(set(war_arr)) #oopsies, randomizing probs need to think of a better way but im lazy atm
		return country_info_arr

	def file_find(self, word_find, end_char, no_end_char): #experimental, dont think ill use

		country_info  = self.important_info[1]
		country_info_arr  = country_info.splitlines()

		iterator = stat.find(word_find)
		word_found = None
		if iterator != -1 and no_end_char is False:
			end_iterator = stat[iterator+len(word_find):].find(end_char)
			word_found = stat[iterator+len(word_find):iterator+len(word_find)+end_iterator]
		elif iterator != -1 and no_end_char is True:
			word_found = stat[iterator+len(word_find):]

		return word_found

	def process(self):

		#im currently parsing two blocks out of the code, hence two strings in the array
		campaign = self.campaign_stats()
		country  = self.country_stats()		

		#print(campaign)
		#print(country)