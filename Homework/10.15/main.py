from typing import List
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
            if len(list[i]) <= len(target) and list[i][j] != target[j]:
                del list[i]
                break

        i -= 1
    
    return list


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
    orginal_list = copy.copy(list)
    list_ = []
    i = len(list) - 1
    while i >= 0:
        if list[i] >= 50:
            list_.append(list[i])
            del list[i]
        i -= 1
    
    sum_ = sum(list)
    if sum_%2 == 0:
        return list_
    else:
        return orginal_list



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



            


