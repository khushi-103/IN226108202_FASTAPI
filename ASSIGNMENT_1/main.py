from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# ── Temporary data — acting as our database for now ──────────
products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499, 'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook', 'price': 99, 'category': 'Stationery', 'in_stock': True},
    {'id': 3, 'name': 'USB Hub', 'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set', 'price': 49, 'category': 'Stationery', 'in_stock': True},
    {'id': 5, 'name': 'Laptop Stand', 'price': 350, 'category': 'Electronics', 'in_stock': True},
    {'id': 6, 'name': 'Mechanical Keyboard', 'price': 230, 'category': 'Electronics', 'in_stock': False},
    {'id': 7, 'name': 'Webcam', 'price': 800, 'category': 'Electronics', 'in_stock': True},
]

# ── Endpoint 0 — Home ────────────────────────────────────────
@app.get("/")
def home():
    return {"message": "Welcome to our E-commerce API"}


# ── Endpoint 1 — Return all products ─────────────────────────
@app.get("/products")
def get_all_products():
    return {"products": products, "total": len(products)}

# ── Endpoint 2 — Task2:- Filter by Category name───────
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    filtered_products = [
        product for product in products
        if product["category"].lower() == category_name.lower()
    ]

    if not filtered_products:
        return {"error": "No products found in this category"}

    return filtered_products

# ── Endpoint 3 — Task3:- Return product where in-stock is True. Also return total count───────
@app.get("/products/instock")
def get_instock_products():
    
    instock_products = [
        product for product in products 
        if product["in_stock"] == True
    ]

    return {
        "in_stock_products": instock_products,
        "Total count": len(instock_products)
    }
# ── Endpoint 4 — Task4:- Show store summary───────
@app.get("/store/summary")
def store_summary():
    total_products = len(products)
    in_stock_count = sum(1 for product in products if product["in_stock"])
    out_of_stock_count = total_products - in_stock_count
    categories = list({product["category"] for product in products})  # unique categories

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock_count,
        "out_of_stock": out_of_stock_count,
        "categories": categories
    }

# ── Endpoint 5 — Task5:- Search Product by Name───────
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    # Case-insensitive search
    matched_products = [
        product for product in products
        if keyword.lower() in product["name"].lower()
    ]

    if not matched_products:
        return {"message": "No products matched your search"}

    return {
        "matched_products": matched_products,
        "count": len(matched_products)
    }

# ── Endpoint 6 — Bonus Task:- Cheapest and Most Expensive Product───────
@app.get("/products/deals")
def get_deals():
    if not products:
        return {"message": "No products available"}

    # Cheapest product
    best_deal = min(products, key=lambda x: x["price"])

    # Most expensive product
    premium_pick = max(products, key=lambda x: x["price"])

    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }