#Task 1
# def quadrs(lst):
#     res = []
#     for n in lst:
#         res.append(n ** 2)
#     if type(lst) == tuple:
#         return tuple(res)
#     else:
#         return res
#
# print(quadrs([1,2,3]))

#Task 2
# def simm(s):
#     return len(s)%2 == 0
#
# print(simm('arbat'))

#Task 3
# def tridel(lst):
#     res = {}
#     for i in lst:
#         res.update([(i, i%3==0)])
#     return res
# print(tridel((3,7,12)))

#Task 4
# def chet_nechet(lst):
#     if len(lst)%2 == 0:
#         return list(filter(lambda x: x%2 == 0, lst))
#     else:
#         return list(filter(lambda x: x%2 != 0, lst))
# print(chet_nechet([3,7,12]))
#

#Task 5
# def separator(lst):
#     odd = []
#     even = []
#     for n in lst:
#         if n % 2 == 0:
#             even.append(n)
#         elif n % 2 != 0:
#             odd.append(n)
#     return sorted(odd) + sorted(even, reverse=True)
# print(separator([1,4,8,6,3,7,1]))

#Task 6
# def classificator(d):
#     res = {}
#     for i in d:
#         res.update({type(d[i]).__name__: res.get(type(d[i]).__name__, 0) + 1} )
#     return res
# print(classificator({'a': 1, 3: [1,5], 'e': 'abc', '6': []}))

#Task 8
# def courtage(tup):
#     new_tup = []
#     for i in range(0, len(tup), 2):
#         try:
#             new_tup.append((tup[i], tup[i+1]))
#         except:
#             #new_tup.append(tuple(tup[i],))
#             new_tup.append((tup[i],))
#     return new_tup
# print(courtage((1,4,8,6,3,7,1)))

#Task 9
def list_of_list(lst):
    res = []
    for i in lst:
        res += i

    return res
print(list_of_list([[1],[4,8],[6,3,7],[1,3]]))