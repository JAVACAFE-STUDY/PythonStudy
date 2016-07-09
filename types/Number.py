# coding=utf-8 ~

import sys
import os

#숫자형

#정수형(Integer) - 정수를 뜻하는 자료형
a = 123
a = -123
a = 0

#실수형(Floating point) - 소수점이 포함된 숫자
a = 1.2
a = -3.45

a = 4.24E10 #컴퓨터식 지수

#8진수와 16진수

a = 0O177
a = 0o244

a = 0x8ff

#복소수

a = 1+2j
b = 3-4J

print(a.real) #실수부
print(a.imag) #허수
print(a.conjugate()) #켤레복소수
print(abs(a)) #절대값
