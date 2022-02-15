# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def bubblesort(list):
    for item in range(len(list)-1,0,-1):
        for i in range(item):
            if list[i] > list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
    print(list)

def mergesort(list):
    if len(list) > 1 :
        left=list[ :len(list)//2]
        right=list[len(list)//2: ]

        mergesort(left)
        mergesort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j<len(right):
            if left[i] < right[j]:

                list[k] = left[i]
                i += 1
            else:
                list[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            list[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1

    return list

def insertionsort(list):
    idx_range=range(1,len(list))

    for idx in idx_range :
        value=list[idx]
        while list[idx-1] > value and idx > 0:
            list[idx],list[idx-1]= list[idx-1],list[idx]
            idx= idx -1

    return list



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list=[1,4,5,6,3,9]
    #bubblesort(list)
    #print(mergesort(list))
    #print(insertionsort(list))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
