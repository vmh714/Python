for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print(f"{i} FizzBuzz")
    elif not i % 3:
        print(f"{i} Fizz")
    elif not i % 5:
        print(f"{i} Buzz")
    else:
        print(i)
        