
# 논리 연산자
# and 는 로그인을 생각하면 편함, 양쪽 항이 모두 True 인 경우

T = True
F = False

print(T and T) # alt + shift + 아래방향키(밑으로 복사)
print(T and F)
print(F and T)
print(F and F)

print('=====================')

print(T or T) # alt + shift + 아래방향키(밑으로 복사)
print(T or F)
print(F or T)
print(F or F)

print('=====================')

a = 5

if (a > 1) and (a < 10):
    print('a는 1과 10사이의 정수입니다!')
else:
    print('a는 범위 안의 정수가 아닙니다.')     

    
print('=====================')

b = 3

if (b == 2) or (b == 4):
    print('b는 2 또는 4입니다.')
else:     
    print('b는 2 또는 4가 아닙니다.')   