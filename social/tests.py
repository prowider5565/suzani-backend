import requests


request = requests.post(
    "https://suzani-abdulhakim.uz/accounts/verify-email/",
    json={
        "username": "string",
        "email": "prowider.dev@gmail.com",
        "password": "123",
        "role": "client",
    },
)

print(request.status_code)
print(request.json())
print(request.text)
