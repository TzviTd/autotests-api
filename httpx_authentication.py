import httpx

payload = {
    "email": "johndoe@example.com",
    "password": "1234"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

print("Login data:", login_response_data)
print("Status:", login_response.status_code)

refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

refresh_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("Refresh data:", refresh_response_data)
print("Status:", refresh_response.status_code)