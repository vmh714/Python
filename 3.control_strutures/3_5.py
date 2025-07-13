input_str = 'Practice Makes Perfect'
chuoi_thuong = input_str.lower()
chuoi_dau_vao = chuoi_thuong.replace(" ","")
my_dict = {}
for i in range(len(chuoi_dau_vao)):
    if chuoi_dau_vao[i] in my_dict:
        my_dict[chuoi_dau_vao[i]] += 1
    else:
        my_dict[chuoi_dau_vao[i]] = 1
for x,y in my_dict.items():
    print(f"\'{x}\': {y}")