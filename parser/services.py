from bs4 import BeautifulSoup


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
            result[key.text.strip()] = val.text.strip()

    return result


import requests
import os


def download_image(url: str, folder: str = "sonia_images"):
    os.makedirs(folder, exist_ok=True)
    filename = url.split("/")[-1].split("?")[0]
    path = os.path.join(folder, filename)

    response = requests.get(url)
    response.raise_for_status()

    with open(path, "wb") as f:
        f.write(response.content)

    return path

