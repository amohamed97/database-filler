from Classes.Course import Course
from Classes.Instructor import Instructor
from Classes.Lab import Lab
from Classes.Lecture import Lecture
from Classes.SchGroup import SchGroup
import os
import subprocess
import sys

from Classes.Tutorial import Tutorial
from . import *

groups = []
inp = ''
courseName = ''
courseTerm = ''
instructorName = ''
finish = False
# def clear():
#     os.system('cls ' if os.name == 'nt' else 'clear')
#
#
# cls = subprocess.call('cls', shell=True)


def createTut(tut, group):
    global courseName, inp
    tut.courseName = courseName
    tut.groupNum = group.number
    tut.instName = 'Unknown'
    tut.periodType = 'Tut'
    if checkInp(group, "Tutorial Place: "):
        return True
    tut.place = inp
    if checkInp(group, "Tutorial type: "):
        return True
    tut.type = int(inp)
    if checkInp(group, "Tutorial Day: "):
        return True
    tut.time.day = int(inp)
    if checkInp(group, "Tutorial From: "):
        return True
    tut.time.fr = int(inp)
    if checkInp(group, "Tutorial To: "):
        return True
    tut.time.to = int(inp)
    return False


def createLab(lab, group):
    global courseName, inp
    lab.courseName = courseName
    lab.groupNum = group.number
    lab.instName = 'Unknown'
    lab.periodType = 'Lab'
    if checkInp(group, "Lab Place: "):
        return True
    lab.place = inp
    if checkInp(group, "Lab Type: "):
        return True
    lab.type = int(inp)
    if checkInp(group, "Lab Day: "):
        return True
    lab.time.day = int(inp)
    if checkInp(group, "Lab From: "):
        return True
    lab.time.fr = int(inp)
    if checkInp(group, "Lab To: "):
        return True
    lab.time.to = int(inp)
    return False


def modifyGroup(group):
    global inp
    print("1.Group Number      2.Group Lecture      3.Group Tutorials      4.Group Labs      (b).Back")
    inp = input("Which property? ")
    if inp == '1':
        print("Group Number: {}".format(group.number), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Group Number: ")
        if inp == 'b':
            return modifyGroup(group)
        if inp != 'n':
            group.number = int(inp)
    elif inp == '2':
        lectureMenu(group)
    elif inp == '3':
        tutorialsMenu(group)
    elif inp == '4':
        labsMenu(group)
    elif inp == 'b':
        return


def check(group):
    global inp, courseName, courseTerm, instructorName
    if inp == "1a":
        print("Course Name: {}".format(courseName), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Course's Name: ")
        if inp == 'b':
            return True
        if inp != 'n':
            courseName = inp
        return True
    elif inp == "2a":
        print("Course Term: {}".format(courseTerm), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Course's Term: ")
        if inp == 'b':
            return True
        if inp != 'n':
            courseTerm = int(inp)
        return True
    elif inp == "3a":
        print("Instructor Name: {}".format(instructorName), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Instructor's Name: ")
        if inp == 'b':
            return True
        if inp != 'n':
            instructorName = inp
        return True
    elif inp == "5m":
        viewGroups()
        return True
    elif inp == "4m":
        modifyGroup(group)
        return True
    elif inp == "finish":
        return False
    else:
        return 2


def viewGroups():
    global inp
    if len(groups) == 0:
        print("No saved groups yet")
    else:
        for i in range(len(groups)):
            print("{}.Course Name: {} , instructor Name: {} , group Number: {}".
                  format(i+1, groups[i].lecture.courseName, groups[i].lecture.instName, groups[i].number))
        inp = input("Which Group? ")
        i = int(inp)
        modifyGroup(groups[i-1])


def checkInp(group, inputString):
    global finish, inp
    inp = input(inputString)
    ch = check(group)
    while ch != 2:
        if not ch:
            finish = True
            break
        else:
            inp = input(inputString)
            ch = check(group)
    if finish:
        return True
    return False


def mainMenu():
    print('1. Modify Course Name -----------> 1a')
    print('2. Modify Course Term -----------> 2a')
    print('3. Modify Instructor Name -------> 3a')
    print("4. Modify Group Info-------------> 4m")
    print("5. Modify last groups------------> 5m")
    print('6. Finish -----------------------> finish')


def tutorialsMenu(group):
    global inp
    if len(group.tutorials) == 0:
        print("No tutorials in this group")
    else:
        print("(b)Back")
        for i in range(len(group.tutorials)):
            print("1.({})Tutorial Place: {}".format(i+1, group.tutorials[i].place), end="      ")
            print("2.({})Tutorial Type: {}".format(i+1, group.tutorials[i].type), end="      ")
            print("3.({})Tutorial Day: {}".format(i+1, group.tutorials[i].time.day), end="      ")
            print("4.({})Tutorial From: {}".format(i+1, group.tutorials[i].time.fr), end="      ")
            print("5.({})Tutorial To: {}".format(i+1, group.tutorials[i].time.to))
        i = 0
        if len(group.tutorials) == 2:
            inp = input("Which Tutorial? (1 Or 2) ")
            if inp == 'b':
                return modifyGroup(group)
            i = int(inp)
        inp = input("Which property? ")
        if inp == '1':
            inp = input("(n->No change & b->Back) New Tutorial's Place: ")
            if inp == 'b':
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i-1].place = inp
        elif inp == '2':
            inp = input("(n->No change & b->Back) New Tutorial's Type: ")
            if inp == 'b':
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i-1].type = int(inp)
        elif inp == '3':
            inp = input("(n->No change & b->Back) New Tutorial's Day: ")
            if inp == 'b':
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i-1].time.day = int(inp)
        elif inp == '4':
            inp = input("(n->No change & b->Back) New Tutorial's From: ")
            if inp == 'b':
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i-1].time.fr = int(inp)
        elif inp == '5':
            inp = input("(n->No change & b->Back) New Tutorial's To: ")
            if inp == 'b':
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i-1].time.to = int(inp)
        elif inp == 'b':
            return modifyGroup(group)


def labsMenu(group):
    global inp
    if len(group.labs) == 0:
        print("No labs in this group")
    else:
        print("(b)Back")
        for i in range(len(group.labs)):
            print("1.({})Lab Place: {}".format(i+1, group.labs[0].place), end="      ")
            print("2.({})Lab Type: {}".format(i+1, group.labs[0].type), end="      ")
            print("3.({})Lab Day: {}".format(i+1, group.labs[0].time.day), end="      ")
            print("4.({})Lab From: {}".format(i+1, group.labs[0].time.fr), end="      ")
            print("5.({})Lab To: {}".format(i+1, group.labs[0].time.to))
        i = 0
        if len(group.labs) == 2:
            inp = input("Which Lab? (1 Or 2) ")
            if inp == 'b':
                return modifyGroup(group)
            i = int(inp)
        inp = input("Which property? ")
        if inp == '1':
            inp = input("(n->No change & b->Back) New Lab's Place: ")
            if inp == 'b':
                return labsMenu(group)
            if inp != 'n':
                group.labs[i-1].place = inp
        elif inp == '2':
            inp = input("(n->No change & b->Back) New Lab's Type: ")
            if inp == 'b':
                return labsMenu(group)
            if inp != 'n':
                group.labs[i-1].type = int(inp)
        elif inp == '3':
            inp = input("(n->No change & b->Back) New Lab's Day: ")
            if inp == 'b':
                return labsMenu(group)
            if inp != 'n':
                group.labs[i-1].time.day = int(inp)
        elif inp == '4':
            inp = input("(n->No change & b->Back) New Lab's From: ")
            if inp == 'b':
                return labsMenu(group)
            if inp != 'n':
                group.labs[i-1].time.fr = int(inp)
        elif inp == '5':
            inp = input("(n->No change & b->Back) New Lab's To: ")
            if inp == 'b':
                return labsMenu(group)
            if inp != 'n':
                group.labs[i-1].time.to = int(inp)
        elif inp == 'b':
            return modifyGroup(group)


def lectureMenu(group):
    global inp
    print("(b)Back")
    print("1.Lecture Place: {}".format(group.lecture.place), end="      ")
    print("2.Lecture Type: {}".format(group.lecture.type), end="      ")
    print("3.Lecture Day: {}".format(group.lecture.time.day), end="      ")
    print("4.Lecture From: {}".format(group.lecture.time.fr), end="      ")
    print("5.Lecture To: {}".format(group.lecture.time.to))
    inp = input("Which property? ")
    if inp == '1':
        inp = input("(n->No change & b->Back) New Lecture's Place: ")
        if inp == 'b':
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.place = inp
    elif inp == '2':
        inp = input("(n->No change & b->Back) New Lecture's Type: ")
        if inp == 'b':
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.type = int(inp)
    elif inp == '3':
        inp = input("(n->No change & b->Back) New Lecture's Day: ")
        if inp == 'b':
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.time.day = int(inp)
    elif inp == '4':
        inp = input("(n->No change & b->Back) New Lecture's From: ")
        if inp == 'b':
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.time.fr = int(inp)
    elif inp == '5':
        inp = input("(n->No change & b->Back) New Lecture's To: ")
        if inp == 'b':
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.time.to = int(inp)
    elif inp == 'b':
        return modifyGroup(group)

def clear():
    print('\n'*100)
def filling():
    global courseName, courseTerm, instructorName, inp, finish
    first = True
    while True:
        if first:
            courseTerm = int(input("Course Term: "))
            courseName = input("Course Name: ")
            instructorName = input("Instructor Name: ")
            first = False
        # clear()
        mainMenu()
        print("Group Information:")
        group = SchGroup()
        lecture = Lecture()
        group.lecture = lecture
        if checkInp(group, "Group Number: "):
            break
        group.number = int(inp)
        group.courseTerm = courseTerm
        lecture.groupNum = group.number
        lecture.periodType = 'Lecture'
        lecture.courseName = courseName
        lecture.instName = instructorName
        if checkInp(group, "Lec place: "):
            break
        lecture.place = inp
        if checkInp(group, "Lec Type: "):
            break
        lecture.type = int(inp)
        if checkInp(group, "Lec Day: "):
            break
        lecture.time.day = int(inp)
        if checkInp(group, "Lec From: "):
            break
        lecture.time.fr = int(inp)
        if checkInp(group, "Lec To: "):
            break
        lecture.time.to = int(inp)
        if checkInp(group, "Have Tutorial? (yes Or no) "):
            break
        if inp == "yes":
            tut = Tutorial()
            if createTut(tut, group):
                break
            group.add_tut(tut)
            if checkInp(group, "Another Tutorial? (yes Or no) "):
                break
            if inp == "yes":
                tut = Tutorial()
                if createTut(tut, group):
                    break
                group.add_tut(tut)
        if checkInp(group, "Have Lab? (yes Or no) "):
            break
        if inp == "yes":
            lab = Lab()
            if createLab(lab, group):
                break
            group.add_lab(lab)
            if checkInp(group, "Another Lab? (yes Or no) "):
                break
            if inp == 'yes':
                lab = Lab()
                if createLab(lab, group):
                    break
                group.add_lab(lab)
        groups.append(group)


if __name__ == '__main__':
    print("Welcome to Database Filler Application. Let's start the journey")
    filling()
    print("Congratulations")


