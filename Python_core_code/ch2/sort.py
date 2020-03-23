
list =   [22,4,12,212,45,5,90,10,15,0,2]
list_1 = [90,42,1,9,100,37,15,10,2,12,5]
list_2 = [4,12,212,5,90,10,15,0,2,15,10,2,12,5,90,42,1,9,100,22]


# element = len(list)
# def interchange_sort(list):
    # print('\n','*'*20,'interchange_sort','*'*20)

#     list_test = list
#     print(list_test)
#     n  = len(list)
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if list_test[i] > list_test[j]:
#                 a = list_test[i]
#                 list_test[i] = list_test[j]
#                 list_test[j] = a
#     print(list_test)
# interchange_sort(list)

# def selection_sort(list):
#     print('*'*20,'selection_sort','*'*20)
#     n = len(list)
#     for i in range(0,n):
#         min_posi = i
#         for j in range(i+1,n):      #   [i+1,..,..,end]
#             if list[j] < list[min_posi]:
#                 min_posi = j
#         if i != min_posi:
#             temp = list[min_posi]
#             list[min_posi] = list[i]
#             list[i] = temp
#     return list
#
#
# print('sorted list: ',selection_sort(list),'\n')



# def insertion_sort(list):
#     n = len(list)
#     for i in range(1,n):
#         x = list[i]
#         posi = i
#         for j in range(0,i):        # find postion in sorted_list
#             if x < list[j]:
#                 posi = j
#                 break
#         # print('\n','x = ',x,'i = ',i,'posi = ',posi)
#         for k in range(i-1,posi,-1):  # [*****(i-1)](i)]  data(i) is saved in 'x'
#             list[k+1] = list[k]
#         list[posi] = x
#         # print('list_',i,list)
#     return list

# def insertion_sort(list):
#     n = len(list)
#     for i in range(1,n):
#         x = list[i]         #  consider element i _index list[i-1]
#         j = i-1
#         while j >= 0 and x < list[j]:
#             list[j+1] = list[j]     # move right to last_right = i = j+1
#             j-=1
#         list[j+1]  = x              # if x_least <-> j = 0 <-> first_elemnet
#     return list
# print('clear screen','\r')
# print('\n sorted list: ',insertion_sort(list_1))


# def selection_sort(list):
#     print('*'*20,'selection_sort','*'*20)
#     n = len(list)
#     for i in range(0,n):
#         min_posi = i
#         for j in range(i+1,n):      #   [i+1,..,..,end]
#             if list[j] < list[min_posi]:
#                 min_posi = j
#         if i != min_posi:
#             temp = list[min_posi]
#             list[min_posi] = list[i]
#             list[i] = temp
#     return list
# print('sorted list: ',selection_sort(list),'\n')


# def bubble_sort(list):
#     print('\n','origin_list: ','\ni =  ',list)
#     print('*'*20,'bubble_sort','*'*20)
#     n = len(list)
#     for i in range(0,n-1):
#         for j  in range(n-1,i,-1):
#             if list[j] < list[j-1]:
#                 temp = list[j]
#                 list[j] = list[j-1]
#                 list[j-1] =  temp
#         print('i = ',i,list,list[i],'list[n-1-i] = ',list[n-1-i])
#     return list


def quick_sort(list,left,right):
    # print('\n','origin_list: ','\ni =  ',list)
    # print('*'*20,'bubble_sort','*'*20)
    i = left
    j = right
    pivot = list[round((left+right)/2)]

    while i <= j:
        while list[i] < pivot:
            i+=1    # i=i[nearest_pivot_index]
        while list[j] > pivot:
            j-=1
        if i <= j:      # i,j is not over pivot ->swap
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            i+=1
            j-=1


    if i < right:
        quick_sort(list,i,right)
    if j > left:
        quick_sort(list,left,j)


quick_sort(list,0,len(list)-1)
print('sorted list: ',list,'\n')
