"""
Exercise 30. Word Frequency Counter (The Histogram)
Practice Problem: Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.

Exercise Purpose: This is a classic “Natural Language Processing” (NLP) task. It teaches you how to map data to occurrences, which is the logic used by search engines to index web pages or by social media platforms to identify trending hashtags.

"""


def get_stats(text:list) -> dict:
  count ={}
  for i in text:
    count[i] = count.get(i,0) + 1
  return count

text = "apple banana apple cherry banana apple"

list_l = text.split()

occurances = get_stats(list_l)

print(occurances)