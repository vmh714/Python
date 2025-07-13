input_list = [0, 1, "hello", "", None, [], [1, 2], False, True, {"key": "value"}, {}]
my_list = [x for x in input_list if x]
for i in my_list:
    print(i)