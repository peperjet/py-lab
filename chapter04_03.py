#260107 Chapter04-2
#파이썬 반복문 
# While 실습

# while <expr>:
#   <statement(s)>

#예제1. 조건을 만족하는 동안 반복
n = 5
while n > 0:
    print(n) 
    n = n - 1   

#예제2
a = ['foo','bar','baz']

while a:
    print(a.pop())


#예제3 break, continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')

# 예제4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

#if 중첩
#예제5
i = 1

while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1


# while - else 구문

# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')


#예제7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux' #리스트에 없는 값
i1 = 0

while i1 < len(a):
    if a[i1] == s:
        print('Found it!')
        break
    i1 += 1
else:
    # 루프를 끝까지 돌았는데 s를 못 찾아서 break를 안만났을 때 실행
    print(s, 'not found in list.')


#무한반복
#While True
#   print('Foo')

#예제 8
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())