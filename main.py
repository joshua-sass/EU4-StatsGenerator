from scraper import scraper
from file_read import file_read

if __name__ == "__main__":
	scraping = scraper()

	#scraping.testing()

	print("gib filename")
	#filename = input()
	filename = "GermanyBaseline.eu4"

	scraping.interact(filename)