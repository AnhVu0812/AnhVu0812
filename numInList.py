def inputList(num):
    list = []
    for i in range(num):
        print(f"nhap phan tu thu {i+1}", end=':')
        list.append(int(input()))
        # print(list)
    return list

def countNum(mylist):
    count = 0
    for num in mylist:
        if num > 10:
            count +=1
    return count

num = int(input("nhap vao so phan tu:"))
mylist = inputList(num)
print(f"co {countNum(mylist)} so trong list > 10")