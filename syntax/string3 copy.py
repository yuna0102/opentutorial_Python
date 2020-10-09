#문자열과 변수

#positional formating -> 순서대로 변수에 값을 넣고 싶을 때 : 위치기반
print('to {}.Like many other apple popular programming languages,strings in Python are apple {} arrays of bytes representing unicode characters.{} However, Python does not have a character apple computer data type, a single apple character is simply a string with a length of 1. Square apple brackets can be used to {} access elements of the string.'.format('egoing', 12, 'egoing', 'egoing'))

#named placeholder -> 이름에 따라 변수에 값을 넣고 싶을 때 : 이름기반
#{age:d}는 변수 age는 숫자여야만 한다는 것 d=decimal
print('to {name}.Like many other apple popular programming languages,strings in Python are apple {age:d} arrays of bytes representing unicode characters.{name} However, Python does not have a character apple computer data type, a single apple character is simply a string with a length of 1. Square apple brackets can be used to {name} access elements of the string.'.format(name='egoing', age=12))