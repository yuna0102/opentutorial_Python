s = [1, 'four', 9, 16, 25] #각각의 요소는 element라 부른다.
print(s)
print(s[0]) #[]안에 적는 것은 index다.
print(len(s))
s[1]=4 #기존의 1번째 칸에 있던 데이터를 4로 바꿔라 >> 갱신
print(s)
del s[2] #2번째 칸에 있던 데이터를 지우고 앞으로 땡김
print(s)
s.append('yuna') #list의 마지막에 element 추가
print(s)

#dictionary
person = {'name':'egoing', 'address':'seoul', 'age':'20'} #person이라는 개념(변수)에 이름은 egoing, 주소는 seoul 이런 식으로 정의해주고 원하는 것을 가져오는 것임.
print(person['name'])