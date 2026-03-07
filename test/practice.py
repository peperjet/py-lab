
a=10
b=3
print(a+b)

print(a+b, a-b, a*b, a/b)

#파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열
list : 리스트
tuyple : 튜플
set : 집합
dict : 사전
"""

#데이터 타입
str1="Python"
bool="True" 
str2='Anaconda'
num_float=10.0
num_int=7
list=[str1, str2]

dict={
    "name":"Machine Learning",
      "version":2.0
}
tuple=7,8,9
set={3,5,7}


#데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(num_float))
print(type(num_int))
print(type(dict))



#숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) x**y -> 2**3
round(x) : 반올림
"""

#정수선언
i=77
i2=-14
big_int=777777777777777788888888888879999999999999

#정수 출력
print(i)
print(i2)
print(big_int)


#실수출력
f=0.9999
f2=3.141592
f3=-3.9
f4=3/9

print(f)
print(f2)
print(f3)
print(f4)
print()


#연산실습
i1=39
i2=939
big_int1=7777777777777777777777
big_int2=8888888888888888888888
f1=1.234
f2=3.9394

#덧셈
print(">>>>> +")
print("i1 + i2 :", i1+i2)
print("f1 + f2 :", f1+f2)
print("big_int1 + big_int2 :", big_int1+big_int2)

#곱셈
print(">>>>> *")
print("i1 * i2 :", i1*i2)
print("f1 * f2 :", f1*f2)
print("big_int1 * big_int2 :", big_int1*big_int2)


#형변환
a=3.
b=6
c=.7
d=12.7

#타입 출력
print(type(a), type(b), type(c), type(d))

#형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) #Ture : 1, False : 0
print(float(False))
print(complex(3))
print(complex('3')) #문자열-> 숫자형
print(complex(False))
print()


# 수치 연산 함수
print(abs(-7))

x, y=divmod(100,8) #몫과 나머지
print(x, y)
print(pow(5,3), 5**3)

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)