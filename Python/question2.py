"""Question 2: - Consider a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just one character at the index in the string, and the remaining characters will occur the same number of times. 
Given a string, determine if it is valid. If so, return YES , otherwise return NO . 
Note - You have to write at least 2 additional test cases in which your program will run successfully and provide an explanation for the same. 
Example input 1 - s = “abc”. 
This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 } 
Example output 1- YES Example input 2 - s “abcc”. 
This string is not valid as we can remove only 1 occurrence of “c”. 
That leaves character frequencies of { “a”: 1, “b”: 1 , “c”: 2 } Example output 2 - NO"""


def valid_string(string):
    freq = {}
    for i in string:
        freq[i] = freq.get(i, 0) + 1
    #print(freq)

    freq_count = {}
    for j in freq.values():
        freq_count[j] = freq_count.get(j, 0) + 1
    #print(freq_count)    

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) >= 2:
        return "NO"

    # Checking if we can remove one occurrence of a character to make it a valid string
    freq_values = list(freq_count.values())
    freq_keys = list(freq_count.keys())
    
    if freq_values[0] == 1 and freq_keys[0] == 1:
        return "YES"
    
    if freq_values[1] == 1 and freq_keys[1] == 1:
        return "YES"
    
    return "NO"    



s1 = "abc"
s2 = "abcc"
s3 = "heyyy"
s4 = "hey"

print(valid_string(s1))
print(valid_string(s2))
print(valid_string(s3))
print(valid_string(s4))
