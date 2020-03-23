# fatorial n!  = 1.2.3...n test_4:24

# def factiorial (n):
#     if n==0:
#         return 1
#     else:
#         return n*factiorial(n-1)


"""
     fibonaci f1 = 0, f1 = 1, fn = f(1)+F(2)+...+f(n-1)
     (same factiorial_but ADD not PLUS and FUCTION f(n-1) NOT value)
     test 10:55
"""
# def fibonaci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     # elif n == 2:
#     #     return 0+1
#     # elif n == 3:
#     #     return 1 + 1
#     # ...
#     else:
#         return fibonaci(n-1) + fibonaci(n-2)


""" find Un = {
                    n : n < 6
                    Un-5 + Un-4 + Un-3 + Un-2 + Un-1 : n >= 6
                    test_6:15
            }
"""
# def sum_Un_less_than_6(n):
#     if n < 6:
#         return n
#     else:
#         return sum_Un_less_than_6(n-5)+sum_Un_less_than_6(n-4)+sum_Un_less_than_6(n-3)+sum_Un_less_than_6(n-2)+sum_Un_less_than_6(n-1)


# ******************************* TAIL_RECURSION   *******************************
# recursion_func_command => last_recursion

def tail_recursion_fatorial(n):
    if n == 0:
        return 1
    return tail_recursion_fatorial_i_(n,1)


def tail_recursion_fatorial_i_(n,result):
    if n == 1:
        return result
    return tail_recursion_fatorial_i_(n-1,result*n)
    """
        when n=2 =>cal_fn: tail_recursion_fatorial_i_(1,result*1) = last_command
    """

x = input('enter n :')
f = tail_recursion_fatorial(int(x))
print(f)
# print(1, 2, 3, 4, sep='*')
