from fantasy_name_scraper.scraper import scrape_names
# The first 4 names have a much higher chance of having a more guttural sound to them, ideal for the stronger and brutish looking aliens.
# The next 3 names have a much higher chance of having a more melodic sound to them, making them ideal for the softer and gentle looking aliens.
# The last 3 names can sound both guttural and melodic and anything in between. These names are more randomized than the previous 2 types and unlike the other 2 types, these aren't always easy to pronounce in English.


names = scrape_names("alien", 18)
print(names)
print(len(names))
