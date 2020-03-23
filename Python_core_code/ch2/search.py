

list  = [1,2,3,4,5,6,7,8,9,10,100,1000]
list_2 = [2,4,12,42,85,90,120,125,150,180]

element = len(list)
def linear_search(x):
    for i in range(0,element):
        if list[i]  == x:
            print(i)
            return 'position '+str(i+1)
            # break
    return 'not found'

def binary_search(x):
    n = len(list_2)
    left = 1
    right = n
    # print('total: ',right)
    while left <= right:
        mid = round ((left+right)/2)
        print('middle = ',mid)
        if list_2[mid] == x:
            return 'position: '+str(mid+1)
            break
        if list_2[mid] > x:
            right = mid-1
        elif list_2[mid] < x:
            left = mid+1
    return 'not found!'





cont = 1
while cont:
    n = int(input('enter a digit:'))
    # fn = linear_search(n)
    fn = binary_search(n)

    print('result : ', fn)

    try:
        cont = int(input(' press 0 to exit '))
    except:
        exit()
