
# 백준 알고리즘 
# - 입출력과 사칙연산 13단계 2588번

# a = int(input())
# b = int(input())


# print(a * (b % 10))
# print(a * ((b // 10) % 10))# 식은 다르나 같은 값
# print(a * ((b % 100) // 10))# 식은 다르나 같은 값
# print(a * (b // 100))
# print(a * b)


# c = (a * (b % 10))
# d = (a * ((b // 10) % 10))
# e = (a * (b // 100))
# f = (a * b)



# a = int(input())
# b = int(input())
 
# c = (a * (b // 10 ** 0 % 10))
# d = (a * (b // 10 ** 1 % 10))
# e = (a * (b // 10 ** 2))
# f = (c * 10 ** 0) + (d * 10 ** 1) + (e * 10 ** 2)
# print(c)
# print(d)
# print(e)
# print(f)





A = int(input())
B = int(input())

C = A * (B // 10 ** 0 % 10)
print(C)

D = A * (B // 10 ** 1 % 10)
print(D)

E = A * (B // 10 ** 2 )
E2 = A * (B // 10 ** 2 % 10)
print(E)
print(E2)

F = (C * 10 ** 0) + (D * 10 ** 1) + (E * 10 ** 2)
print(F)





# E와 E2의 닶이 같은 이유가 뭘까?

A = int(input())
B = int(input())


E = A * (B // 10 ** 2 )
E2 = A * (B // 10 ** 2 % 10)
E3 = B // 10
E4 = B // 10 ** 2
E5 = 10 ** 2 % 10
E6 = B // 10 ** 2 % 10
E7 = B // 100 % 10
E8 = 3 % 10

print(E)
print(E2)
print(E3)
print(E4)
print(E5)
print(E6)
print(E7)
print(E8)

# 3 / 10 은 왜 나머지 값이 3일까?