import requests

url = "http://127.0.0.1:8000/send_data"

data = {
    "temperature" : 25.9
}

response = requests.post(url, json = data)
print("Server Response:", response.text)