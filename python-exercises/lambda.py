#Square
my_lst = [1,2,3]
print(list(map(lambda item: item ** 2, my_lst)))

#List Sorting
a = [(0,2), (4,3), (9,9), (10,-1)]
print(sorted(a, key=lambda x: x[1]))