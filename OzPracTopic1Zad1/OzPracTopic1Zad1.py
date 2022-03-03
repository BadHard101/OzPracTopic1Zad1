# task_A148
# �������� ������� two_identical(start, finish), ������� ���������� ���������� �����
# � ��������� ����� ������� start � finish (�� �� ������), � ������ ������� ���� ���� �� ��� ���������� �����.
#
# �������:
# max_multiple(20,33) ==> 1 (����� 22)
# max_multiple(0,101) ==> 10

import traceback


def two_identical(start, finish):
    s=0
    for i in range(start+1,finish):
        a = [0]*10
        while(i!=0):
            a[i%10]+=1
            if (a[i%10]==2):
                s+=1
                break
            i=i//10
    return s


# �����
try:
    assert two_identical(20, 33) == 1
    assert two_identical(0, 10) == 0
    assert two_identical(0, 101) == 10
    assert two_identical(0, 1000) == 261
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
