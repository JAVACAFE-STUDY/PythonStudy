import sys
import os

"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

head = "Python"
tail = " is fun!"
print(head + tail)

a = "Python"
print(a * 3)

a = "Life is too short."

print(a[1])
print(a[-1])
print(a[-0]) # a[0]

print(a[1:3]) #문자열 슬라이싱
print(a[12:])
print(a[:17])

# Format 함수 사용

age = 20
name = 'Swaroop'

print('I eat %d %s' % (3, "apples"))
print('%s was %s years old when he wrote this book' %(name, age))

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# 사용자 지정 키워드를 이용해 (Swaroop wrote A Byte of Python) 표기
print('{name} wrote {book}'.format(name='Swaroop',
                                   book='A Byte of Python'))

#정렬과 공백
print('%10s' % "hi")
print('{0:<10}'.format("hi"))
print("%-10sjane." % 'hi')
print('{0:>10}'.format("hi"))
print('{0:^10}'.format("hi"))
# 밑줄(_)로 11칸을 채우고 가운데 정렬(^)하기 (___hello___)
print('{0:_^11}'.format('hello'))

#{ } 문자 표현하기
print('{{ and }}'.format())

# 소수점 이하 셋째 자리까지 부동 소숫점 숫자 표기 (0.333)
print('{0:.3f}'.format(1.0/3))
#소수점 네자리만 표시하기
print("%0.4f" % 3.42134234)
#소수점 네자리만 표시하고 왼쪽 정렬하기
print("%10.4f" % 3.42134234)

#문자열 함수
a = "hobby"
print(a.count('b')) #b의 문자 개수

print(a.find('b')) #가장 처음 나온 b의 위치
print(a.find('k')) #없는 값인 경우

print(a.index('o')) #o의 위치
#print(a.index('k')) #k의 위치

a = ','
print(a.join('abcd'))

a = "hi"
b = a.upper()
print(a.upper())
print(b.lower())

c = "  'hi'  "
print(c.lstrip()) #왼쪽
print(c.rstrip()) #오른쪽
print(c.strip()) #양쪽

a = "Life is too short"
print(a.replace("Life", "Your leg"))

a = "Life  is too short"
print(a.split())  #['Life', 'is', 'too', 'short']
a = "a:b:c:d"
print(a.split(':'))  #['a', 'b', 'c', 'd']





