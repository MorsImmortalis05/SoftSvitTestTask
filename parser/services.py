from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def clean_price(price: str) -> str:
    result = price.replace(" ", "").replace("грн", "")
    return result

def parse_description(soup: BeautifulSoup) -> dict:
    tab = soup.select_one("#tab-additional_information table")
    if not tab:
        return {}

    result = {}

    for row in tab.select("tr"):
        key = row.select_one("th")
        val = row.select_one("td")
        if key and val:
            result[key.text] = val.text

    return result

def get_description_dict(driver):
    description_dict = {}
    table = driver.find_element(By.CSS_SELECTOR, "#tab-additional_information table")
    rows = table.find_elements(By.CSS_SELECTOR, "tr")

    for row in rows:
        label = row.find_element(By.CSS_SELECTOR, "th").text.strip()
        value = row.find_element(By.CSS_SELECTOR, "td").text.strip()
        description_dict[label] = value

    return description_dict
