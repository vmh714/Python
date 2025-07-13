import random
secret_number = random.randint(1,100)


while True:
    user_number = int(input("Hãy nhập số để dự đoán: "))
    if user_number == secret_number:
        print("Chúc mừng! Bạn đã đoán đúng")
        break
    elif user_number < secret_number:
        print("Số bạn đoán nhỏ quá!")
    else:
        print("Số bạn đoán lớn quá!")