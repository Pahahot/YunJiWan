#61. 다음 코드의 결과값에 대해 예측하여라.
interest_0 = ['삼성전자','LG전자','SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
print(interest_0)

print(id(interest_0))
print(id(interest_1))
"""
interest_1에 interest_0을 대입하면 리스트가 복사되는 것이 아닌
주소를 공유하여 동일한 리스트를 가리키게 된다.
따라서 interest_1을 수정하면 interest_0의 내용도 수정된다.
"""

#62 다음 코드의 결과값에 대해 예측하여라.
interest_0 = ['삼성전자','LG전자','SK Hynix']
interest_1 = interest_0[:2]
interest_1[0] = 'Naver'
print(interest_0)
"""
리스트의 슬라이싱은 리스트를 복사 생성한다.
"""

#63. my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()

#64. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
t = (1,2,3)
#t[0] = 'a'
"""
튜플은 속성 값을 변경할 수 없다.
"""

#65. 숫자 1이 저장된 튜플을 생성하라.
t = (1,)
print(t)
"""
튜플은 요소를 한개만 가질 때 요소 뒤에 (,)를 반드시 붙여야 한다.
"""

#66. 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1,2,3,4
"""
튜플은 괄호를 생략하여 정의 할 수 있다.
"""

#67. 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a','b','c')
t = ('A','b','c')
print(t)

#68. 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자','LG전자','SK Hynix')
data = list(interest)
print(data)

#69. 다음 리스트를 튜플로 변환하라.
interest = ['삼성전자','LG전자','SK Hynix']
data = tuple(interest)
print(data)

#70. 아래 코드의 실행 결과를 예측하라.
my_tuple = (1,2,3)
a,b,c = my_tuple
print(a+b+c)

#71. 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 
# 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 
# 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 
# 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
a,b,*c = (0,1,2,3,4,5)
print(a)
print(b)
print(c)
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, 
# start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,b = scores
print(valid_score)

#72. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, 
# start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,b,*valid_score = scores
print(valid_score)

#73. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, 
# start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,*valid_score,b = scores
print(valid_score)

#74. temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}

#75. 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
icecream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(icecream)

#76. 75 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500
print(icecream)

#77. 76에서 만든 딕셔너리를 사용하여 메로나 가격을 출력하라.
print('메로나 가격:',icecream.get('메로나'))
print('메로나 가격:',icecream['메로나'])

#78. 77에서 만든 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
icecream['메로나'] = 1300
print(icecream)

#79. 78에서 만든 딕셔너리에 메로나를 삭제하라.
#방법1
del icecream['메로나']
print(icecream)

#방법2
"""
icecream.pop('메로나')
print(icecream)
"""

#80. 다음 코드에서 에러가 발생한 원인을 설명하라.
"""
icecream['누가바']
누가바라는 키값이 존재하기 않기 때문에 에러가 발생한다.
"""

#81. 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 
# 딕셔너리의 이름은 inventory로 한다.

inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print(inventory)

#82. 81의 inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
print(inventory['메로나'][0],'원')

#83. 81의 inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
print(inventory['메로나'][1],'개')

#84. 81의 inventory 딕셔너리에 아래 데이터를 추가하라.
inventory['월드콘'] = [500,7]
print(inventory)

#85. 다음의 딕셔너리에서 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
list_key = list(icecream.keys())
print(list_key)

#86. 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
list_value = list(icecream.values())
print(list_value)

#87. icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
print(sum(list_value))

#88. 아래의 new_product 딕셔너리를 87번의 icecream 딕셔너리에 추가하라.
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)
"""
icecream['팥빙수'] = 2700
icecream['아맛나'] = 1000 이렇게 할수도 있지만
update를 활용하면 한번에 딕셔너리를 추가할 수 있다.
"""

#89. 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. 
# keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
keys = ('apple','pear','peach')
vals = (300, 250, 400)

result = dict(zip(keys,vals))
print(result)
"""
zip 메서드는 두개의 자료구조를 하나로 묶어준다
"""

#90. data와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date,close_price))
print(close_table)
