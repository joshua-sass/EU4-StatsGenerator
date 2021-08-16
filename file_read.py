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
			end_iterator = stat[iterator+len(searching):].find('"')
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
		country_info_tples = []

		war_arr = []
		tech_flag = 0
		adm_spent_flag = 0
		dip_spent_flag = 0
		mil_spent_flag = 0
		tech_var = ""
		development_var = 0

		for line in country_info_arr:
			searching = 'war="'
			iterator = line.find(searching)
			if iterator != -1:
				end_iterator = line[iterator+len(searching):].find('"')
				war_var = line[iterator+len(searching):iterator+len(searching)+end_iterator]	
				war_arr.append(war_var)
				#print(war_var)

			searching = 'starting_development='
			iterator = line.find(searching)
			if iterator != -1:
				start_dev_var = line[iterator+len(searching):]	
				country_info_tples.append(tuple(["starting_development", start_dev_var]))	

			searching = 'raw_development='
			iterator = line.find(searching)
			if iterator != -1:
				#end_iterator = line[iterator+len(searching):].find('"')
				development_var = line[iterator+len(searching):]
				#print(development_var)
				country_info_tples.append(tuple(["development", development_var]))

			searching = 'technology={' #take string into 3 parts for adm, dip, mil respectively
			iterator = line.find(searching)
			if tech_flag == 1 or tech_flag == 2 or tech_flag == 3:
				iterator_temp = line.find('tech=')
				if iterator_temp != -1:
					tech_var += line[iterator_temp+5:]
					tech_flag += 1
			if iterator != -1:
				tech_flag = 1

			searching = 'score_place='
			iterator = line.find(searching)
			if iterator != -1:
				score_var = line[iterator+len(searching):]
				country_info_tples.append(tuple(["place in score", score_var]))

			searching = 'estimated_monthly_income='
			iterator = line.find(searching)
			if iterator != -1:
				income_var = line[iterator+len(searching):]
				country_info_tples.append(tuple(["income per month", income_var]))

			searching = 'max_manpower='
			iterator = line.find(searching)
			if iterator != -1:
				max_manpower_var = line[iterator+len(searching):]
				country_info_tples.append(tuple(["max manpower", float(max_manpower_var)*1000]))

			searching = 'max_sailors='
			iterator = line.find(searching)
			if iterator != -1:
				max_sailors_var = line[iterator+len(searching):]
				country_info_tples.append(tuple(["max sailors", float(max_sailors_var)]))

			searching = 'innovativeness='
			iterator = line.find(searching)
			if iterator != -1:
				inno_var = line[iterator+len(searching):]
				country_info_tples.append(tuple(["innovativeness", inno_var]))

			searching = 'adm_spent_indexed='
			iterator = line.find(searching)
			
			if adm_spent_flag == 1:
				temp_line = line.split()
				adm_sum = 0
				for admin in temp_line:
					temp_iterator = admin.find("=")
					adm_sum += int(admin[temp_iterator+1:])	
				adm_spent_flag = 2
				country_info_tples.append(tuple(["total admin spent", adm_sum]))

			if iterator != -1:
				adm_spent_flag = 1	

			searching = 'dip_spent_indexed='
			iterator = line.find(searching)

			if dip_spent_flag == 1:
				temp_line = line.split()
				dip_sum = 0
				for dip in temp_line:
					temp_iterator = dip.find("=")
					dip_sum += int(dip[temp_iterator+1:])	
				dip_spent_flag = 2
				country_info_tples.append(tuple(["total diplo spent", dip_sum]))


			if iterator != -1:
				dip_spent_flag = 1	

			searching = 'mil_spent_indexed='
			iterator = line.find(searching)

			if mil_spent_flag == 1:
				temp_line = line.split()
				mil_sum = 0
				for mil in temp_line:
					temp_iterator = mil.find("=")
					mil_sum += int(mil[temp_iterator+1:])	
				mil_spent_flag = 2	
				country_info_tples.append(tuple(["total mil spent", mil_sum]))

			if iterator != -1:
				mil_spent_flag = 1	

		country_info_tples.append(tuple(list(["wars", set(war_arr)]))) #oopsies, randomizing probs need to think of a better way but im lazy atm
		country_info_tples.append(tuple(["technology", tech_var[0:1], tech_var[2:3], tech_var[4:5]]))
		return country_info_tples

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

		print(campaign)
		print(country)