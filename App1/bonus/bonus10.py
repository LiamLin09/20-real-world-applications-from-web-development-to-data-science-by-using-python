try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That is a square.")

    area = width * length
    print(area)
except ValueError:
    print("Plz enter a number.")