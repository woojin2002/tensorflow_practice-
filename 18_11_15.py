import numpy as np = numpy�� np��� �̸����� �����´�.��� �ؼ��մϴ�. 

x = np.array([1.0,2.0,3.0]) = ������ �迭�� x�� �����Ѵ�.

type(x) = x�� ������ ��ȯ�ϴ��� Ȯ�� �Ѵ�.

�س����� �迭�� ����
x = np.array([1,2,3])�� y = np.array([2,4,6])�� ���ϸ� �ε��� ������ ������ �����Ͽ� �״����� 2,8,18�� �ȴ�.

��Ģ���� ��� �׷�.

x = np.array([[1,2],[3,4]])�� y = np.array([[3,0],[0,6]])��� ������ ��
x�� y�� ��Ģ�����ϸ� �ε��� ���� ��ġ�ϴ� ���� �����Ѵ�.

�׸��� y�� y = np.array([10,20])�϶��� 10�� x�� 1��°[1,2]�� 1�� �׸��� [3,4]�� 3�� �����ϰ� ������ 2�� 4�� 20�� �����Ѵ�.
//��ε�ĳ��Ʈ�� ����

���̽��� �̿��Ͽ� �׷����� �׸��� ���� ������Ʈ�� ���� matplotlib�� �ٿ�޾��ְ� import�� ����Ͽ� �ҷ��� �׷����� ������ �Է����� show�� �����ָ� �ȴ�. 

�׷��� �׸��� ���� : 
import numpy as np 
import matplotlib.pyplot as plt
x = np.arange(0,6,0,1)//0���� 6���� 0.1�������� �׸���� ��
y = np.sin(x)
plt.plot(x,y)
plt.show()
---------------------------
�״������� �ڻ��α��� �׷����ڸ�

import numpy as np 
import matplotlib.pyplot as plt
x = np.arange(0,6,0,1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle="--",label="cos")//cos�� �������� �׸���
plt.xlabel("x")//x�� �̸�
plt.ylabel("y")// y�� �̸�
plt.title('sin & cos')//�׷��� ����
plt.legend()
plt.show()//������