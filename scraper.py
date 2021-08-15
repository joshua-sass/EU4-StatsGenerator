from urllib.request import urlopen
from selenium import webdriver
import time

class scraper:
	def __init__(self):
		pass

	def testing(self):
		#prints html to console for testing
		html = urlopen("https://nixx.is-fantabulo.us/paperman/").read().decode('utf-8')
		print(html)

	def interact(self, filename):
		#bulk function for interacting with paperman, uploads file and downloads new one.
		options = webdriver.ChromeOptions() 
		options.add_experimental_option("excludeSwitches", ["enable-logging"])

		browser = webdriver.Chrome("C:/Users/josh/OneDrive - Texas A&M University/Documents/PythonWork/chromedriver_win32/chromedriver.exe")
		browser.get('https://nixx.is-fantabulo.us/paperman/')
		time.sleep(2)

		#file_input = browser.find_element_by_id("root") #try path instead
		#file_input = browser.file_element_by_xpath("/html/body/div[0]/div[0]/form[0]/input[1]")
		file_input = browser.file_element_by_xpath("/html/body/div[0]/div[0]/form[0]/input")
		#time.sleep(2)

		browser.close()