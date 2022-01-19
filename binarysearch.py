#binary search questions
def cieling_of_number(list1,target):
    start = 0
    end = len(list1)-1
    while(start<=end):
        mid = (start + end)//2

        if(list1[mid] == target):
             return list1[mid]
        elif (list1[mid]<target):
            start = mid +1
        elif(list1[mid]>target):
            end = mid-1
        print(list1[start:end+1])
    return list1[start]  
def binary_search(list1,target):
    start = 0
    end = len(list1)-1
    while(start<=end):
        mid = (start + end)//2

        if(list1[mid] == target):
             return list1[mid]
        elif (list1[mid]<target):
            start = mid +1
        elif(list1[mid]>target):
            end = mid-1
        print(list1[start:end+1])
    return -1
def floor_of_number(list1,target):
    start = 0
    end = len(list1)-1
    while(start<=end):
        mid = (start + end)//2

        if(list1[mid] == target):
             return list1[mid]
        elif (list1[mid]<target):
            start = mid +1
        elif(list1[mid]>target):
            end = mid-1
        print(list1[start:end+1])
    return list1[end]

print(floor_of_number([12,13,17,18,24],15))