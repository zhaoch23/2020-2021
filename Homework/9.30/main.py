from typing import List

class Teacher:

    def __init__(self, first_name:str, last_name:str, classrroms:List[object], employee_num:int):
        self.first_name = first_name
        self.last_name = last_name
        self.classrooms = classrroms
        self.employee_num = employee_num
    
    def get_email(self) -> str:
        return f'{self.first_name}.{self.last_name}@ycdsb.ca'
    
    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Student:

    def __init__(self, first_name:str, last_name:str, graduate_year:int, classrooms:List[object]):
        self.first_name = first_name
        self.last_name = last_name
        self.graduate_year = graduate_year
        self.classrooms = classrooms
    
    def get_email(self) -> str:
        return f'{self.first_name}.{self.last_name}{self.graduate_year}@ycdsbk12.ca'
    
    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'        


class Classroom:

    def __init__(self, name:str, course_code:str, students:List[Student], teacher:Teacher):
        self.name = name
        self.course_code = course_code
        self.students = students
        self.teacher = teacher

    def add_student(self, email:str, all_students:List[Student]) -> None:
        for student in all_students:
            self.students.append(student)

def main():
    classroom = Classroom('computer science', 'ICS 4U', [], None)
    teacher = Teacher('', 'Gallo', [classroom], 0)
    student = Student('Chengzong', 'Zhao', 21, [classroom])
    classroom.students = [student]
    classroom.teacher = teacher

    print('Main function')

if __name__ == "__main__":
    main()


