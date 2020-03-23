
lst  = [1,3,'a',1.35]
# List comprehension
squares = []
for i in range(1,101):
    squares.append(i**2)
# print(squares)

squares_2 = [i**2 for i in range(1,101)]
# print(squares)
remainder5 = [ i**2 % 5 for i in range(1,101) ]
remainder11 = [i**2 % 11 for i in range(1,101)]

def p_remainder(p):
    p_remainder = [i**2 % p for i in range(0,p)]
    return [len(p_remainder),p+1//2]

# print(p_remainder(100)) #
# print(remainder11)
listNames = ["William", "Keighley","Aline" ,"MacMahon","Guy" ,"Kibbee", "Drama",
"Warner", "Bros","Babes","Toyland,","Gus" ,"Meins","Stan art",'Google' ]

listNameAndYear = [
                        ("William",1991),("Keighley",1912),("Aline",1943),
                        ("MacMahon",1943),("Guy",1925),("Kibbee",1966),("Drama",1922),
                        ("Warner",1910),("Bros",1964),("Babes",1952),("Toyland",1942),
                        ("Gus",1990),("Meins",1914),("Stan art",1999)
                  ]

G_names = [ letter for letter in listNames if letter.startswith("G") ]
# print(G_names)
aYearNames = [(title,year) for (title,year) in listNameAndYear if year > 1955]
# print(aYearNames)

n = [1,4,5,3]
list_3_times = [4*i for i in n ]
# print(list_3_times)
A = [1,2,4,6]
B = [5,2,7]
cartesian_product = [(a,b,b) for a in A for b in B]
print(cartesian_product)
