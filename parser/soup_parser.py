import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

from parser.services import clean_price, parse_description, download_image

BASE_URL = "https://kitka-sonya.com/shop/"


@dataclass
class Product:
    title: str
    current_price: int
    old_price: int
    rating: float
    image_link: str
    description: dict
    image_path: str


def get_soup(url: str) -> BeautifulSoup | None:
    r = requests.get(url, timeout=10)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def parse_product(link: str) -> Product:
    soup = get_soup(link)

    title = soup.select_one(".product_title.entry-title")
    title = title.text.strip() if title else ""

    price_block = soup.select_one(".product_price, .summary .price")

    if price_block:
        current_price_el = price_block.select_one("span.woocommerce-Price-amount")
        old_price_el = price_block.select_one("del .woocommerce-Price-amount")
        current_price = int(clean_price(current_price_el.text.strip())) if current_price_el else None
        old_price = int(clean_price(old_price_el.text.strip())) if old_price_el else None
    else:
        current_price = old_price = None

    rating_el = soup.select_one(".star-rating")
    if rating_el and rating_el.get("aria-label"):
        try:
            rating = float(rating_el["aria-label"].split()[1])
        except (KeyError, IndexError):
            rating = None
    else:
        rating = None

    image_el = soup.select_one(".woocommerce-product-gallery__image img, .wp-post-image")
    image_link = image_el["src"] if image_el else ""
    image_path = download_image(image_link) if image_link else ""

    description = parse_description(soup)

    return Product(
        title=title,
        current_price=current_price,
        old_price=old_price,
        rating=rating,
        image_link=image_link,
        description=description,
        image_path=image_path,
    )

def get_all_product_links() -> list:
    links = []
    page = 1

    while True:
        url = f"{BASE_URL}page/{page}/" if page > 1 else BASE_URL
        soup = get_soup(url)

        if soup is None:
            break

        products = soup.select(".product-thumb-hover a")
        if not products:
            break

        for p in products:
            link = p.get("href")
            if link:
                links.append(link)

        page += 1

    return list(set(links))
