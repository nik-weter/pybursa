# -*- utf8 -*-

# lst = ['a', 'e', 'i', 'o', 'u']
# count = 0
# s = input("Enter string: ")
# for i in s.lower():
#     if i in lst:
#         count += 1
# print(count)
#

def sliced(string):
    return string[::-1]

def list_reverse(string):
    lst = list(string)
    lst.reverse()
    return "".join(lst)

def reversed(string):
    return "".join(reversed(list(string)))

def manual_reversed(string):
    result = []
    for letter in string:
        result.insert(0, letter)
