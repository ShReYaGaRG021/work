# -*- coding: utf-8 -*-
"""
Question 1: - Write a program that takes a string as input, and counts the frequency of each word 
in the string, there might be repeated characters in the string. Your task is to find the highest 
frequency and returns the length of the highest-frequency word.  

Example input - string = “write write write all the number from from from 1 to 100” 
Example output - 5 

Explanation - From the given string we can note that the most frequent words are “write” and “from”
and the maximum value of both the values is “write” and its corresponding length is 5
"""


from collections import Counter
# pylint: disable=too-many-function-args

#a = input(str("Enter the Input String: "))
a = "write write write all the number from from from 1 to 100"
b = "Hello Hello hello how how how are you you you today today today"
c = "What a beautiful beautiful beautiful beautiful weather weather weather weather"

def highest_frequency(f):
    text = f.split()
    text = Counter(text)
    #print(text)
    max_count = max(text.values())
    common = [text for text, count in text.items() if count == max_count]
    len_common = max(common, key=len)
    print(len(len_common))

highest_frequency(a) # test case 1
highest_frequency(b) # test case 2
highest_frequency(c) # test case 3