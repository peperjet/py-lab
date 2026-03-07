#260103 문자열 10문제

#1.문자열 s가 주어질 때 문자열의 길이를 출력하라.
a = "Life is too short"
print(len(a))


#2.문자열 s가 주어질 때 첫 글자와 마지막 글자를 출력하라.
a = "Life is too short, You need Python"
print(a[0], a[-1])


#3.문자열 s가 주어질 때 문자열을 모두 대문자로 변환하여 출력하라.
a = "hi"
print(a.upper())



#4.문자열 s가 주어질 때 문자열을 모두 소문자로 변환하여 출력하라.
a="HI"
print(a.lower())



#5.문자열 s가 주어질 때 문자열에 'a'가 몇 개 있는지 출력하라.
a = "happy"
print(a.count('p'))



#6.문자열 s가 주어질 때 문자열을 거꾸로 출력하라.
a = "happy"
print(a[::-1])


#7.문자열 s가 주어질 때 'python'이라는 단어가 포함되어 있으면 True, 아니면 False를 출력하라.
a="Python is difficult for me"
print("Python" in a)


#8.문자열 "hello world"에서 공백을 제거한 문자열을 출력하라.
a="hello world"
print(a.replace(" ",""))


#9.문자열 s가 주어질 때 문자열이 회문인지 True / False로 출력하라.
a="level"
print(a==a[::-1])


#10.문자열 "abc123"에서 숫자만 추출해서 출력하라.
a="abc123"
print(a[3:])
