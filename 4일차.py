# shelf={3:"강호동", 25:"이수근"}
# print(shelf[3])
# print(shelf.get(25))
# print(shelf.get(68,"enable"))
# print(68 in shelf)

# shelf[25]= "차태현"
# shelf[3]= "류현진"
# shelf["A"]= "강정호"
# print(shelf)

# del shelf[3]
# print(shelf)
# print(shelf.keys())
# print(shelf.items())
# print(shelf.values())

# shelf.clear
# print(shelf)

# (A,B,C)= ("짬뽕", "삼선짬뽕", "홍합짬뽕")
# print(A,B,C)

# java={1,2,3}
# python={2,3,6}

# print(java & python)
# print(java | python)
# print(java. intersection(python))
# print(python. union(java))

# print(java - python)
# print(java. difference(python))

# python.add(1)
# print(python)

# java.remove(2)
# print(java)

dish={"짬뽕", "삼선짬뽕", "홍합짬뽕"}
print(dish,type(dish))
dish=list(dish)
print(dish,type(dish))
dish=tuple(dish)
print(dish,type(dish))

dish=set(dish)
print(dish,type(dish))