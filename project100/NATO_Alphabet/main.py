import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dic = {row.letter:row.code for (index, row) in data.iterrows()}


word = input("Enter a word: ").upper()
new_list = [new_dic[letter] for letter in word]
print(new_list)
