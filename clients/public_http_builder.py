from httpx import Client

def get_public_http_client():
    """
    The function creates the basic httpx.Client
    :return: httpx.Client object 
    """
    return Client(timeout=100, base_url="http://localhost:8000")