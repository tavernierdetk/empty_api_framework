import requests


url = "http://127.0.0.1:5000/test/time"
params = {
    "query_body": "Test string"
}

res = requests.get(url,
                   params=params
                   )
print(res)
print(res.content)

