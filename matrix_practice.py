import sympy as sp


# 예제 1
A1 = sp.Matrix([
[1,1,2],
[2,4,-3],
[3,6,-5]
])

b = sp.Matrix([9,1,0])

Ab = A1.row_join(b)

print("첨가행렬:")
print(Ab)

rref_matrix, pivot = Ab.rref()

print("\nRREF 결과:")
print(rref_matrix)


# 예제 2. 행렬 A RREF 기약행 사다리꼴 구하기
# 행렬 A 입력
A2 = sp.Matrix([
[1,1,1,4,4],
[2,3,4,9,16],
[-2,0,3,-7,11]
])

print("\nA =")
print(A2)

print("\nRREF(A) =")
print(A2.rref()[0])



# 예제 3. 연립방정식 바로 해(x) 구하는 함수
A3 = sp.Matrix([
    [2, 4, 6],
    [2, -1, 1],
    [3, 0, -1]
])
b3 = sp.Matrix([18, 8, 3])

Ab3 = A3.row_join(b3)

print("[A:b] =")
print(Ab3)

rref3, pivot3 = Ab3.rref()
print("\nRREF([A:b]) =")
print(rref3)

# 해 구하기
sol = rref3[:, -1]
print(f"\n해: x = {sol[0]}, y = {sol[1]}, z = {sol[2]}")



# 예제4.첨가행렬 RREF 구하기
A4 = sp.Matrix([
    [1, -2, 1],
    [2, -2, 1],
    [3, 1, -5],
    [0, -1, 2],
    [-6, 0, 7]
])
b4 = sp.Matrix([7, 5, 0, -4, -10])

Ab4 = A4.row_join(b4)

print("\n[A:b] =")
print(Ab4)

rref4, pivot4 = Ab4.rref()

print("\nRREF([A:b]) =")
print(rref4)
# 0 = 1 이건 절대 성립 못 함. 모순 : 해 없음.


# 예제 5. Gauss-Jordan 소거법을 이용하여 연립방정식의 해를 구하기
A5 = sp.Matrix([
    [1, 3, -2, 0, 2, 0],
    [2, 6, -5, -2, 4, -3],
    [0, 0, 5, 10, 0, 15],
    [2, 6, 0, 8, 4, 18]
])
b5 = sp.Matrix([0, -1, 5, 6])

Ab5 = A5.row_join(b5)

print("[A:b] =") #그대로 출력
print(Ab5)

rref5, pivot5 = Ab5.rref()
print("\nRREF([A:b]) =") #앞에 빈 줄을 하나 넣고 출력
print(rref5)
print("\nPivot columns:", pivot5)

# 해집합(일반해)까지 보고 싶을 경우
x1, x2, x3, x4, x5, x6 = sp.symbols("x1:7")
sol_set = sp.linsolve((A5, b5), (x1, x2, x3, x4, x5, x6))
print("\n해집합 =", sol_set)