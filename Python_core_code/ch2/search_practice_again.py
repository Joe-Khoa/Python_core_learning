

list  = [1,2,3,4,5,6,7,8,9,10,100,1000]
list_2 = [2,4,12,42,85,90,120,125,150,180]
list_unsorted = [120,125,150,2,4,12,42,85,2,3,4,5,6,90,180]

# def linear_search(list,x):
#     print('*'*20,' binary_search ','*'*20)
#     print(list)
#     flag = True
#     n = len(list)
#     i = 0
#     while flag and i < n:
#         if list[i] == x:
#             print('found ',x)
#             flag = False
#             return 'found'+ str(x)+' in index: '+str(i)
#         else:
#             i+=1
#     return

# def binary_search(x,list,left,right):
#     print('*'*20,' binary_search ','*'*20)
#     print(list)
#     mid = round((left + right)/2)
#     if left <= right:
#         if x == list[mid]:
#             return 'found: '+str(x)
#         elif x > list[mid]:
#             return binary_search(x,list,mid+1,right)    # exclude mid
#         elif x < list[mid]:
#             return binary_search(x,list,left,mid-1)
#     return 'not found!'


# cont = 1
# while cont:
#     n = int(input('enter a digit:  '))
#     fn = binary_search(n,list,0,len(list))
#     print('result : ', fn)
#     try:
#         cont = int(input(' press 0 to exit '))
#     except:
#         exit()
