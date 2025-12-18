import httpx

payload = {
    "email": "johndoe@example.com",
    "password": "1234"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

print("Login data:", login_response_data)
print("Status:", login_response.status_code)

users_me_header = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}

user_me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=users_me_header)
user_me_response_data = user_me_response.json()

print("User me data:", user_me_response_data)
print("Status:", user_me_response.status_code)