from .Products.get_products import get_products_router
from .Categorires.get_categories import categories_router
from .Brands.get_brands import brands_router
from .Products.delete_products import delete_products_router
from .Products.add_products import add_products_router
from .Products.update_products import update_products_router
from .Client.add_or_update_client import add_or_update_client_router
from .Client.client_profile import client_profile_router
from .Cart.add_product_to_cart import add_product_to_cart_router

__all__ = [
    'get_products_router',
    'categories_router',
    'brands_router',
    'delete_products_router',
    'add_products_router',
    'update_products_router',
    'add_or_update_client_router',
    'client_profile_router',
    'add_product_to_cart_router'
]
