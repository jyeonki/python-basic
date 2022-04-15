
# 상품의 이름
product_name = input('상품명을 입력하세요: ')
# 상품의 가격
price = int(input('원가를 입력하세요: '))

# 할인가격
# discount = price - price * 0.1
discount = int(price - price * 0.1) # 소수점아래를 버리고 싶을 때 정수형으로 변환


# 메세지 출력
print(f'{product_name}의 할인가격은 {discount}원입니다.')
# 변수랑 문자랑 같이 출력을 하려면 {}에 변수를 입력


# ctrl + space 앞에 글자만 입력하면 쫙 뜬다  