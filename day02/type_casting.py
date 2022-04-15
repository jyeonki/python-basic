

n1 = 10
n2 = '34'

print(n1 + int(n2)) # 문자(정수)를 정수로 형변환
print(str(n1) + n2) # 정수를 문자로 형변환


# 문자열 내부값이 순수한 정수가 아닌 경우 변환 불가

s1 = 'hello'
# print(int(s1)) 불가능


s2 = '3.14'

# print(int(s2)) 불가능 
print(float(s2)) # 실수변환


f1 = 5.7
print(int(f1)) # 실수를 정수로 변환 - 정수만 남는다
# 2000원으로 600원짜리 과자를 몇 개 살 수 있을가? 3개 - 소수점 버리기

# 반올림 round()
print(round(f1))

f2 = 3.14159265
print(round(f2,4)) # 소수점 넷째자리까지 반올림
