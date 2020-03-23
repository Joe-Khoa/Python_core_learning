from clear_shell_automatically import *
list =   [22,4,12,212,45,5,90,10,15,0,2]
list_1 = [90,42,1,9,100,37,15,10,2,12,5]
list_2 = [4,12,212,5,90,10,15,0,2,15,10,2,12,5,90,42,1,9,100,22]

def swap(list,i,j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

# ********************  interchange_sort  ********************

# def sort(list,left,right):
#
#     print('origin list \n',list,'\n')
#     n = right
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if list[i] > list[j]:
#                 swap(list,i,j)  # swap list
#         # print('',list)
#     print('fee = $'+str(n*(n-1)) )


# ********************  selection_sort  ********************
#
# def sort(list,left,right):
#
#     print('origin list \n',list,'\n')
#     n = right
#     for i in range(0,n):
#         min_Po = i
#         for j in range(i+1,n):
#             if list[j] < list[min_Po]:
#                 min_Po = j
#         if min_Po != i:
#             swap(list,i,min_Po)
#
#     print('fee = $'+str(n*(n-1)) )



# ********************  insertion_sort  ********************

# def sort(list,left,right):
#
#     print('origin list \n',list,'\n')
#     n = right
#     for i in range(1,n):
#         x = list[i]
#         j = i-1
#         while j >= 0 and list[j] > x:
#             list[j+1] = list[j]     # ex: i = n; j = n-1; list[n] = x (SAVED)
#             j-=1                    ###_sorted_array_###<<--(j=i-1)(i)(n-1)(n
#         list[j+1] = x   # j+1 = i always_right
#     print('fee = $'+str(n*(n-1)) )

# ********************  bubble_sort  ********************

# def sort(list,left,right):
#     print('origin list \n',list,'\n')
#     n = right
    # for i in range(0,n):
    #     # print('last = ',list[n-i-1])
    #     for j in range(n-1,i,-1):
    #         if list[j] < list[j-1]:
    #             swap(list,j,j-1)
    #             # print('j = ',j)
    #     #     print(list)
    #     print('','i = ',i,list)
    # flag  = 1
    # i = 0
    # while flag:
    #     i+=1
    #     flag = 0
    #     for j in range(0,n-i):
    #          if list[j] > list[j+1]:    #   ********1   i take 1
    #              swap(list,j,j+1)       #   *******21   i take 12... i take n-j
    #              flag = 1       # this mean every loop must replace else -> DONE



# ********************  quick_sort  ********************


def sort(list,left,right):
    print('origin list \n',list,'\n')
    i = left
    j = right
    pivot = list[round((left+right)/2)]
    while i <= j:
        while list[i] < pivot:
            i+=1
        while list[j] > pivot:
            j-=1
            # now : *left*****ij*****right
        if  i <= j:     # this to swap i&j list[i&j]
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            i+=1
            j-=1
            # now : left*****ji*****right
    if j > left:
        sort(list,left,j)
    if i < right:
        sort(list,i,right)


    # print('fee = $'+str(n*(n-1)) )

sort(list,0,len(list)-1)
print('\n sorted list: \n',list,'\n')
