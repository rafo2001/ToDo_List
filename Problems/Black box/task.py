# use the function blackbox(lst) that is already defined
list1 = [1, 2, 3]
list2 = blackbox(list1)
if id(list1) == id(list2):
    print("modifies")
else:
    print("new")