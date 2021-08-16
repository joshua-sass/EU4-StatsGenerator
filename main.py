from scraper import scraper
from file_read import file_read

if __name__ == "__main__":
	scraping = scraper()

	#scraping.testing()

	print("gib filename (please dont forget .eu4 extension or i have to ask again)") #need to add exception handling here!
	#filename = input()
	filename = "GermanyBaseline.eu4"
	
	processing = file_read(scraping.interact(filename))
	processing.process()