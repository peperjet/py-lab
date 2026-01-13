#260103 숫자형 10문제

#1.정수 a = 10, b = 3이 주어질 때 *사칙연산 결과(+, -, , /) 를 한 줄씩 출력하라.
a,b=10,3
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#2.정수 n이 주어질 때 n이 짝수면 “even”, 홀수면 "odd"를 출력하라.
n=7
print("even" if n % 2 == 0 else "odd")



#3.정수 n이 주어질 때 n의 제곱을 출력하라.
n=4
print (n**2)


#4.정수 n이 주어질 때 n의 절댓값을 출력하라.
n= -5
print(abs(n))


#5.정수 a, b가 주어질 때 큰 수를 출력하라.
a,b =(7,5)
if a > b:
    print(a)
else:
    print(b)


#6.실수 x = 3.14159가 주어질 때 소수 둘째 자리까지 반올림하여 출력하라.
x=3.14159
print(round(x, 2))


#7.정수 n이 주어질 때 1부터 n까지의 합을 출력하라.
n=7
print(sum(range(1, n+1)))




#8.정수 n이 주어질 때 n의 자릿수 개수를 출력하라.
n=123456
print(len(str(n)))




#9.정수 n이 주어질 때 n이 3의 배수이면서 5의 배수인지 True / False로 출력하라.

n=17
print(n % 3==0 and n % 5 ==0)



#10.정수 n이 주어질 때 n의 일의 자리 숫자를 출력하라.
n=123
print(n % 10)
