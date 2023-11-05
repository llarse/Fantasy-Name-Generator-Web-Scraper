
# Fantasy Name Generators Web Scraper

This is a basic web scraper for https://www.fantasynamegenerators.com/

*This code was made extremely quickly as I needed it for a project - It has not been checked thoroughly before release. There is no edge case/error handling.*






## Installation

You can clone the repo and use the library as a module or you can navigate to it and run
```
pip install .
```
    
## Usage

**scrape_names(generator_name, num_of_names)** 

*Scrape the number of names from the given generator on fantasynamegenerators.com*

Args:

* generator_name (str): The name of the generator you want to scrape
    ```
    e.g. "alien" --> "http://www.fantasynamegenerators.com/alien-names.php"

    fstring: "http://www.fantasynamegenerators.com/{generator_name}-names.php"
    ```
* num_of_names (int): The number of names you want to scrape

Returns: 

* names (list): A list of names from the given generator
## Future Improvements

If I ever revist this project (it suited my needs so the chances are low), I would like to add:
* Error and Edge Case handling
* generator links dictionary - I started implementation in get_generator_links.py but never finished it if youd like to continue


## Acknowledgements

Many thanks to Emily - the creator of the fantasynamegenerators.com website. 
I checked for a robots.txt page and in the about section to ensure that web scraping was allowed. In my research, I found nothing to suggest that it wasnt allowed nor do I believe this web scraper morally or legally betrays the purpose or philosophy of the website. However, if you have information contrary, please contact me immediately to have this removed. 
