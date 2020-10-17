from main import *

res = Student('res', [80, 22, 39, 49], [1,2,3,4,5])
crynn = Student('crynn', [70, 12, 56, 77], [1,2,3,5,6])
knox = Student('knox', [80, 76, 21, 49, 89], [1, 2, 3, 4])
ryatt = Student('ryatt', [90 ,98, 12, 75, 54], [1,2,3,4,5,6,7,8])
ares = Student('ares', [76, 42, 42, 65, 32], [1])

classroom = [
    res,
    crynn,
    knox,
    ryatt,
    ares
]


def test_1():
    num = [1,2,3,4,5,6,7]
    assert linear_search_1(num, 4) == 3

    num = [3,2,3,9,5,3,7,9,2]
    assert linear_search_1(num, 7) == 6

def test_2():
    num = [10, 20, 30, 40, 50, 60, 70, 60, 50, 40]
    assert linear_search_2(num, 40) == [50, 60, 70, 60, 50]

    num = [1,2,6,8,0,3,4,5,6,4]
    assert linear_search_2(num , 5) == [6,8,6]

def test_3():
    list = ['4565324', '9074y', 'y64850335y0', 'y9469817']
    string = '4565324'
    assert linear_search_3(list, string) == ['4565324', '9074y', 'y64850335y0', 'y9469817']
    string = '9074y'
    assert linear_search_3(list, string) == ['9074y', '4565324', 'y64850335y0', 'y9469817']

def test_4():
    assert linear_search_4(classroom, 'kn') == knox
    assert linear_search_4(classroom, 'rya') == ryatt

def test_5():
    num = [49 ,50]
    assert linear_search_5(num) == [49, 50]

    num = [1,2,3,67,68]
    assert linear_search_5(num) == [67, 68]

    num = [4, 88, 5]
    assert linear_search_5(num) == [4, 88, 5]

def test_6():
    assert bubble_sort_1(classroom) == [res, ares, crynn, knox, ryatt]

def test_7():
    assert bubble_sort_2(classroom) == [ares, knox, res, crynn, ryatt]

