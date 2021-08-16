from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
import shutil
import getpass
import os

class scraper:
	def __init__(self):
		pass

	def testing(self):
		#prints html to console for testing
		html = urlopen("https://nixx.is-fantabulo.us/paperman/").read().decode('utf-8')
		print(html)

	def interact(self, filename):
		#bulk function for interacting with paperman, uploads file and downloads new one.
		current_dic = os.getcwd()
		current_dic.replace("\\", "/")

		options = webdriver.ChromeOptions() 
		options.add_experimental_option("excludeSwitches", ["enable-logging"]) #a little bit of trolling bc bluetooth wont play nice (???) idk

		browser = webdriver.Chrome("C:/Users/josh/OneDrive - sassware/Documents/PythonWork/chromedriver_win32/chromedriver.exe", options=options)
		browser.get('https://nixx.is-fantabulo.us/paperman/')
	
		#file_input = browser.find_element_by_name("file")
		#file_input = browser.find_element_by_id("root")
		#file_input = browser.file_element_by_xpath("/html/body/div[0]/div[0]/form[0]/input[1]")
		file_name_string = current_dic + "/" + filename #GermanyBaseline.eu4
		file_input = browser.find_element_by_css_selector("[aria-label='File selection']").send_keys(file_name_string)
		file_input = browser.find_element_by_xpath("//input[@value='Paperman it']").send_keys("\n")

		new_filename = "paperman_" + filename
		user = getpass.getuser()
		path_to_newfile = "C:/Users/" + user + "/Downloads/" + new_filename
		path = Path(path_to_newfile)
		while not path.exists():
			print("Waiting to download!")
			time.sleep(3)

		shutil.move(path_to_newfile, current_dic +"/nonironman_" + filename)	

		browser.close()
		return(current_dic +"/nonironman_" + filename)