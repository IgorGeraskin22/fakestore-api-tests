from utils.api_client import send_request

def post_login(username: str, password: str, timeout: int = 5):
    payload = {
        "username": username,
        "password": password
    }
    return send_request("post", "/auth/login", json=payload, timeout=timeout)
