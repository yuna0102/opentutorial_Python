#Number
print(1) #Integer

#String
print('Hello World')

#Boolean
print(True) #참
print(False) #거짓
# True = 1; #얘는 에러가 남-> 변수로 사용할 수 없음

#Expression
print(1+1) # +는 산술 연산자 : 좌변과 우변을 하나로 합침
print('Hello '+'world') # +는 결합 연산자(이항연산자) : 좌항과 우항을 하나로 만듦

#Comparison operator
print(1==1) #True
print(1<2) #True
print(2<1) #False

#Membership operator
print('World' in 'Hello World')  #in은 앞에 있는 값이 뒤에 속해있는가를 판단하는 연산자

import os.path #os라는 명령어들을 모아놓은 디렉토리 안에 있는 path를 가져온다
print(os.path.exists('boolean.py'))