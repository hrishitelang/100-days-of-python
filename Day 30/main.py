import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
# data_dict = data.to_dict()
# print(data_dict)
# Step 1: Create a dictionary in this format: {'A': 'Alfa', 'B': 'Bravo}
dictionary = {value.letter: value.code for (key, value) in data.iterrows()}
# print(dictionary)


# Step 2: Create a list of the phonetic code words from a word
# that the user inputs
while True:
    name = input('Enter a word: ').upper()
    try:
        name = [i for i in name]
        # print(name)
        nato_name = [dictionary[i] for i in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_name)
        break
