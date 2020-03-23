

#   Factorial

# def factorial(n):
#     if  n == 0 :
#         return 1
#     else:
#         return n*factorial(n-1)


# def fibonaci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonaci(n-1)+fibonaci(n-2)

# def recursion_greater_6(n):
#     if n < 6:
#         return n
#     else:
#         sum = 0
#         for i in range(1,6):
#             sum+=recursion_greater_6(n-i)
#         return sum

#
# def indirect_recursion_A(n):
#     if n == 1:
#         return 1
#     else:
#         return indirect_recursion__B(n-1)*n
# def indirect_recursion__B(n):
#     if n == 1:
#         return n
#     else:
#         return indirect_recursion_A(n-1)*n
# def indirect_recursion_total(n):
#     return indirect_recursion_A(n)+indirect_recursion__B(n)

#************************ Ch2_task_1 **********************
def task_1(n):
    if n == 1:
        return 1
    else:
        return task_1(n-1)+n

list  = [12,3,32,2,31,10,39,0,7,76]

def task_2(n):
    min = 0
    if n == 0:
        return list[min]
    else:
        for i in range(1,n):
            if list[i] < list[min]:
                min = i
        return list[min]

def task_3(n):


if __name__ =='__main__':
    cont = 1
    while cont:
        n  = int(input('enter n = '))
        # fn = factorial(n)
        # fn = fibonaci(int(n))
        # fn = recursion_greater_6(int(n))
        # fn = indirect_recursion_total(n)
        fn = task_2(n)
        print('func_res = ',fn)
        try:
            cont = int(input('press 0 or not_number_digit to exit: \t'))
        except:
            print('exit already!')
            exit()
