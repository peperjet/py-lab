def hello():
    print("Hello")

f = hello
f()


#반복 (시퀀스)
im_str = "Good Boy!"

print(dir(im_str))  # __iter__


#출력
for i in im_str:
    print(i)


#슬라이싱 연습
str_sl = "Nice Python"
print(str_sl[0:3]) # 0 1 2
print(str_sl[5:])  # 5부터 끝까지
print(str_sl[:len(str_sl)]) #처음부터 끝까지 str_sl[:11]
print(str_sl[:len(str_sl)-1]) #처음부터 끝에서 한 글자 전까지 [:10]
print(str_sl[:]) #처음부터 끝까지
print(str_sl[1:9:2]) #1부터 9까지 2칸씩
print(str_sl[-5:]) #뒤에서 5번째부터 끝까지
print(str_sl[1:-2]) #1부터 뒤에서 2번째 전까지
print(str_sl[::2]) #처음부터 끝까지 2칸씩
print(str_sl[:: -1]) #역순출력

#아스키코드 (또는 유니코드)
a = 'z'

print(ord(a))  #ord: 문자 -> 아스키코드
print(chr(122)) #chr: 아스키코드 -> 문자
print(chr(ord(a)))


#260105 챕터 03-3

#파이썬 리스트
#자료구조에서 중요


#선언 
a = []
b = list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.14159] 

#인덱싱
print('>>>>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', list(e[-1][1]))

#슬라이싱
print('>>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

#리스트 연산
print('>>>>>>>>>')
print('c + d = ', c + d)
print('c * 3 = ', c * 3)
print("'test' + c[0] = ", 'test' + str(c[0]))

#값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()


#Identity
temp = c
print(temp, c)
print(id(c))

#리스트 수정, 삭제
print('>>>>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2]=['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1]=['a', 'b', 'c'] 
print('c - ', c)
c[1:3]=[]
print('c - ', c)
del c[2] #삭제 
print('c - ', c)

#리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a)
# del a[6]
a.remove(10)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count("4"))
ex= [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove, pop, del

