#91. 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
"""
boolean 타입 / 불타입
"""

#92. 아래 코드의 출력 결과를 예상하라
print(3==5)
""" False """

#93. 아래 코드의 출력 결과를 예상하라
print(3<5)
""" True """

#94. 아래 코드의 출력 결과를 예상하라.
x = 4
print(1<x<5)
""" True """

#95. 아래 코드의 출력 결과를 예상하라
print((3==3) and (4!=3))
""" True """

#96. 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
"""
print(3=>4)
: 크거나 같음, 작거나 같음 조건은 부등호가 =보다 앞에 나온다.
"""

#97. 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World")
"""
if 조건을 만족하지 못하므로 아무것도 출력되지 않는다.
"""

#98. 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World")
else :
    print("Hi, there.")

"""
Hi, there가 출력
"""

#99. 아래 코드의 출력 결과를 예상하라
if True:
    print("1")
    print("2")
else :
    print("3")
print("4")

"""
1
2
4
"""
print(' ')


#100. 아래 코드의 출력 결과를 예상하라
if True :
    if False: 
        print("1")
        print("2") 
    else: 
        print("3") 
else : 
    print("4") 
print("5")

"""
3
5
"""


#101. 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
string = input()
print(string*2)


#102. 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
num = input('숫자를 입력하세요')
print(int(num)+10)


#103. 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
num = int(input())
if num%2==0:
    print("짝수")
else:
    print("홀수")


#104. 사용자로부터 값을 입력받은 후 해당 값에 +20을 더한 값을 출력하라. 
# 단 값의 범위는 0~255로 가정한다. 255를 초과하는 경우 255를 출력해야 한다.
num = int(input('입력값:')) + 20
if 0 < num < 255:
    print('출력값:', num)
else:
    print('출력값:', 255)


#105. 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 
# 단 값의 범위는 0~255이다. 0보다 작은 값이되는 경우 0을 출력해야 한다.
num = int(input('입력값:')) - 20
if 0 < num < 255:
    print('출력값:', num)
else:
    print('출력값:', 0)


#106. 사용자로부터 입력받은 시간이 정각인지 판별하라.
time = input("현재시간:")
minute = time[3:]
if minute == '00':
    print("정각입니다.")
else:
    print("정각이 아닙니다.")


#107. 사용자로부터 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = ["사과","포도","홍시"]
love_fruit = input("좋아하는 과일은?")

if love_fruit in fruit:
    print("정답입니다.")
else :
    print("오답입니다.")


#108. 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 
# 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 
# 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
in_investment = input('종목명:')
if in_investment in warn_investment_list:
    print("투자 경고 종목입니다.")
else :
    print("투자 경고 종목이 아닙니다.")


#109. 아래와 같이 fruit 딕셔너리가 정의되어 있다. 
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
key = input("키를 입력하세요:")
if key in fruit.keys() :
    print("정답입니다.")
else :
    print("오답입니다.")

#110. 아래와 같이 fruit 딕셔너리가 정의되어 있다. 
# 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
value = input("값을 입력하세요:")
if value in fruit.values() :
    print("정답입니다.")
else :
    print("오답입니다.")


