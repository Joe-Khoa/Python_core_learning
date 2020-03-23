
# print(sum([1,2,3]))
def not_use_generator():
    numbers = list()
    for i in range(1000):
        numbers.append(i)
    # print(numbers)
    # total = sum(numbers)
    # print(total)

# not_use_generator()

def generate_number(n):
    num = 0
    while num < n:
        yield num
        num+=1
print(list(generate_number(1000)))
# total = sum(generate_number(1000))
# print(total)
