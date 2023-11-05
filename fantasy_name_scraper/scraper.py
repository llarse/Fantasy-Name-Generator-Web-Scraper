from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.fantasynamegenerators.com/alien-names.php"


def scrape_names(generator_name, num_of_names):
    ''' Scrape the number of names from the given generator on fantasynamegenerators.com
    Args: generator_name (str): The name of the generator you want to scrape,
    e.g. "alien" --> "http://www.fantasynamegenerators.com/alien-names.php"
    num_of_names (int): The number of names you want to scrape
    Returns: names (list): A list of names from the given generator'''
    # format generator_name
    url = "https://www.fantasynamegenerators.com/" + \
        generator_name + "-names.php"

    # Set up the driver and open the URL
    driver = webdriver.Chrome()

    names = []

    # Calculate the number of pages to load
    batches = num_of_names // 10
    if num_of_names % 10 != 0:
        batches += 1

    for _ in range(batches):
        driver.get(url)

        # Get the results
        results_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )

        batch_names = results_div.text.split('\n')
        names.extend(batch_names)

    # Truncate the names to be the length of num_of_names.
    names = names[:num_of_names]

    driver.quit()
    return names
