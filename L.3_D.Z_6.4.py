def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [1, 1, 2, 2, 3, 3]

print(find_duplicates(lst))