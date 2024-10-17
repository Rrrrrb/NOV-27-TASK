import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()  # Use the response from the first request
    print("API data is loaded successfully")
    print(data)
else:
    print("Failed to load data")
