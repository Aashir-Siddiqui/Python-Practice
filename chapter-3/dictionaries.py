student = {
    "name": "Aashir",
    "age": 22,
    "course": "Python"
}

print(student["name"])
print(student.get("age"))
print(student.get("email"))
student["age"] = 23
print(student)
student.update({"course": "Backend Python"})
print(student)
student["email"] = "aashir@test.com"
print(student)
student.update({
    "city": "Karachi",
    "active": True
})
print(student)
student.pop("email")
print(student)
student.popitem()
print(student)
del student["age"]
print(student)

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, ":", value)

d1 = student.copy()
d2 = dict(student)
print("d2", d2)

users = {
    "user1": {"name": "Aashir", "age": 22},
    "user2": {"name": "Ali", "age": 25}
}

print(users["user1"]["name"])

for user, info in users.items():
    print(user, info["name"])

print(student.keys())
print(student.values())
print(student.items())

student.setdefault("country", "Pakistan")
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, None)
print(new_dict)

user = {
    "username": "aashir",
    "password": "123456",
    "role": "admin"
}

if user.get("role") == "admin":
    print("Access Granted")


student.clear()
print(student)