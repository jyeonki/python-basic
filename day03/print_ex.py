
dog = '멍멍이'
cat = '야옹이'

print(dog, cat, '짹짹이') # 멍멍이 야옹이 짹짹이 출력
print(dog,cat,'짹짹이')  # 멍멍이야옹이짹짹이가 아닌 위랑 똑같이 출력

print(dog, cat, '짹짹이', sep='') # 멍멍이야옹이짹짹이
print(dog, cat, '짹짹이', sep=' ') # 멍멍이 야옹이 짹짹이
print(dog, cat, '짹짹이', sep='!') # 멍멍이!야옹이!짹짹이!

# sep은 구분자, 기본값은 공백 문자열




fruit = '딸기'
food = '짜장면'

print(fruit)
print(food)

print(fruit); print(food) # 같은 줄에 써도 food는 다음줄에 출력 
# 같은 줄에 쓸 때 ; 써주면 food는 다음줄에 출력

print(fruit + '\n\n\n\n') # \n 문자니까 '' 안에 넣어야함
print(fruit, end='\n') # 함수내부에 end='\n' 이 속성이 숨어있다(enter)
print(fruit, end='') # \n 지우면 엔터 삭제
print(fruit, end='메롱!\n')
print(food)

# end속성은 데이터  출력 이후 맨 끝에 포함할 문자를 지정