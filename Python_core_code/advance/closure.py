# https://quantrimang.com/python
"""
use Closure in Python
Ví dụ: Hàm lồng nhau truy cập biến nonlocal : msg
"""

def print_msg(msg):
 # Hàm bên ngoài

     def printer():
 # Hàm lồng nhau
         print(msg)

     printer()

 # Chạy hàm
 # Output: Hello
 print_msg("Hello")

"""
Định nghĩa hàm Closure trong Python
Closure thường được tạo ra bởi hàm lồng nhau, có thể hiểu là những hàm ghi nhớ không gian nơi mà nó tạo ra.
"""
def print_msg(msg):
 # Hàm bê ngoài

     def printer():
 # Hàm lồng nhau
         print(msg)

     return printer

 another = print_msg("Hello")
 another()

# Khi nào nên sử dụng Closure?
"""
Khi cần định nghĩa một class chỉ với vài phương thức,
closure có thể được sử dụng như một giải pháp thay thế
 nhẹ nhàng hơn lập trình hướng đối tượng.
Tuy nhiên là khi các thuộc tính và phương thức nhiều lên,
 sử dụng lập trình hướng đối tượng sẽ là giải pháp tốt hơn.
"""
def make_multiplier_of(n):
     def multiplier(x):
         return x * n
     return multiplier

 # He so 3
 times3 = make_multiplier_of(3)

 # He so 5
 times5 = make_multiplier_of(5)

 # Output: 27
 print(times3(9))

 # Output: 15
 print(times5(3))

 # Output: 30
 print(times5(times3(2)))
