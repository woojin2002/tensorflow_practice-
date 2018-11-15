import numpy as np = numpy를 np라는 이름으로 가져온다.라고 해석합니당. 

x = np.array([1.0,2.0,3.0]) = 넘파이 배열을 x에 대입한다.

type(x) = x가 무엇을 반환하는지 확인 한다.

※넘파이 배열의 연산
x = np.array([1,2,3])와 y = np.array([2,4,6])를 곱하면 인덱스 값끼리 곱셈을 실행하여 그다음은 2,8,18이 된다.

사칙연산 모두 그럼.

x = np.array([[1,2],[3,4]])과 y = np.array([[3,0],[0,6]])라고 선언한 후
x와 y를 사칙연산하면 인덱스 값이 일치하는 곳만 연산한다.

그리고 y가 y = np.array([10,20])일때는 10은 x의 1번째[1,2]중 1만 그리고 [3,4]중 3만 연산하고 나머지 2와 4는 20을 연산한다.
//브로드캐스트의 내용

파이썬을 이용하여 그래프를 그리는 법은 프롬프트에 먼저 matplotlib을 다운받아주고 import를 사용하여 불러와 그래프의 정보를 입력한후 show로 보여주면 된다. 

그래프 그리기 예시 : 
import numpy as np 
import matplotlib.pyplot as plt
x = np.arange(0,6,0,1)//0에서 6까지 0.1간격으로 그리라는 말
y = np.sin(x)
plt.plot(x,y)
plt.show()
---------------------------
그다음에는 코사인까지 그려보자면

import numpy as np 
import matplotlib.pyplot as plt
x = np.arange(0,6,0,1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle="--",label="cos")//cos는 점선으로 그리기
plt.xlabel("x")//x축 이름
plt.ylabel("y")// y축 이름
plt.title('sin & cos')//그래프 제목
plt.legend()
plt.show()//보여줘