def inter(list):
    count = len(list)
    for i in range(1,count):
        temp = list[i]
        j = i - 1
        while(j>=0 and temp<list[j]):
            list[j+1] = list[j]
            j -=1
        list[j+1] = temp
    return list


def maopao(list):
    count = len(list)
    for i in range(count-1):
        flog = 0
        for j in range(count-i-1):
            if list[j+1]< list[j]:
                list[j+1],list[j] = list[j],list[j+1]
                flog = 1
        while flog == 0:
            return list
def quick(list,left,right):
    if left>=right:
        return list
    i = left
    j = right - 1
    temp = list[left]
    while i<j:
        while i<j and temp < list[j]:
            j-=1
        list[i] = list[j]
        i+=1
        while i<j and temp > list[i]:
            i+=i
        list[j] = list[i]
        j-=1
    list[i] = temp
    quick(list,left,i-1)
    quick(list,i+1,right)
    return list

def xier(list):
    count = len(list)
    group = 2
    step = int(count/group)

    while step>0:
        for i in range(step):
            k = i+step
            while k<count:
                i = k-step
                temp = list[k]
                while i>=0 and temp<list[i]:
                    list[i+step] = list[i]
                    i -=step
                list[i+step] = temp
                k += step
        step = int(step/2)
    return list

def select(list):
    count = len(list)
    for i in range(count):
        min = list[i]
        num = i
        for j in range(i+1,count):
            if list[j]<min:
                min = list[j]
                num = j
        list[i],list[num] = list[num],list[i]
    return list

def adjuct_dui(list, i, size):
    lchild = 2*i+1
    rchild = 2*i+2
    father = i
    mam = lchild
    if father < int(size/2):
        if rchild<size and list[rchild] > list[lchild]:
            mam = rchild
        if list[father] > list[mam]:
            mam = father
        if mam != father :
            list[father],list[mam] = list[mam],list[father]
            adjuct_dui(list,mam,size)

def bulid_dui(list, size):
    for i in range(int(size/2))[::-1]:
        adjuct_dui(list,i,size)

def dui(list):
    size = len(list)
    bulid_dui(list,size)
    for i in range(size)[::-1]:
        list[0],list[i]=list[i],list[0]
        adjuct_dui(list,0,i)
    return list

def splica(list):
    if len(list)<=1:
        return list
    num = int(len(list)/2)
    left = splica(list[:num])
    right = splica(list[num:])
    return merget(left,right)

def merget(left,right):
    i = 0
    j = 0
    result = []
    while i<len(left) and j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

s = [2,1,8,3,6,5,0]
m = [1,2,3,4,5]
a = splica(s)
print(a)
c = range(0,4)[::-1]
