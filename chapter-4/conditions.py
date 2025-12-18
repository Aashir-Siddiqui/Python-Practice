age = 18

if age >= 18:
    print("You are eligible to vote")

marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
else:
    print("Lag gaye")

result = "Pass" if marks >= 50 else "Fail"
print(result)

print("Adult") if age >= 18 else print("Minor")

has_id = True
is_admin = True
is_owner = False
logged_in = False

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not Allowed")
    
if is_admin or is_owner:
    print("Access granted")
else:
    print("Access Denied")

if not logged_in:
    print("Please login")
else:
    print("Welcome User")
    
if age >= 18:
    if has_id:
        print("Ja sakte ho")
    else:
        print("Chala Ja BSDk")
else:
    print("Goli beta masti nahi")

if age > 18:
    pass   # future code
else:
    print("Minor")

user = "admin"
password = "12345"

if user == "admin" and password == "12345":
    print("Ye tu admin hai")
elif user == "admin":
    print("Invalid Passowrd")
else:
    print("Ap admin nahi ho")