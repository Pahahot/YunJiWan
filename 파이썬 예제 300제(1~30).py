#1. 화면에 Hello World 문자열을 출력하라
print("Hello World")

#2. 화면에 Mary's cosmetics을 출력하라. (중간에 '가 있음에 주의.)
print("Marry's cosmetics")
print('Marry\'s cosmetics')

#3. 화면에 [신씨가 소리질렀다. "도둑이야".] 문장을 출력하라. (중간에 "가 있음에 주의.)
print('신씨가 소리질렀다. "도둑이야".')
print("신씨가 소리질렀다. \"도둑이야\".")

#4. 화면에 "C:\Windows"를 출력하라.
print("C:\\\\Windows")

#5. [ print("안녕하세요.\n만나서\t\t반갑습니다.") ] 코드를 실행해보고 \t와 \n의 역할을 설명하라.
"""
\t : 4칸 띄어쓰기 or tab, \n : 개행
"""

#6. print 함수에 두 개의 단어를 입력한 예제이다. [ print ("오늘은", "일요일") ] 코드의 출력 결과를 예상하라.
print("오늘은","일요일")
""" '오늘은 일요일'이 출력된다. 문자열 사에를 ','로 연결하면 공백으로 연결된다."""

#7. print() 함수를 사용하여 [ naver;kakao;sk;samsung ]같이 출력하라. (힌트: sep=';')
print("naver","kakao","sk","samsung", sep=";")

#8. print() 함수를 사용하여 [ naver/kakao/sk/samsung ]다음과 같이 출력하라.
print("naver","kakao","sk","samsung", sep="/")

#9. [ print("first");print("second") ] 코드를 수정하여 줄바꿈이 없이 출력되도록 하라.
print("first",end='');print("second",end='')
""" end의 기능을 숙지하자. ;는 한줄에 여러 개의 명령어 작성을 위함이다. """

#10. string 문자열의 길이를 구하여라. string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(string))

#11. a = "3", b = "4", print(a+b)의 결과를 예상하라
""" 문자열 34가 출력 된다."""

#12. 변수 s = "hello"와 t = "python" 문자열이 바인딩 되어있다. 두 변수를 이용하여 [ hello! python ]으로 출력하라.
s = "hello"
t = "python"
print(s+"! "+t)

#13. [ print("Hi" * 3) ] 코드의 실행 결과를 예상하라.
""" HiHiHi """

#14. 화면에 '-'를 80개 출력하라.
print('-'*80)

#15. 변수에 t1 = 'python'과 t2 = 'java' 문자열이 바인딩되어 있다. 
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 
# [ python java python java python java python java ]로 출력하여라.
t1 = 'python'
t2 = 'java'
print((t1+" "+t2+" ")*4)

#16. LG전자 주식을 10주 보유하고 있습니다. 금일 종가 20,000원일 경우 총 평가 금액을 화면에 출력하라.
print(20000*10)

#17. [ 2 + 2 * 3 ] 코드의 실행 결과를 예측하라.
print(2+2*3)
""" 8이죠 """

#18. type() 함수는 데이터 타입을 판별합니다. 
# 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다. 
# 변수 b에 "132"를 바인딩했을 때, 값의 타입을 판별하라.
""" 문자열(str) """

#19. 문자열 '720'를 정수형으로 변환하라.
num = int('720')

#20. 정수 100을 문자열 '100'으로 변환하라.
num = str(100)

#21. python이 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하라.
s = 'python'
print(s[0], s[2])

#22. 자동차 번호가 "24가 2210" 일 때 뒤에 4자리만 출력하라.
car_num = "22가 2210"
print(car_num[-4:])

#23. "홀짝홀짝홀짝" 문자열에서 '홀' 만 출력하라.
str = "홀짝홀짝홀짝"
print(str[::2])

#24. "PYTHON" 문자열을 거꾸로 뒤집어 출력하라.
str2 = "PYTHON"
print(str2[::-1])

#25. "010-1111-2222" 전화번호에서 하이푼 ('-')을 제거하고 [ 010 1111 2222 ]와 같이출력하라.
phone_num = "010-1111-2222"
print(phone_num.replace('-',' '))
print(phone_num[0:3],phone_num[4:8],phone_num[9:13])

#26. 25번 문제의 전화번호를 [ 01011112222 ]와 같이 모두 붙여 출력하라.
print(phone_num.replace('-',''))
print(phone_num[0:3]+phone_num[4:8]+phone_num[9:13])

#27. [ url = "http://sharebook.kr" ] url에 저장된 웹 페이지 주소에서 도메인(kr)을 출력하라.
url = "http://sharebook.kr"
print(url[-2:])

#28. 아래 코드의 실행 결과를 예상하라
# lang = 'python', lang[0] = 'P', print(lang)
""" 오류난다. 기존의 생성한 문자열은 변경할 수 없다 """

#29. 'abcdfe2a354a32a' 문자열에서 소문자 'a'를 대문자 'A'로 변경하라.
str = 'abcdfe2a354a32a'
print(str.replace('a','A'))

#30. 아래 코드의 실행 결과를 예측하라.
#string = 'abcd', string.replace('b','B'), print(string)
""" 'abcd'가 출력된다.
29, 30에서 확인할 수 있는 replace의 쓰임은
replace는 기존의 문자열을 변경해주는 것이 아니라 새로운 문자열을 반환해주는 것이다.
"""





















