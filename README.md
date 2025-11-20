# 🛒 Kitka-Sonya Product Parser

This project scrapes products from the online store **kitka-sonya.com**, collecting product data such as:

* Titles
* Prices
* Ratings
* Descriptions
* Image links

It also downloads product images locally.

---

## 🚀 How to Run the Parser

Follow these steps to run the Kitka-Sonya product parser locally.

### 1. Clone the repository

```bash
git clone https://github.com/MorsImmortalis05/SoniaParser.git
cd SoniaParser
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux
# or
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the parser

In the project root:

```bash
python parser/main.py
```

This will:

* Fetch all product links
* Parse each product
* Download product images into `/sonia_images/`
* Save structured data into `sonia_products.json`

### 5. Output files

After running the script, you will see:

```
sonia_products.json   → parsed product data
sonia_images/         → downloaded product images
```