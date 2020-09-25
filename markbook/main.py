
'''Run this file to open markbook
python -m main
  '''

from fastcode import *
import os
import markbook_

class Option(object):
    '''option object, saves option attributes
    '''

    def __init__(self, name=None, index=-1, event=None, content=None):
        self.name = name
        self.index = index
        self.event = event
        self.content = content
    
    def __str__(self):
        return str(self.index)
    
    def trigger(self):
        if self.event:
            return self.event(self)
  


class Client(object):
    '''user interpertation object
    '''

    def __init__(self):
        self.markbook = markbook_.Markbook()

    def set_up(self):
        print("{:=^60}".format('Markbook'))
        print("{}".format('Loading...'))
        self.markbook.set_up()
        print("{}".format('Wellcome to Markbook'))
        self.view_all_classroom()
    
    def get_input(self, str: str) -> str:
        i = input(str)
        return i

    def get_assurance(self) -> bool:
        while True:
            i = input('Are you sure?(y/n):')
            if i == y:
                return True
            elif i == n:
                return False
            else:
                print("invalid input, please enter 'y' or 'n'")
    
    def header_1(self ,str:str):
        print("\n"*40+"{:=^60}".format(str))     

    def header_2(self, str:str):
        print("\n"*5+"{:-^60}".format(str))

    def skip_line(self):
        print("\n")      
  
    #model - view - controller
    def view_all_classroom(self, str1=''):
        '''a menu shows all classtooms and options
        '''
        #model part
        list = self.markbook.get_all_classroom()
        self.all_classroom_options = []#a list contents option objects in this menu 
        index = 0

        for classroom in list:#add all classrooms
            name = f'period {classroom[PERIOD]}, {classroom[COURSE_NAME]}'
            event = self.event_enter_a_classroom
            option = Option(name, index, event, classroom)

            self.all_classroom_options.append(option)
            index += 1

        #add other options
        self.all_classroom_options.append(Option('add a classroom', index,      self.event_add_a_classroom))
        self.all_classroom_options.append(Option('remove a classroom', index+1,   self.event_remove_a_classroom))
        self.all_classroom_options.append(Option('exit', index+2,               self.event_exit))

        #view part: print everything
        self.header_1('Menu: All Classrooms')
        if str1:
            print(str1)
            self.skip_line()
        self.header_2('classrooms')
        for classes in self.all_classroom_options:
            if int(str(classes)) < index:
              print (f"period{classes.content[PERIOD]}: {classes.content[COURSE_CODE]} {classes.content[COURSE_NAME]} by {classes.content[TEACHER_NAME]}")
        self.header_2('Options')
        for classes in self.all_classroom_options:
            if int(str(classes)) < index:
                print (f'type {classes.index} to enter class "{classes.name}"')
            else:
                print(f'type {classes.index} to {classes.name}')
        self.header_2('Please Enter')

        #User and controller part
        while True:
            option = self.get_input("Please enter the option index: ")
            for opt in self.all_classroom_options: 
                if str(opt) == str(option):    
                    return opt.trigger()
            else:
                print("invalid input, please try again")


    def event_add_a_classroom(self, obj: object, str1=''):
        self.header_1('Menu: Add Classroom')
        self.header_2('Classroom has following attributes')
        for attr in CLASSROOM_ATTRIBUTES.keys():
          print(attr)
  
        def create_classroom(list):
            if self.get_assurance:
                self.markbook.add_classroom(list[0], list[1], list[2], list[3])
                self.view_all_classroom(str1='Successfully added a classroom')
            else:
                enter_attributes()

        def enter_attributes():
            self.header_2("Please Enter")
            print("{:-^60}".format("type 'enter' to skip this attributes"))
            print("{:-^60}".format("type 'c' to cancel this addition"))
            list = ['', '', 0, '']
            for index, (key, value) in enumerate(CLASSROOM_ATTRIBUTES.items()):
                while True:
                    self.skip_line()
                    input_ =  self.get_input("please enter the {}(type: {},     defualt={})".format(key, type(value), value))
                    print(f'{key}: {input_}')
                    if input_ == 'c':
                        return self.view_all_classroom(str1='Cancelled addition')
                    elif input_:
                        list[index] = input_
                        break
                    elif not input_:
                        break

            self.header_2("Review New classroom")
            for index, key in enumerate(CLASSROOM_ATTRIBUTES.keys()):
                    print(f'{key}: {list[index]}')
            
            create_classroom(list)
        
        enter_attributes()

    def event_remove_a_classroom(self, obj: object):#
        pass

    def event_exit(self, obj: object):
        self.markbook.close()
    
    def event_enter_a_classroom(self, classroom: object):#
        list = self.markbook.get_classroom_detials(classroom.content)
        print("="*7 + classroom.name + "="*7 )
        print(list)
        
    #def view_all_assignments(self):
        #list = self.markbook
    
        


if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(path)

    client = Client()
    client.set_up()
