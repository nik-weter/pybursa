# -*- utf8 -*-
import copy


#Task 1
#s = "ambulance"

#result = s[::-1]

# result = ''
# i = len(s) - 1
# while i >= 0:
#     result = result+s[i]
#     i -= 1

# lst = []
# result = ''
# for n,letter in enumerate(s):
#     lst.append((n,letter))
# lst.sort(reverse=True)
# for i in lst:
#     result += i[1]
#
# result = ''
# for i in range(1,len(s)+1):
#     i = -i
#     result += s[i]
#
#
# print(result)

#Task 2
# lst = ['a', 'e', 'i', 'o', 'u']
# count = 0
# s = input("Enter string: ")
# for i in s.lower():
#     if i in lst:
#         count += 1
# print(count)

#Task 3
# lst = 'wow'
# count = 0
# s = input("Enter string: ")
# while True:
#     if lst in s:
#         count += 1
#         s = s[s.find(lst)+1:]
#     else:
#         break
# print(count)

#Task 4
# s = input("Enter string: ")
# s = list(s)
#
#
# max_sub = []
# while True:
#     sub = []
#     for i in s:
#         sub.append(i)
#         if sub == sorted(sub):
#             if len(max_sub) < len(sub):
#                 max_sub = copy.copy(sub)
#         else:
#             s.pop(0)
#             break
#     if len(s) <= 1:
#         break
# for i in max_sub:
#     print(i, end='')

#Task 5
# def typer(i):
#     print(str(type(i).__name__))
#
# typer(typer)

#Task 6
# a = input("Enter A: ")
# b = input("Enter B: ")
# if (a.isalpha()) or (b.isalpha()):
#     print("Получена строка!")
# elif a > b:
#     print("bigger")
# elif a == b:
#     print("equal")
# elif a < b:
#     print("smaller")

#Task 7
# def unique_ordered(lst):
#     s = []
#     for i in lst:
#         if i not in s:
#             s.append(i)
#     return s
# def unique_disordered(lst):
#     d  = {}
#     for i in lst:
#         d.update([(i, "yes")])
#     return d.keys()
#
# print(unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) == ["a", 5, 2, (1, "a")])
# print(unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]))

#Task 8
# t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')
# t2 = []
# for i in range(0, len(t), 3):
#     t2.append(t[i-1])
# t2.pop(0)
#
# print(tuple(t2))

#Task 9
def f(x, y, z):
    return min(max(x,y),z)
print(f(3,2,1))
