#조건문
# if xxx : #xxx 자리에는 무조건 boolean 타입의 코드가 와야 한다.
#     yyy #if가 True면 yyy가 실행되고, False면 실행되지 않는다.


user_id = input('id?') #input은 입력받은 값을 데이터로 저장함->지금은 이를 user_input이라는 변수에 저장
user_pwd = input('password?')
'''
if user_input == '111111' : #숫자가 아니라 문자로 해야됨(계산X)
    print('Hello master')
else: #조건에 맞지 않다면?
    print('Who are you?')
'''
'''
if user_id == 'yuna':   
    if user_pwd == '111111':
        print('Hello master')
    else:
        print('Who are you?')
else:
    print('Who are you?')
'''

if user_id == 'yuna' and user_pwd == '111111':
    print('Hello master')
elif user_id == 'babo' and user_pwd == '222222':
    print('Hello master')
else:
    print('Who are you?')
