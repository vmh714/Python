#YC1
numbers = [1, 2, 3, 4, 5, 6]
square_list = [x*x for x in numbers if not x%2]
[print(x) for x in square_list]

#YC2
words = ["apple", "banana", "cherry", "date"]
new_words = [x for x in words if len(x) > 5]
[print(x) for x in new_words]
#YC3
my_list = [x for x in range(2,51) if not x%15]
[print(x) for x in my_list]