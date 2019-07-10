li = input()
li = li.strip("',][")

if li.count("','"):
    li = li.split("','")
if li.count("', '"):    
    li = li.split("', '")



for i in range(len(li[0])):
    
    k = li[0][0:len(li[0])-i+1]
    count = 0
    for j in li:
        if k == j[0:len(li[0])-i+1]:
            count +=1

    if count == len(li):
        result = k
        break
    

print(result)
