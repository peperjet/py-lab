import sympy as sp
from sympy.combinatorics import Permutation

# 2026-03-05 행렬과 역행렬

# 예제 1
A1 = sp.Matrix([[1, 4, 3], [2, 5, 6], [0, 0, 0]])
print(A1.det()) #역행렬이 존재할 수 없음

# 예제 2
A2 = sp.Matrix([[3, 5], [1, 2]])

print(A2.det()) # 행렬식
print(A2.inv()) # 역행렬



# 예제 3
A3 = sp.Matrix([
    [1, 2, 3],
    [2, 5, 3],
    [1, 0, 8]
])
# A = matrix(3, 3, [1, 2, 3, 2, 5, 3, 1, 0, 8]) 3행 3열 행렬
b3 = sp.Matrix([1, 3, -1])

# 역행렬 이용해 해 구하기
x = A3.inv() * b3

print(x)



# 예제 4
# 대각행렬
H = sp.diag(-3, -2, 1)

# 단위행렬
K = sp.eye(3)

# 영행렬
J = sp.zeros(2,2)

print("H =")
print(H)
print()

print("K =")
print(K)
print()

print("J =")
print(J)



# 예제5 : 대칭행렬 / 반대칭행렬 확인
A5 = sp.Matrix([
    [1,2,3],
    [2,4,5],
    [3,5,6]
])

B5 = sp.Matrix([
    [0,1,-2],
    [-1,0,3],
    [2,-3,0]
])

# A가 대칭행렬인지
print(A5 == A5.T)

# B가 반대칭행렬인지
print(B5.T == -B5)



# 예제6 : LU 분해
A6 = sp.Matrix([
    [2, 6, 2],
    [-3, -8, 0],
    [4, 9, 2]
])

L, U, _ = A6.LUdecomposition()

print("L =")
print(L)

print()
print("U =")
print(U)


# 예제 7 : 치환의 반전과 짝치환/홀치환 확인

p = Permutation([4,0,1,3,2])  # (5 1 2 4 3)

print(p.inversions())   # 반전 위치
print(p.signature())    # 짝치환(1) / 홀치환(-1)



# 예제 8 : B의 행렬식 구하기
B8 = sp.Matrix([
    [1,2,3],
    [-4,5,6],
    [7,-8,9]
])

print(B8.det())



# 예제9 : 행렬식 성질 확인 예제 
A9 = sp.randMatrix(3)
B9 = sp.randMatrix(3)

AB = A9 * B9

print("|AB| = |A||B| ?", AB.det() == A9.det() * B9.det())
print("|A| =", A9.det())

if A9.det() != 0:
    print("Is A invertible ?", True)
    print("|A^-1| = |A|^-1 ?", 1/A9.det() == A9.inv().det())
else:
    print("Is A invertible ?", False)