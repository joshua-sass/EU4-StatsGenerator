from scraper import scraper

if __name__ == "__main__":
	scraping = scraper()
	
	#scraping.testing()

	print("gib filename")
	filename = input()

	scraping.interact(filename)