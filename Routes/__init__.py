from .Products.get_products import products_router
from .Categorires.get_categories import categories_router
from .Brands.get_brands import brands_router

__all__ = [
    'products_router',
    'categories_router',
    'brands_router'
]
