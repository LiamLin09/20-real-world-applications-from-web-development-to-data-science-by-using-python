import parsers13
import converter13

feet_inches = input("enter feet and inches: ")

parse = parsers13.parse(feet_inches)
result = converter13.convert(parse['feet'], parse['inches'])

print(f"{parse['feet']} feet and {parse['inches']} inches is equal to {result} meters.")
print(f"kid is {result} meters")

if result < 150:
    print("kid cannot use the slid.")
else:
    print("kid can use the slide.")