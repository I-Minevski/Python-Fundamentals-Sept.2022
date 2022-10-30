word=input()
word_list=[i for i, i in enumerate(word)]
vowels=['a', 'o', 'u', 'e', 'i']
cleaned=[i for i in word_list if i not in vowels]
cleaned_string=''.join(i for i in cleaned)  #kato slojish neshto m/u '' to se prisuedinqwa kum stringa
print(cleaned_string)