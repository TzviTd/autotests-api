import httpx
from tools.fakers import get_random_email
create_user_payload = {
  "email": get_random_email(),
  "password": "abcd",
  "lastName": "surname",
  "firstName": "name",
  "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_data = create_user_response.json()

print("New user:", create_user_data)
print("Status:", create_user_response.status_code)

login_payload = {
  "email": create_user_data["user"]["email"],
  "password": "abcd"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login data:", login_response_data)
print("Login status:", login_response.status_code)

patch_user_payload = {
  "email": get_random_email(),
  "password": "abcd",
  "lastName": "surname",
  "firstName": "name",
  "middleName": "string"
}

patch_user_headers = {
  "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}

patch_request = httpx.patch(f"http://127.0.0.1:8000/api/v1/users/{create_user_data["user"]["id"]}",
                            json=patch_user_payload,
                            headers=patch_user_headers
                            )
patch_request_data = patch_request.json()

print("Updated user:", patch_request_data)
print("Patch status:", patch_request.status_code)
