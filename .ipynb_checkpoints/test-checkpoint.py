import requests

url = "http://127.0.0.1:8000/send_data"

data = {
    "device id": "Test device 1",
    "data 1" : 30.4,
    "data 2" : 40
}

response = requests.post(url, json = data)
print("Server Response:", response.json())