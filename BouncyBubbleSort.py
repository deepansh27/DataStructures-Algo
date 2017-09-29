'''''''''
In standard bubble sort, the algorithm makes multiple passes through the list, swapping items so that the smaller value comes first and the larger value comes second.

Implement a "bouncing" bubble sort. In this version of bubble sort, instead of making passes through a list that starts at the beginning and runs through to the end, you should reverse the direction of each pass. That is, if the first pass starts at the beginning of the list and runs through to the end, the second pass would run from the end of the list back to the beginning, and then the third pass would start at the beginning again.

Assume items in the list are of the type integer.
'''''''''

def Bouncy_bubble_sort(list1):
    swap = 0
    left = 0
    right = 0
    print("List before sorting")
    print(list1)
    pass1 = 0
    swap_counter =0

    for i in range(0, len(list1)-1):
        if i%2==0: # to fasilitate forward and reverse sorting

            # forward sorting...
            for j in range(left,len(list1)-1-right):
                if list1[j] > list1[j+1]:
                    temp = list1[j]
                    list1[j] = list1[j+1]
                    list1[j+1] = temp
                    swap = 1
                    swap_counter +=1
            right += 1
        else:
            # reverse sorting...
            for j in range(len(list1)-1-right,left, -1):
                if list1[j] < list1[j-1]:
                    temp = list1[j-1]
                    list1[j-1]=list1[j]
                    list1[j]=temp
                    swap = 1
                    swap_counter += 1
            left += 1

        if swap ==0:
            break
        else:
            swap = 0


        pass1 += 1
        print(list1,pass1)





    print("list after sorting")
    print(list1)
    print("sorted in %d number of swaps"%swap_counter)





Bouncy_bubble_sort([2,6,4,2,7,2,9,10,3])

