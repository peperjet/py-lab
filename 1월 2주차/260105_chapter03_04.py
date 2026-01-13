#Chapter03-4
#파이썬 튜플
#리스트와 비교 중요
#튜플 자료형 (순서O, 중복O, 수정X, 삭제X) - 불변

#선언

a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

#인덱싱
print(type(a), type(b))
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('d - ', list(e[-1][1]))

#수정 x
#d[0] = 1500

#슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[:2][1:3])

#튜플 연산
print('>>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)


#튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

#팩킹 & 언팩킹

#팩킹
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

#언팩킹 묶여있던 것을 푸는 것
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)


# 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)


print()


# 튜플형 10문제

# 1.튜플 (1, 2, 3, 4)의 길이를 출력하라.
print(len((1, 2, 3, 4)))


# 2.튜플 (10, 20, 30)에서 첫 번째 값을 출력하라.
t = (10, 20, 30)
print(t[0])


# 3.튜플 (10, 20, 30)을 리스트로 변환하여 출력하라.
t = (10, 20, 30)
l = list(t)
print(l)


# 4.튜플 (1, 2, 3)에 (4, 5)를 붙여 새 튜플을 만들어 출력하라.
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)


# 5.튜플 (1, 2, 3, 2, 2)에서 숫자 2의 개수를 출력하라.
t = (1, 2, 3, 2, 2)
print(t.count(2))


# 6.튜플 (10, 20, 30)을 a, b, c로 언패킹하여 출력하라.
t = (10, 20, 30)
a, b, c = t
print(a, b, c)


# 7.튜플 (5, 1, 3)을 정렬된 리스트로 변환하여 출력하라.
t = (5, 1, 3)
l = sorted(list(t))
print(l)


# 8.튜플 안에 숫자 4가 있는지 True / False로 출력하라.
t = (1, 2, 3, 4, 5)
print(4 in t)


# 9.리스트 [1, 2, 3]을 튜플로 변환하여 출력하라.
l = [1, 2, 3]
t = tuple(l)
print(t)


# 10.튜플이 수정 불가능한 자료형임을 코드로 확인해보라 (에러 발생 확인)
t = (1, 2, 3)
#t[0] = 10

print()
