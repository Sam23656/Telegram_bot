from .Products.get_products import get_products_router
from .Categorires.get_categories import categories_router
from .Brands.get_brands import brands_router
from .Products.delete_products import delete_products_router
from .Products.add_products import add_products_router

__all__ = [
    'get_products_router',
    'categories_router',
    'brands_router',
    'delete_products_router',
    'add_products_router'
]
