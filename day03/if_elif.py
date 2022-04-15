

age = int(input('나이: '))

if age >= 20:
    print('성인입니다')  # 시작은 if 부터 차례대로 실행해서 true면 밑에 조건은 실행하지 않음
elif age >= 17:          # if 부터 실행해서 False면 밑에 elif 조건을 실행함
    print('고딩입니다')  
elif age >= 14:
    print('중딩입니다')
elif age >= 8:
    print('초딩입니다')       
else:
    print('미취학 아동입니다')        


if age >= 20:
    print('성인입니다') # if 로 다 바꾸면 그룹이 4개가 되어서 그룹 하나, 하나 다 실행
if age >= 17:           # 나이에 25을 입력하면 성인, 고딩, 중딩, 초딩 다 출력 
    print('고딩입니다')  
if age >= 14:
    print('중딩입니다')
if age >= 8:
    print('초딩입니다')       
else:
    print('미취학 아동입니다')        


# 위에서부터 조건을 검색하면서 내려오기 때문에 범위조건일 경우 상위조건이 하위조건을 포괄적으로 포함하지 않도록 주의
# 예시
'''
if age >= 12:
    print('성인입니다')  
elif age >= 17:          
    print('고딩입니다')  
elif age >= 14:
    print('중딩입니다')
elif age >= 8:
    print('초딩입니다')       
else:
    print('미취학 아동입니다')        
'''

