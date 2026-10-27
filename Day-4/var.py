# accept a string of text
# convert all words to lowercase
# remove basic punctuations 
# split text into words 
# count occurances using a dict
# print the words in descending order
# Handles Empty Input


# accept a string. 
import string

def miniproject(text):

  clean_text = text.lower().translate(str.maketrans('','',string.punctuation))

  # split into words
  new_clean_list = clean_text.split() 

  # count the words
  count_word_dict = {}
  for word in new_clean_list:
    count_word_dict[word] = count_word_dict.get(word,0) + 1

  # sort the list 
  for words,counts in sorted(count_word_dict.items(),key=lambda item : item[1],reverse=True): # descending order 
    print(f"{words} : {counts}")



text = miniproject("Python is fun, and Python is useful!")