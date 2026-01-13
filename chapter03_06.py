# Chapter 03-6
# 집합(Set) 특징
# 집합 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4, 4 , 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen','Cap','Plate' ])
e = {'foo', 'bar', 'baz', 'foo', 'qux' }
f = {42, 'foo', (1,2,3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환 (set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

#리스트 변환 (set -> list)
l =list(c)
l2 = list(e)

print('l - ', type(l), l)
print('l2 - ', type(l2), l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6])

print('s1 & s2 - ', s1 & s2) # 교집합
print('s1 교집합 - ', s1.intersection(s2))

print('s1 | s2 - ', s1 | s2) # 합집합
print('s1 합집합 - ', s1.union(s2))

print('s1 - s2 - ', s1 - s2) # 차집합
print('s1 차집합 - ', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 - ', s1.isdisjoint(s2)) # 교집합이 없으면 True

# 부분 집합 확인
print('subset :', s2.issubset(s1))
print('superset :', s1.issuperset(s2)) # s2가 s1의 슈퍼셋인가?

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)

s1.discard(3)
print('s1 - ', s1)
# s1.remove(7) # 없는 값을 제거하려고 하면 에러 발생
# s1.discard(7) # 없는 값을 제거하려고 해도 에러 발생X

s1.clear()
print('s1 - ', s1)


a = [1, 2, 3]
a.clear()
print(a)


# 집합 자료형 10문제

# 문제 1. (기초 생성) 비어 있는 집합 my_set을 생성하는 코드를 작성하세요. (주의: {}는 사용하면 안 됩니다.)
my_set = set()


# 문제 2. (중복 제거) 리스트 nums = [1, 2, 2, 3, 3, 3, 4]가 있습니다. 이 리스트에서 중복을 모두 제거하고 유일한 숫자들만 남긴 집합 unique_nums를 만드세요.
nums = [1, 2, 2, 3, 3, 3, 4]
umique_nums = set(nums)

# 문제 3. (값 추가) 집합 s = {1, 2, 3}이 있습니다. 여기에 숫자 4를 추가하는 코드를 작성하세요.
s = {1,2,3}
s.add(4)
print(f"3번 결과 : {s}")


# 문제 4. (여러 값 추가) 집합 s = {1, 2}가 있습니다. 여기에 리스트 [3, 4, 5]에 들어있는 값들을 한꺼번에 추가하는 코드를 작성하세요.
s={1,2}
s.update({3,4,5})
print(f"4번 결과 : {s}")


# 문제 5. (안전한 삭제) 집합 s = {1, 2, 3}에서 값 5를 삭제하려고 합니다. 만약 5가 없더라도 에러가 나지 않도록 삭제하는 메서드를 사용하세요.
s={1,2,3}
s.discard(5) #remove()는 에러발생. discard는 발생하지 않음
print(f"5번 결과 : {s}")



# 문제 6. (교집합) 두 집합 A = {1, 2, 3, 4}와 B = {3, 4, 5, 6}이 있습니다. 두 집합에 모두 포함된 요소만 뽑아서 출력하세요.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(f"6번 결과 교집합 {A & B}") #또는 A.intersection (B)


# 문제 7. (합집합) 위의 두 집합 A와 B의 모든 요소를 합치되, 중복은 제거하여 출력하세요.
A = {1,2,3,4}
B ={3,4,5,6}
# 기호를 사용하는 방법
print(f"7번 결과 합집합: {A | B}")

# 메서드를 사용하는 방법
# print(f"7번 결과 합집합: {A.union(B)}")


# 문제 8. (차집합) 집합 A에는 있는데 B에는 없는 요소(1, 2)만 남기는 코드를 작성하세요.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 기호를 사용하는 방법
print(f"8번 결과 차집합: {A - B}")

# 메서드를 사용하는 방법
# print(f"8번 결과 차집합: {A.difference(B)}")



# 문제 9. (문자열 처리) 문자열 "Hello World"에 들어있는 '알파벳 종류'가 총 몇 개인지 구하는 코드를 작성하세요. (공백 포함 여부는 상관없음, 대소문자는 구분함)
s="Hello World"
unique_chars = set(s) #문자열을 집합으로 변환
print(f"9번  결과 종류:{unique_chars}")
print(f"알파벳 종류 개수: {len(unique_chars)}")


# 문제 10. (부분집합 확인)sub = {1, 2}이고 main = {1, 2, 3, 4}입니다. sub가 main의 부분집합이 맞는지 확인하여 True가 출력되게 하세요.
sub = {1, 2}
main = {1, 2, 3, 4}

# 1. 비교 연산자(<=)를 사용하는 방법
print(f"10번 결과(연산자): {sub <= main}")

# 2. 메서드(.issubset)를 사용하는 방법
print(f"10번 결과(메서드): {sub.issubset(main)}")