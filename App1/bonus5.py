waiting_list = ['Ryan', 'John', 'Iris', 'Q']
waiting_list.sort()

for index, name in enumerate(waiting_list):
    row = f"{index + 1}.{name.capitalize()}"
    print(row)