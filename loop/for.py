import os
import sys

for i in range(1, 5):
    print(i)
    #if i == 3:
        #break
else:
    print('The for loop is over')

print("for end")

# 추가적으로 else 도 같이 사용할 수 있음. 다만 break 에 걸려서 for 문을 나오는 경우에는 else 문이 실행되지 않음

# 파이썬의 for 루프는 C/C++ 에서 제공하는 for 루프와 다름. 파이썬의 for 는 차라리 C# 의 foreach 루프 및
# Java 1.5의 `for (int i : IntArray)`와 비슷하다
# C/C 처럼 `for (int i = 0; i < 5; i)` 와 같이 사용하고 싶은 경우, 파이썬에서는 단순히 for i in range(0,5)`라고 입력하면 됨
