def get_average():
    with open("files2/data.txt", 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    avg = sum(values) / len(values)
    return avg


average = get_average()
print(average)