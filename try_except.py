

file_path = '/Users/sanchitbhardwaj/PycharmProjects/DE_Pandas/costs.csv'
try:
    with open(file_path, encoding='utf-8') as file_object:
        contents = file_object.read()
        print(contents)

except FileNotFoundError:
    msg = "Sorry, the file" + file_path + "does not exist."
    print(msg)
else:
    # count the approximate number of words in the file
    words = contents.split()
    print(words)
    num_words = len(words)
    print(num_words)

