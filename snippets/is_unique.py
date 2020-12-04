def is_unique(l):
    return len(l) == len(set(l))


list1 = ["a", "b", "c", "a"]
list2 = ["a", "b", "c", "d"]

print(f"List: {list1}, Is Unique? {is_unique(list1)}")
print(f"List: {list2}, Is Unique? {is_unique(list2)}")
