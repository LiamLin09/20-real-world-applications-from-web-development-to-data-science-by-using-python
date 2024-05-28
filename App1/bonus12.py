feet_inches = input("enter feet and inches: ")


def convert(feet_inches):
    part = feet_inches.split(" ")
    feet = float(part[0])
    inch = float(part[1])
    meter = feet * 0.3048 + inch * 0.0254
    return meter


result = convert(feet_inches)
print(f"kid is {result} meters")

if result < 150:
    print("kid cannot use the slid.")
else:
    print("kid can use the slide.")