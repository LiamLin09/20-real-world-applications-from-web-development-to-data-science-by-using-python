password = input("Plz Enter a new password: ")
result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False


digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

uppercase = False
for i in password:
    if i .isupper():
        uppercase = True
result["upper_case"] = uppercase



print(result)
if all(result.values()):
    print("Strong Password!!!")
else:
    print("Weak Password!!")