
# using except and error method to avoid error and ending up with tracback

# count the approximate number of words in the single file
# text file analysis
# Pass statement
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
    words = contents.split(',')
    print(words)
    num_words = len(words)
    print(num_words)



# working with Multiple files


def count_words(file_name):
    try:
        with open(file_name, encoding='utf-8') as file_object:
            contents = file_object.read()
            print(contents)

    except FileNotFoundError:
        msg = "Sorry, the file" + file_name + " does not exist."
        print(msg)
    else:
    # count the approximate number of words in the file
        words = contents.split(',')
        print(words)
        num_words = len(words)
        print(num_words)

file_name_list = ['/Users/sanchitbhardwaj/PycharmProjects/DE_Pandas/costs.csv']
for file_name in file_name_list:
    count_words(file_name)

# Failing silently (Pass statement)
def count_words(file_name):
    try:
        with open(file_name, encoding='utf-8') as file_object:
            contents = file_object.read()
            print(contents)

    except FileNotFoundError:
        pass
    else:
    # count the approximate number of words in the file
        words = contents.split(',')
        print(words)
        num_words = len(words)
        print(num_words)

file_name_list = ['/Users/sanchitbhardwaj/PycharmProjects/DE_Pandas/cost.csv']
for file_name in file_name_list:
    count_words(file_name)
