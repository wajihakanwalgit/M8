my_set = {10, 20, 20, 30, 40, 40, 50}
print("Set :", my_set)

my_set.add(60)
print("Updated Set:", my_set)

set1 = my_set
set2 = {20, 30, 70, 80}

print("\nSet 1:", set1)
print("Set 2:", set2)

print("Difference:")
print(set1.difference(set2))

print("Symmetric Difference:")
print(set1.symmetric_difference(set2))
