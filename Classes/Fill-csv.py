from Classes.Course import Course
from Classes.Instructor import Instructor
from Classes.Lab import Lab
from Classes.Lecture import Lecture
from Classes.SchGroup import SchGroup
import os
import subprocess

from Classes.Tutorial import Tutorial
from . import *

courses = []
sameTerm = True
sameCourse = True
sameInstructor = True
first = True


# def clear():
#     os.system('cls ' if os.name == 'nt' else 'clear')
#
#
# cls = subprocess.call('cls', shell=True)


def createTut(tut, courseName, groupNum):
    tut.courseName = courseName
    tut.groupNum = groupNum
    tut.instName = 'Unknown'
    tut.periodType = 'Tut'
    tut.place = input("Tutorial Place: ")
    tut.time.day = input("Tutorial Day: ")
    tut.time.fr = input("Tutorial From: ")
    tut.time.to = input("Tutorial To: ")


def createLab(lab, courseName, groupNum):
    lab.courseName = courseName
    lab.groupNum = groupNum
    lab.instName = 'Unknown'
    lab.periodType = 'Tut'
    lab.place = input("Tutorial Place: ")
    lab.time.day = input("Tutorial Day: ")
    lab.time.fr = input("Tutorial From: ")
    lab.time.to = input("Tutorial To: ")


def filling():
    course = Course()
    instructor = Instructor()
    global first
    global sameTerm
    global sameCourse
    global sameInstructor
    while True:
        if first:
            course.term = int(input("Course Term: "))
            course.name = input("Course Name: ")
            instructor.name = input("Instructor Name: ")
            instructor.courseName = course.name
            first = False
        else:
            if not sameCourse:
                courses.append(course)
                course = Course()
                course.name = input("Course Name: ")
                sameCourse = True
            if not sameTerm:
                course.term = int(input("Course Term: "))
                sameTerm = True
            if not sameInstructor:
                instructor = Instructor()
                instructor.name = input("Instructor Name: ")
                sameInstructor = True
        instructor.courseName = course.name
        group = SchGroup()
        lecture = Lecture()
        print('1. Another Course --------> 1a')
        print('2. Another Term ----------> 2a')
        print('3. Another Instructor ----> 3a')
        print('4. Finish ----------------> f')
        print("Group info:")
        group.number = input("Group Number: ")
        if group.number == "1a":
            sameCourse = False
            continue
        elif group.number == "2a":
            sameTerm = False
            continue
        elif group.number == "3a":
            sameInstructor = False
            continue
        elif group.number == "f":
            break
        group.number = int(group.number)
        lecture.groupNum = group.number
        lecture.periodType = 'Lecture'
        lecture.courseName = course.name
        lecture.instName = instructor.name
        lecture.place = input("Lec place: ")
        lecture.type = int(input("Lec Type: "))
        lecture.time.day = int(input("Lec Day: "))
        lecture.time.fr = int(input("Lec From: "))
        lecture.time.to = int(input("Lec To: "))
        group.lecture = lecture
        checkTut = input("Have Tutorial? ")
        if checkTut == "yes":
            tut = Tutorial()
            createTut(tut, lecture.courseName, lecture.groupNum)
            group.add_tut(tut)
            checkTut = input("Another Tutorial? ")
            if checkTut == "yes":
                tut = Tutorial()
                createTut(tut, lecture.courseName, lecture.groupNum)
                group.add_tut(tut)
        checkLab = input("Have Lab?")
        if checkLab == "yes":
            lab = Lab()
            createLab(lab, lecture.courseName, lecture.groupNum)
            group.add_lab(lab)
            checkLab = input("Another Lab? ")
            if checkLab == 'yes':
                lab = Lab()
                createLab(lab, lecture.courseName, lecture.groupNum)
                group.add_lab(lab)
        instructor.add_group(group)
        course.add_instructor(instructor)


if __name__ == '__main__':
    print("Welcome to Database Filler Application. Let's start the journey")
    filling()
    print("Congratulations")


