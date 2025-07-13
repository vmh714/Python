import math
for x in range(2,101):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            break
    else:
        print(x)