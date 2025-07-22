# Simple stub to emulate product search without external API
def dummy_product_search(query: str):
    products = [
        {"id": 1, "name": "Nike Air Zoom", "price": 120, "link": "https://example.com/nike-air-zoom"},
        {"id": 2, "name": "Adidas Ultraboost", "price": 150, "link": "https://example.com/adidas-ultraboost"},
        {"id": 3, "name": "Apple iPhone 15", "price": 999, "link": "https://example.com/iphone15"},
    ]
    if not query:
        return products
    return [p for p in products if query.lower() in p["name"].lower()]
