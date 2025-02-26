original = [1, 2, 3]
copy_list = original.copy()

print(copy_list)  # [1, 2, 3, [4, 5]]
copy_list.append(1) 

print(copy_list)
  # [1, 2, 3, [4, 5], 1]
print(original)

