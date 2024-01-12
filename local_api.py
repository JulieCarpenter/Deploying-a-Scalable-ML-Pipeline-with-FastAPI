import json
import requests

# send a GET using the URL http://127.0.0.1:8000 to retrieve the welcome message
url = "http://127.0.0.1:8000"
r = requests.get(url)
# print the status code
print(r.status_code)
# print the welcome message
print(r.text)

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# send a POST using the data above
post_url = url+"/data"
pr = requests.post(post_url, json=data)
# print the status code
print(pr.status_code)
# print the result
print(pr.text)
