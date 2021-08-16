from scraper import scraper
from file_read import file_read
import os.path

if __name__ == "__main__":
	scraping = scraper()

	#scraping.testing()

	print("What's your filename? (please dont forget .eu4 extension or i have to ask again)") #need to add exception handling here!
	good_input = False
	while good_input == False:
		filename = input()
		if os.path.isfile(filename):
			break
		#filename = "GermanyBaseline.eu4"
		print("Oops! Your file doesnt exist in the current directory or you mistyped it. Try again please :)")
	
	processing = file_read(scraping.interact(filename))
	processing.process()