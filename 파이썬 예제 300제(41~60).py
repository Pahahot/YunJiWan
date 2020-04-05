# 41. 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 
# 영화 제목을 movie_rank 이름의 리스트에 저장하라. (순위 정보는 저장하지 않는다.)
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

#42. 41의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append('배트맨')
print(movie_rank)

#43. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. 
# "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

#44. movie_rank 리스트에서 '럭키'를 삭제하라.
del movie_rank[3]
""" 방법2  movie_rank.remove('럭키') """

#45. movie_rank 리스트에서 '스플릿' 과 '배트맨'을 삭제하라.
del movie_rank[2:]
""" 
방법2  
movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
"""
print(movie_rank)

#46. lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C","C++","JAVA"]
lang2 = ["Python","Go","C#"]
langs = lang1+lang2
print(langs)

#47. 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1,2,3,4,5,6,7]
print("max : ", max(nums))
print("min : ", min(nums))

#48. 다음 리스트의 합을 출력하라.
nums = [1,2,3,4,5]
print(sum(nums))

#49. 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#50. 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums))

#51. price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라.
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#52. 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])

#53. 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])

#54. 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1,2,3,4,5]
print(nums[::-1])

#55. interest 리스트에는 아래의 데이터가 바인딩되어 있다. interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

#56. interest 리스트에는 아래의 데이터가 바인딩되어 있다. interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#방법1
print(interest[0], interest[1], interest[2], interest[3], interest[4])
#방법2
print(' '.join(interest))

#57. interest 리스트에는 아래의 데이터가 바인딩되어 있다. interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#방법1
print(interest[0], interest[1], interest[2], interest[3], interest[4], sep='/')
#방법2
print('/'.join(interest))

#58. interest 리스트에는 아래의 데이터가 바인딩되어 있다. join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
print('\n'.join(interest))

#59. 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다. 이를 interest 이름의 리스트로 분리 저장하라.
string = "삼성전자/LG전자/Naver"
interest = [string[0:4],string[5:9],string[10:15]]
print(interest)

#60. 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.(힌트 : split() 메서드)
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest = string.split("/")
print(interest)






