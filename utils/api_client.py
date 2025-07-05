import requests
import logging

BASE_URL = "https://fakestoreapi.com"
session = requests.Session()

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


def send_request(method, endpoint, **kwargs):
    url = BASE_URL + endpoint
    timeout = kwargs.pop("timeout", 10)  # Вынесли timeout отдельно
    try:
        response = session.request(method=method, url=url, timeout=timeout, **kwargs)
        logging.info(f"{method.upper()} {url} -> {response.status_code}")
        return response
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        raise


def post_login(username, password, **kwargs):
    payload = {"username": username, "password": password}
    return send_request("post", "/auth/login", json=payload, **kwargs)


def get_products():
    return send_request("get", "/products")


def get_product(product_id):
    return send_request("get", f"/products/{product_id}")


def create_cart(cart_data):
    return send_request("post", "/carts", json=cart_data)


def get_cart(cart_id):
    return send_request("get", f"/carts/{cart_id}")


def delete_cart(cart_id):
    return send_request("delete", f"/carts/{cart_id}")
