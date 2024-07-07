import json

numbers = [2,3,4,5,8,11,29]

file_name = 'numbers.json'
try:
    with open(file_name, 'w') as file_object:
        json.dump(numbers,file_object)

except FileNotFoundError:
    msg = "Sorry, the file" + file_name + "does not exist."
    print(msg)