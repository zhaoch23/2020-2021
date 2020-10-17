from typing import List
import os
import statistics
import copy

class Student(object):

    def __init__(self, name: str, marks: List[int], exercises: List[int]) -> None:
        self.name = name
        self.marks = marks
        self.exercises = exercises
    
    def get_average(self) -> float:
        return statistics.mean(self.marks)


def linear_search_1(list: List, target) -> int:
    i = 0
    for j in range(len(list)):
        if target == list[j]:
            break
        else:
            i += 1

    return i

def linear_search_2(list: List[int], cut_off: int) -> List:
    i = len(list) - 1
    while i >= 0:
        if list[i] <= cut_off:
            del list[i]
        i -= 1

    return list

def linear_search_3(list: List[str], target: str) -> List:
    i = len(list) - 1
    while i >= 0:
        for j in range(len(target)):
            if len(list[i]) == len(target) and list[i][j] == target[j]:
                string = list[i]
                del list[i]
                list.insert(0, string)
                return list

        i -= 1
    



def linear_search_4(list: List[Student], target: str) -> Student:
    for i in range(len(list)):
        q = 0
        for j in range(len(target)):
            if len(list[i].name) >= len(target) and list[i].name[j] == target[j]:
                q  += 1
            else:
                break

        if q == len(target):
            return list[i]

def linear_search_5(list: List[int]) -> List:
    temp_list = []
    temp_list_ = []
    for i in range(len(list)):
        if list[i] >= 50:
            temp_list.append(list[i])
        else:
            temp_list_.append(list[i])
    
    sum_ = sum(temp_list_)
    if sum_%2 == 0:
        return temp_list
    else:
        return list



def bubble_sort_1(list: List[Student]) -> List:
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j].get_average() > list[j + 1].get_average():
                list[j], list[j + 1] = list[j + 1], list[j]
    
    return list

def bubble_sort_2(list: List[Student]) -> List:
    for i in range(len(list) - 1):
        for j in range(len(list) - i -1):
            if len(list[j].exercises) > len(list[j + 1].exercises):
                list[j], list[j + 1] = list[j + 1], list[j]     

    return list          


if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(path)

    os.system('pytest test_main.py')


            


