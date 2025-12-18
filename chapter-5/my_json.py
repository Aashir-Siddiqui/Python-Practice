import json
import requests

data = {
    "name": "Ali",
    "age": 22,
    "skills": ["Python", "Django"],
    "active": True
}

# python object to JSON string
json_str = json.dumps(data, indent=4)
print(json_str)
print(type(json_str))

# JSON string to python object
py_data = json.loads(json_str)
print(py_data)
print(type(py_data))


user = {
    "id": 1,
    "profile": {
        "username": "aashir123",
        "email": "aashir@gmail.com",
        "followers": 1500
    }
}

print(user["profile"]["username"])
print(user["profile"]["followers"])

res = requests.get("https://jsonplaceholder.typicode.com/users")
users = res.json()
print(users)

for user in users:
    print(user["username"], "-", user["email"])

print(type(users))

data = {
    "b": 2,
    "a": 1,
    "c": 3
}

print(json.dumps(data, sort_keys=True))


# Python	JSON
# dict	    Object
# list	    Array
# tuple	    Array
# str	    String
# int	    Number
# float	    Number
# True	    true
# False	    false
# None	    null