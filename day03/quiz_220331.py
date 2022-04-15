
# 백준 알고리즘
# - 조건문 1330

A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')   


'''
A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')  

'''




# - 조건문 9498    

score = int(input())

if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else:
    print('F')   


'''
score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F') 
'''              




# - 조건문 2753

leap_year = int(input())

if (leap_year % 4 == 0) and (leap_year % 100) != 0:
    print(1)
elif leap_year % 400 == 0:
    print(1)
else:
    print(0)        


''''   
if (leap_year % 4 == 0) and (leap_year % 100) != 0 or (leap_year % 400) == 0:
    print(1)
else:
    print(0)        
'''




# - 조건문 14681

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)     


'''
x = int(input())
y = int(input())

if x >= 0:        # if가 x보다 크거나 같고
    if y >= 0:
        print(1)
    else:
        print(4)                   
else:
    if y >= 0:
        print(2)
    else:
        print(3)    
'''




# - 조건문 2884

hour, minute = map(int, input().split())

# 분이 45분 이상일 경우 분에서 45를 뺀다
if minute >= 45:
    print(hour, minute-45)

# 분이 44분 이하이면서 시가 1시보다 크다면
# 45분을 제거할 경우 시침이 1시간 줄어들어야 하므로
# 시간은 1을 빼주고 분은 15를 더한다.
elif minute <= 44 and hour >= 1:
    print(hour-1, minute+15)

# 남은 경우의 수는 시간이 0이면서 분이 44분 이하인 
# 경우로 이럴 때는 23시로 돌아가야한다.
else:
    print(23, minute+15)




# - 조건문 2525

hour, minute = map(int, input().split())
long = int(input())


if minute >= 45:
    print(hour, minute-45)
elif minute <= 44 and hour >= 1:
    print(hour-1, minute+15)    
else:
    print(23, minute+15)

