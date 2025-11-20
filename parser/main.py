import json

from parser.soup_parser import parse_product
from parser.soup_parser import get_all_product_links

BASE_URL = "https://kitka-sonya.com/shop/"

def main():
    links = get_all_product_links()
    products = []

    for link in links:
        products.append(parse_product(link))

    with open("sonia_products.json", "w", encoding="utf-8") as f:
        json.dump([p.__dict__ for p in products], f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
