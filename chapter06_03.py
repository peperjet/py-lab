# 260112 Chapter 06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대경로 ..(부모디렉토리), .(현재 디렉토리) -> 모듈내부에서만 사용


# 예제1
import sub1.module1
import sub2.module2


# 사용
sub1.module1.mod1_test1()
sub1.module1.mod1_test2()

sub2.module2.mod2_test1()
sub2.module2.mod2_test2()


print()
print()
print()


# 예제2
from sub1 import module1
from sub2 import module2 as m2 # alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제3 (상대경로는 '..')
from sub1 import *
from sub2 import *


module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test1()
