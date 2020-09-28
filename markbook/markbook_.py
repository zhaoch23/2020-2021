'''Markbook object
'''

import json
import statistics
import os
from PIL import Image
from fastcode import *


class Markbook(object):
    '''Marbook object, involves self.classroom_list, save all things in this object
    '''

    def __init__(self):
        self.classroom_list = []#To save all informations in this list


    def set_up(self):
        '''set up everything
        '''
        self.read_file()

    def close(self):
        '''When object closes
        '''
        self.write_file()

    #file methods: read file, write file, empty file
    def read_file(self):
        '''Read the file markbook.json
        '''
        try:
            f = open('markbook.json', 'r')
            self.classroom_list = json.loads(f.read())
            f.close()
        except:
            print('Storage file missing')
    
    def write_file(self):
        '''Write the informations of classroom_list into json file
        '''
        f = open('markbook.json', 'w')
        f.write(json.dumps(self.classroom_list, indent=4))
        f.close()
        
    def empty_file(self):
        '''Empty the informaiton, for testing
        '''
        f = open('markbook.json', 'w+')
        f.close()
    
    def buble_sort(self, nums: list):
        '''Sort by mark or last name
        '''
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                try:
                    if nums[j][1] < nums[j + 1][1]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                except:
                    try:
                        if nums[j][LAST_NAME] < nums[j + 1][LAST_NAME]:
                            nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    except:
                        if nums[j][ASSIGNMENT_NAME] < nums[j + 1][ASSIGNMENT_NAME]:
                            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    #classroom methods, create classroom, get informations from classroom, edit classroom, delete classroom
    def add_classroom(self, course_code: str='', course_name: str='',
                            period: int=None, teacher_name: str='', student_list: list=[], 
                            assignments_list: list=[]) -> dict:
        '''To create a classroom dictionary(default empty):
        Args:
            course_code='': course code
            course_name='': course name
            period=None: period
            teacher_name='': teacher's name
            student_listt=[]: A list of students
            assignments_list=[]: A list of assignments
        Returns -> dict:
            A dictionary object that contents all args upon
        '''
        
        classroom = {
            COURSE_CODE: course_code,
            COURSE_NAME: course_name,
            PERIOD: period,
            TEACHER_NAME: teacher_name,
            STUDENT_LIST: student_list,
            ASSIGNMENTS_LIST: assignments_list
        }

        self.classroom_list.append(classroom)

        return classroom
    
    #Methods to get informations of all classroom
    def get_all_classroom(self) -> list:
        '''get all classrooms in classroom list
        Returns -> list:
            A list of all classroom dict objs
        '''
        return self.classroom_list
        
    def get_classroom_detials(self, classroom: dict) -> list:
        '''get detials of a certain classroom in classroom list
        Returns -> list:
            A list that contents tuples of key-value pairs
            example: [('course_code', 'ICS4U'), ('course_name', 'Computer Science')]
        '''
        return [classroom.items()]
        
    def get_classroom_average_median(self, classroom: dict) -> list:
        '''get the class average and median
        Returns -> list:
            A list contents class average and class median
            example: [90, 85]
        '''
        list = []
        for student in classroom[STUDENT_LIST]:
            ave = self.get_student.get_student_average(classroom, student)
            list.append(ave)
        class_ave = round(statistics.mean(list),1)
        class_med = round(statistics.median(list),1)
        return [class_ave, class_med]


    #Methods to edit a classroom
    def update_classroom(self, classroom: dict, **kwargs: dict) -> dict:
        '''update everything in the classroom with given key word args
            Return -> dict:
            the dict updated
        '''
        classroom.update(**kwargs)
        return classroom

    def del_classroom(self, classroom: dict):
        '''Remove a classroom from list
        '''
        if classroom in self.classroom_list:
            self.classroom_list.remove(classroom)

    
    #Assignment methods, create assignment, get informations from assignment, edit assignment, delete assignment
    def add_assignment(self, classroom, name: str='', due: str='', points: int=None, to_everyone=True) -> dict:
        '''To create a classroom dictionary(default empty):
        Args:
            classroom: a dict obj contents a classroom
            name='': assignment name
            due='': due date
            points=None: full points
            to_everyone=True: assign this assignment to everyone, if False， must assign the assignment to each student manually(defualt marks=None)
        Returns -> dict:
            A dictionary object that contents all args upon
        '''
        assignmnet = {
            ASSIGNMENT_NAME: name,
            DUE: due,
            POINTS: points
        }

        classroom[ASSIGNMENTS_LIST].append(assignmnet)

        if to_everyone:
            for student in classroom[STUDENT_LIST]:
                student[MARKS].append({ASSIGNMENT_NAME: name, MARKS: 0})  
        
        return assignmnet
    
    
    #Methods to get informations of all assignment
    def get_all_assignments(self, classroom: dict) -> list:
        '''get all assignmnet in assignment list
        Returns -> list:
            A list of all assignment dict objs
        '''
        return classroom[ASSIGNMENTS_LIST]
    
    def get_assignment_detials(self, assignment: dict, classroom: dict) -> list:
        '''get detials of a certain assignment in ceratin classroom's assignment list
        Returns -> list:
        A list that contents tuples of key-value pairs
        example: [('name', 'markbook'), ('due', 'Sept/28 2020')]
        '''
        return [assignment.items()]

    def get_assignment_student_marks(self, classroom: dict, assignment: dict) -> list:
        '''get all students participate in and their marks
        Returns -> list:
            A list that contents lists of individual detials that content first name and marks
            example: [['Chengzong', 100], ['Duoyang', 100], ['Jason', 100]]
        '''
        list = []
        for student in classroom[STUDENT_LIST]:
            for assignment_ in student[MARKS]:
                
                if assignment_[ASSIGNMENT_NAME] == assignment[ASSIGNMENT_NAME]:


                    list.append([student[FIRST_NAME], assignment_[MARKS]])
        return list
        
    def get_assignment_average_median(self, classroom: dict, assignment: dict) -> list:
        '''get the class average and median of the an assignment
        Returns -> list:
            A list contents class average and class median
            example: [90, 85]
        '''
        list = self.get_assignment_student_marks(classroom, assignment)
        temp_mark_list =[]
        sum = 0
        for student in list:
            temp_mark_list.append(student[1])
            
        return [round(statistics.mean(temp_mark_list),1), round(statistics.median(temp_mark_list),1)]
  
    def get_all_assignment_average_median(self, classroom: dict) -> list:
        '''get final mark average and median of class
        Returns -> list:
            A list contents class average and class median
            example: [90, 85]
        '''
        templist = [[],[]]
        for ass in classroom[ASSIGNMENTS_LIST]:
            list_ = self.get_assignment_average_median(classroom, ass)
            templist[0].append(list_[0])
            templist[1].append(list_[1])        
        return [round(statistics.mean(templist[0]), 1), round(statistics.median(templist[1]), 1)]


    #Methods to edit an assignment
    def update_assignment(self, assignment: dict, **kwargs) -> dict:
        '''update everything in the classroom with given key word args
        Return -> dict:
            the dict updated
        '''
        assignment.update(**kwargs)
        return assignment
        
    def del_assignment(self, classroom:dict, assignment:dict):
        '''Remove an assignment from a classroom
        '''
        if assignment in self.get_all_assignment(classroom):
            for student in classroom[STUDENT_LIST]:
                for assignment_ in student[MARKS]:
                    if assignment_[ASSIGNMENT_NAME] == assignment[ASSIGNMENT_NAME]:
                        student[MARKS].remove(assignment_)
            classroom[ASSIGNMENTS_LIST].remove(assignment)

    #student methods, add students, get informations from a student, edit student, remove student, print reports
    def add_student(self, classroom, first_name: str='', last_name: str='',
                            gender: str='', image: str='', 
                            student_number: int=None, grade: int=None,
                            email: str='', marks: list=[],
                            comments: str='') -> dict:
        '''
        '''

        student = {
            FIRST_NAME: first_name,
            LAST_NAME: last_name,
            GENDER: gender,
            IMAGE: image,
            STUDENT_NUMBER: student_number,
            GRADE: grade,
            EMAIL: email,
            MARKS: marks,
            COMMENTS: comments
        }

        classroom[STUDENT_LIST].append(student)

        return student


    def get_all_student(self, classroom: dict) -> list:
        '''get all student in student list
        Returns -> list:
           A list of all student dict objs
        '''
        return classroom[STUDENT_LIST]
    
    def get_student_profile(self, student: dict, classroom: dict) -> list:
        '''get the profile of student
        Returns -> list:
            A list that contents a list of keys and a list of values
        example: [('first_name': 'Chengzong'), ('list_name', 'Zhao')]
        '''
        return [student.items()]

    def get_student_marks(self, classroom: dict, student: dict) -> list:
        '''get all assignment the student participate in and it's marks
        Returns -> list:
            A list that contents lists of assignment detials that content assignment name, marks, class average and median
            example: [['first test', 100, 100, 100], ['second test', 100, 100, 100]]
        '''
        list_ = []
        temp_list = []
        for assignment in student[MARKS]:
            for assignment_ in classroom[ASSIGNMENTS_LIST]:
                if assignment[ASSIGNMENT_NAME] == assignment[ASSIGNMENT_NAME]:

                  stat = self.get_assignment_average_median(classroom, assignment_)
                  temp_list = list(assignment.values())
                  temp_list.append(stat[0])
                  temp_list.append(stat[1])
                  list_.append(temp_list)
                  temp_list = []
                  break

        return list_
        
    def get_student_average(self, classroom: dict, student: dict) -> float:
        '''get the student average mark
        Returns -> float:
            student's average mark of all assignment
        '''
        list = self.get_student_marks(classroom, student)
        temp_mark_list = [a[1] for a in list]
            
        ave = statistics.mean(temp_mark_list)

        return ave

    def edit_student(self, student: dict, **kwargs) -> dict:
        '''update student profile
        '''
        student.update(**kwargs)
        return student

    def add_student_marks(self, student: dict, assignment: dict, marks: float=None) -> dict:
        '''add student assignment marks
        '''
        if student:
            mark = {ASSIGNMENT_NAME: assignment[ASSIGNMENT_NAME], MARKS: marks}
            student[MARKS].append(mark)
        
        return mark
    
    def del_student_marks(self, student: dict, assignment: dict):
        '''del a assignment from student list
        '''
        for a in student[MARKS]:
            if a[ASSIGNMENT_NAME] == assignment[ASSIGNMENT_NAME]:
                student[MARKS].remove(a)
    
    def add_student_comments(self, student: dict=None, comment: str='') -> str:
        '''add a report card comment
        '''
        if student:
            student[COMMENTS] = comment
        
        return comment
    
    def del_student(self, classroom: dict, student: dict):
        '''remove a student
        '''
        if student in classroom[STUDENT_LIST]:
            classroom[STUDENT_LIST].remove(student)

