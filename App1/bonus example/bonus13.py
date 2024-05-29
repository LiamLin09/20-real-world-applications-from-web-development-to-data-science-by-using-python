import parsers13

feet_inches = input("enter feet and inches: ")


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parse = parsers13.parse(feet_inches)
result = convert(parse['feet'], parse['inches'])

print(f"{parse['feet']} feet and {parse['inches']} inches is equal to {result} meters.")
print(f"kid is {result} meters")

if result < 150:
    print("kid cannot use the slid.")
else:
    print("kid can use the slide.")