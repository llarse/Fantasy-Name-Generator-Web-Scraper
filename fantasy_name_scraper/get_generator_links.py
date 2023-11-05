from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

URL = "https://www.fantasynamegenerators.com"  # Replace with your target website


def get_php_links():
    # Set up the driver and open the URL
    # If you didn't add chromedriver to PATH, use webdriver.Chrome(executable_path='path_to_chromedriver')
    driver = webdriver.Chrome()
    driver.get(URL)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

    # Extract all links from the page
    all_links = [link.get_attribute("href")
                 for link in driver.find_elements(By.TAG_NAME, "a")]

    # Filter the links to only include those ending with .php
    php_links = [link for link in all_links if urlparse(
        link).path.endswith('.php')]

    driver.quit()

    url_dict = urls_to_dict(php_links)
    return url_dict


def urls_to_dict(urls):
    url_dict = {}
    for url in urls:
        # Parse the URL to extract the path
        path = urlparse(url).path
        # Remove the leading slash and .php extension
        name = path.lstrip('/').rstrip('.php')

        url_dict[name] = url
    return url_dict
