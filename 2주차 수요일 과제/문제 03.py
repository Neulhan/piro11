import random

dwf_list = []

for i in range(1,10):
    dwf = int(input())
    dwf_list.append(dwf)

while True:
    dwf_check = dwf_list.copy()
    num = []
    ran_num = random.randint(0,8)

    for i in range(2):
        while ran_num in num:
            ran_num = random.randint(0,8)
        num.append(ran_num)

    dwf_check[num[0]:num[0]+1] = []
    dwf_check[num[1]:num[1]+1] = []

    if sum(dwf_check) == 100:
        result = sorted(dwf_check)
        break


for i in result:
    print(i)
    
    
        


