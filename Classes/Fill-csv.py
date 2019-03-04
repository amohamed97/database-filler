from Classes.Lab import Lab
from Classes.Lecture import Lecture
from Classes.SchGroup import SchGroup
import pyautogui
from Classes.Tutorial import Tutorial
import msvcrt

groups = []
inp = ''
courseName = ''
courseTerm = ''
instructorName = ''
finish = False


def createTut(tut, group):
    global courseName, inp
    tut.courseName = courseName
    tut.groupNum = group.number
    tut.instName = 'Unknown'
    tut.periodType = 'Tut'
    if checkInp(group, "Tutorial Place: "):
        return True
    tut.place = inp
    clear()
    mainMenu()
    if checkInp(group, "Tutorial type:(1 Or 2) ", 0, 3):
        return True
    tut.type = int(inp)
    clear()
    mainMenu()
    if checkInp(group, "Tutorial Day:(0--->5) ", -1, 6):
        return True
    tut.time.day = int(inp)
    clear()
    mainMenu()
    if checkInp(group, "Tutorial From:(0--->11) ", -1, 12):
        return True
    tut.time.fr = int(inp)
    clear()
    mainMenu()
    if checkInp(group, "Tutorial To:(0--->11) ", -1, 12):
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
    clear()
    mainMenu()
    if checkInp(group, "Lab Type:(1 Or 2) ", 0, 3):
        return True
    lab.type = int(inp)
    clear()
    mainMenu()
    if checkInp(group, "Lab Day:(0--->5) ", -1, 6):
        return True
    lab.time.day = int(inp)
    clear()
    mainMenu()
    if checkInp(group, "Lab From:(0--->11) ", -1, 12):
        return True
    lab.time.fr = int(inp)
    clear()
    mainMenu()
    if checkInp(group, "Lab To:(0--->11) ", -1, 12):
        return True
    lab.time.to = int(inp)
    return False


def modifyGroup(group):
    global inp
    print("1.Group Number      2.Group Lecture      3.Group Tutorials      4.Group Labs      (b).Back")
    inp = input("Which property? ")
    if inp == '1':
        print("Group Number: {}".format(group.number), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Group Number:(1--->6) ")
        while isValidModifying(0, 7) != 'v':
            if inp == 'b':
                print("Invalid number ---> Input must satisfy boundaries")
            elif inp == 'i':
                print("Invalid input")
            print("Group Number: {}".format(group.number), end='   ---->   ')
            inp = input("(n->No change & b->Back) New Group Number:(1--->6) ")
        if inp == 'b':
            clear()
            return modifyGroup(group)
        if inp != 'n':
            group.number = int(inp)
    elif inp == '2':
        clear()
        lectureMenu(group)
    elif inp == '3':
        clear()
        tutorialsMenu(group)
    elif inp == '4':
        clear()
        labsMenu(group)
    elif inp == 'b':
        clear()
        return
    else:
        clear()
        print("Invalid input ---> (1, 2, 3, 4, b)")
        return modifyGroup(group)


def check(group, leftBound, rightBound):
    global inp, courseName, courseTerm, instructorName
    if inp == "1a":
        print("Course Name: {}".format(courseName), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Course's Name: ")
        if inp == 'b' or inp == 'n':
            return True
        courseName = inp
        return True
    elif inp == "2a":
        print("Course Term: {}".format(courseTerm), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Course's Term: ")
        while isValidModifying(0, 11) != 'v':
            if inp == 'b':
                print("Invalid number ---> Input must satisfy boundaries")
            elif inp == 'i':
                print("Invalid input")
            print("Course Term: {}".format(courseTerm), end='   ---->   ')
            inp = input("(n->No change & b->Back) New Course's Term: ")
        if inp == 'b' or inp == 'n':
            return True
        courseTerm = int(inp)
        return True
    elif inp == "3a":
        print("Instructor Name: {}".format(instructorName), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Instructor's Name: ")
        if inp == 'b' or inp == 'n':
            return True
        instructorName = inp
        return True
    elif inp == "5m":
        if len(groups) == 0:
            return 3
        viewGroups()
        return True
    elif inp == "4m":
        clear()
        modifyGroup(group)
        return True
    elif inp == "finish":
        return False
    else:
        return isValidFilling(leftBound, rightBound)


def viewGroups(j=0):
    global inp
    for i in range(len(groups)):
        print("{}.Course Name: {} , instructor Name: {} , group Number: {}".
              format(i + 1, groups[i].lecture.courseName, groups[i].lecture.instName, groups[i].number))
    if j != 0:
        print("Which Group? {}".format(j))
        lastGroupsMenu(j)
    else:
        inp = input("Which Group? ")
        while isValidModifying(0, len(groups) + 1, False) != 'v':
            if inp == 'b':
                print("Invalid number ---> Input must satisfy boundaries")
            elif inp == 'i':
                print("Invalid input")
            inp = input("Which Group? ")
        if inp == 'b':
            return
        i = int(inp)
        lastGroupsMenu(i)


def checkInp(group, inputString, leftBound=None, rightBound=None):
    global finish, inp
    inp = input(inputString)
    ch = check(group, leftBound, rightBound)
    while ch != 2:
        if not ch:
            finish = True
            break
        else:
            clear()
            if ch == 3:
                print("No saved groups yet")
            mainMenu()
            if ch == 'b':
                print("Invalid number ---> Input must satisfy boundaries")
            elif ch == 'i':
                print("Invalid input ---> Input must be number")
            elif ch == 'is':
                print("Invalid input ---> Enter yes Or no")
            inp = input(inputString)
            ch = check(group, leftBound, rightBound)
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
    print("Information of group number {}:".format(len(groups) + 1))


def lastGroupsMenu(i):
    global inp
    print("1. Modify Course Name      2. Modify Course Term      "
          "3. Modify Instructor Name      4. Modify Other Group Info      (b)Back")
    inp = input("Which one? ")
    if inp == '1':
        print("Course Name: {}".format(groups[i - 1].lecture.courseName), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Course's Name: ")
        if inp == 'b':
            clear()
            return viewGroups(i)
        if inp != 'n':
            groups[i - 1].lecture.courseName = inp
    elif inp == '2':
        print("Course Term: {}".format(groups[i - 1].courseTerm), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Course's Term: ")
        while isValidModifying(0, 11) != 'v':
            if inp == 'b':
                print("Invalid number ---> Input must satisfy boundaries")
            elif inp == 'i':
                print("Invalid input")
            print("Course Term: {}".format(groups[i - 1].courseTerm), end='   ---->   ')
            inp = input("(n->No change & b->Back) New Course's Term: ")
        if inp == 'b':
            clear()
            return viewGroups(i)
        if inp != 'n':
            groups[i - 1].courseTerm = int(inp)
    elif inp == '3':
        print("Instructor Name: {}".format(groups[i - 1].lecture.instName), end='   ---->   ')
        inp = input("(n->No change & b->Back) New Instructor's Name: ")
        if inp == 'b':
            clear()
            return viewGroups(i)
        if inp != 'n':
            groups[i - 1].lecture.instName = inp
    elif inp == '4':
        clear()
        return modifyGroup(groups[i - 1])
    elif inp == 'b':
        return viewGroups()
    else:
        print("Invalid input ---> (1, 2, 3, 4, 5, b)")
        return lastGroupsMenu(i)


def tutorialsMenu(group):
    global inp
    if len(group.tutorials) == 0:
        print("No tutorials in this group")
        return modifyGroup(group)
    else:
        print("(b)Back")
        for i in range(len(group.tutorials)):
            print("1.({})Tutorial Place: {}".format(i + 1, group.tutorials[i].place), end="      ")
            print("2.({})Tutorial Type: {}".format(i + 1, group.tutorials[i].type), end="      ")
            print("3.({})Tutorial Day: {}".format(i + 1, group.tutorials[i].time.day), end="      ")
            print("4.({})Tutorial From: {}".format(i + 1, group.tutorials[i].time.fr), end="      ")
            print("5.({})Tutorial To: {}".format(i + 1, group.tutorials[i].time.to))
        i = 0
        if len(group.tutorials) == 2:
            inp = input("Which Tutorial? (1 Or 2) ")
            while isValidModifying(0, 3, False) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                inp = input("Which Tutorial? (1 Or 2) ")
            if inp == 'b':
                clear()
                return modifyGroup(group)
            i = int(inp)
        inp = input("Which property? ")
        if inp == '1':
            inp = input("(n->No change & b->Back) New Tutorial's Place: ")
            if inp == 'b':
                clear()
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i - 1].place = inp
        elif inp == '2':
            inp = input("(n->No change & b->Back) New Tutorial's Type:(1 Or 2) ")
            while isValidModifying(0, 3) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                print("Tutorial Type: {}".format(group.tutorials[i - 1].type), end='   ---->   ')
                inp = input("(n->No change & b->Back) New Tutorial's Type:(1 Or 2) ")
            if inp == 'b':
                clear()
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i - 1].type = int(inp)
        elif inp == '3':
            inp = input("(n->No change & b->Back) New Tutorial's Day:(0--->5) ")
            while isValidModifying(-1, 6) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                print("Tutorial Day: {}".format(group.tutorials[i - 1].time.day), end='   ---->   ')
                inp = input("(n->No change & b->Back) New Tutorial's Day:(0--->5) ")
            if inp == 'b':
                clear()
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i - 1].time.day = int(inp)
        elif inp == '4':
            inp = input("(n->No change & b->Back) New Tutorial's From:(0--->11) ")
            while isValidModifying(-1, 12) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                print("Tutorial From: {}".format(group.tutorials[i - 1].time.fr), end='   ---->   ')
                inp = input("(n->No change & b->Back) New Tutorial's From:(0--->11) ")
            if inp == 'b':
                clear()
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i - 1].time.fr = int(inp)
        elif inp == '5':
            inp = input("(n->No change & b->Back) New Tutorial's To:(0--->11) ")
            while isValidModifying(-1, 12) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                print("Tutorial To: {}".format(group.tutorials[i - 1].time.to), end='   ---->   ')
                inp = input("(n->No change & b->Back) New Tutorial's To:(0--->11) ")
            if inp == 'b':
                clear()
                return tutorialsMenu(group)
            if inp != 'n':
                group.tutorials[i - 1].time.to = int(inp)
        elif inp == 'b':
            clear()
            return modifyGroup(group)
        else:
            print("Invalid input ---> (1, 2, 3, 4, 5, b)")
            return tutorialsMenu(group)


def labsMenu(group):
    global inp
    if len(group.labs) == 0:
        print("No labs in this group")
        return modifyGroup(group)
    else:
        print("(b)Back")
        for i in range(len(group.labs)):
            print("1.({})Lab Place: {}".format(i + 1, group.labs[0].place), end="      ")
            print("2.({})Lab Type: {}".format(i + 1, group.labs[0].type), end="      ")
            print("3.({})Lab Day: {}".format(i + 1, group.labs[0].time.day), end="      ")
            print("4.({})Lab From: {}".format(i + 1, group.labs[0].time.fr), end="      ")
            print("5.({})Lab To: {}".format(i + 1, group.labs[0].time.to))
        i = 1
        if len(group.labs) == 2:
            inp = input("Which Lab? (1 Or 2) ")
            while isValidModifying(0, 3, False) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                inp = input("Which Lab? (1 Or 2) ")
            if inp == 'b':
                clear()
                return modifyGroup(group)
            i = int(inp)
        inp = input("Which property? ")
        if inp == '1':
            inp = input("(n->No change & b->Back) New Lab's Place: ")
            if inp == 'b':
                clear()
                return labsMenu(group)
            if inp != 'n':
                group.labs[i - 1].place = inp
        elif inp == '2':
            inp = input("(n->No change & b->Back) New Lab's Type:(1 Or 2) ")
            while isValidModifying(0, 3) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                print("Lab Type: {}".format(group.labs[i - 1].type), end='   ---->   ')
                inp = input("(n->No change & b->Back) New Lab's Type:(1 Or 2) ")
            if inp == 'b':
                clear()
                return labsMenu(group)
            if inp != 'n':
                group.labs[i - 1].type = int(inp)
        elif inp == '3':
            inp = input("(n->No change & b->Back) New Lab's Day:(0--->5) ")
            while isValidModifying(-1, 6) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                print("Lab Day: {}".format(group.labs[i - 1].time.day), end='   ---->   ')
                inp = input("(n->No change & b->Back) New Lab's Day:(0--->5) ")
            if inp == 'b':
                clear()
                return labsMenu(group)
            if inp != 'n':
                group.labs[i - 1].time.day = int(inp)
        elif inp == '4':
            inp = input("(n->No change & b->Back) New Lab's From:(0--->11) ")
            while isValidModifying(-1, 12) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                print("Lab From: {}".format(group.labs[i - 1].time.fr), end='   ---->   ')
                inp = input("(n->No change & b->Back) New Lab's From:(0--->11) ")
            if inp == 'b':
                clear()
                return labsMenu(group)
            if inp != 'n':
                group.labs[i - 1].time.fr = int(inp)
        elif inp == '5':
            inp = input("(n->No change & b->Back) New Lab's To:(0--->11) ")
            while isValidModifying(-1, 12) != 'v':
                if inp == 'b':
                    print("Invalid number ---> Input must satisfy boundaries")
                elif inp == 'i':
                    print("Invalid input")
                print("Lab To: {}".format(group.labs[i - 1].time.to), end='   ---->   ')
                inp = input("(n->No change & b->Back) New Lab's To:(0--->11) ")
            if inp == 'b':
                clear()
                return labsMenu(group)
            if inp != 'n':
                group.labs[i - 1].time.to = int(inp)
        elif inp == 'b':
            clear()
            return modifyGroup(group)
        else:
            print("Invalid input ---> (1, 2, 3, 4, 5, b)")
            return labsMenu(group)


def isValidFilling(leftBound, rightBound):
    global inp
    if leftBound is None and rightBound is None:  # no validation
        return 2
    while True:
        if type(leftBound) == int and type(rightBound) == int:
            if inp.isdigit():
                if leftBound < int(inp) < rightBound:
                    return 2  # valid number
                else:
                    return 'b'  # invalid number
            else:
                return 'i'  # invalid input
        else:
            if inp == leftBound or inp == rightBound:
                return 2  # valid string
            return 'is'  # invalid input


def isValidModifying(leftBound, rightBound, n=True):
    global inp
    if inp.isdigit():
        if leftBound < int(inp) < rightBound:
            return 'v'  # valid number
        else:
            inp = 'b'  # invalid number
    else:
        if inp == 'b':
            return 'v'  # valid character
        elif inp == 'n':
            if n:
                return 'v'  # n character is valid
            inp = 'i'  # n character is not valid
        else:
            inp = 'i'  # invalid input


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
            clear()
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.place = inp
    elif inp == '2':
        inp = input("(n->No change & b->Back) New Lecture's Type:(1 Or 2) ")
        while isValidModifying(0, 3) != 'v':
            if inp == 'b':
                print("Invalid number ---> Input must satisfy boundaries")
            elif inp == 'i':
                print("Invalid input")
            print("Lecture Type: {}".format(group.lecture.type), end='   ---->   ')
            inp = input("(n->No change & b->Back) New Lecture's Type:(1 Or 2) ")
        if inp == 'b':
            clear()
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.type = int(inp)
    elif inp == '3':
        inp = input("(n->No change & b->Back) New Lecture's Day:(0--->5) ")
        while isValidModifying(-1, 6) != 'v':
            if inp == 'b':
                print("Invalid number ---> Input must satisfy boundaries")
            elif inp == 'i':
                print("Invalid input")
            print("Lecture Day: {}".format(group.lecture.time.day), end='   ---->   ')
            inp = input("(n->No change & b->Back) New Lecture's Day:(0--->5) ")
        if inp == 'b':
            clear()
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.time.day = int(inp)
    elif inp == '4':
        inp = input("(n->No change & b->Back) New Lecture's From:(0--->11) ")
        while isValidModifying(-1, 12) != 'v':
            if inp == 'b':
                print("Invalid number ---> Input must satisfy boundaries")
            elif inp == 'i':
                print("Invalid input")
            print("Lecture From: {}".format(group.lecture.time.fr), end='   ---->   ')
            inp = input("(n->No change & b->Back) New Lecture's From:(0--->11) ")
        if inp == 'b':
            clear()
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.time.fr = int(inp)
    elif inp == '5':
        inp = input("(n->No change & b->Back) New Lecture's To:(0--->11) ")
        while isValidModifying(-1, 12) != 'v':
            if inp == 'b':
                print("Invalid number ---> Input must satisfy boundaries")
            elif inp == 'i':
                print("Invalid input")
            print("Lecture To: {}".format(group.lecture.time.to), end='   ---->   ')
            inp = input("(n->No change & b->Back) New Lecture's To:(0--->11) ")
        if inp == 'b':
            clear()
            return lectureMenu(group)
        if inp != 'n':
            group.lecture.time.to = int(inp)
    elif inp == 'b':
        clear()
        return modifyGroup(group)
    else:
        print("Invalid input ---> (1, 2, 3, 4, 5, b)")
        return lectureMenu(group)


def clear():
    pyautogui.hotkey('ctrl', 'shift', ';')


def filling():
    global courseName, courseTerm, instructorName, inp, finish
    first = True
    while True:
        group = SchGroup()
        lecture = Lecture()
        group.lecture = lecture
        if first:
            mainMenu()
            if checkInp(group, "Course Term:(1--->10) ", 0, 11):
                break
            courseTerm = int(inp)
            clear()
            mainMenu()
            if checkInp(group, "Course Name: "):
                break
            courseName = inp
            clear()
            mainMenu()
            if checkInp(group, "Instructor Name: "):
                break
            instructorName = inp
            first = False
        clear()
        mainMenu()
        if checkInp(group, "Group Number:(1--->6) ", 0, 7):
            break
        group.number = int(inp)
        group.courseTerm = courseTerm
        lecture.groupNum = group.number
        lecture.periodType = 'Lecture'
        lecture.courseName = courseName
        lecture.instName = instructorName
        clear()
        mainMenu()
        if checkInp(group, "Lec place: "):
            break
        lecture.place = inp
        clear()
        mainMenu()
        if checkInp(group, "Lec Type:(1 Or 2) ", 0, 3):
            break
        lecture.type = int(inp)
        clear()
        mainMenu()
        if checkInp(group, "Lec Day:(0--->5) ", -1, 6):
            break
        lecture.time.day = int(inp)
        clear()
        mainMenu()
        if checkInp(group, "Lec From:(0--->11) ", -1, 12):
            break
        lecture.time.fr = int(inp)
        clear()
        mainMenu()
        if checkInp(group, "Lec To:(0--->11) ", -1, 12):
            break
        lecture.time.to = int(inp)
        clear()
        mainMenu()
        if checkInp(group, "Have Tutorial? (yes Or no) ", 'yes', 'no'):
            break
        if inp == "yes":
            clear()
            mainMenu()
            tut = Tutorial()
            if createTut(tut, group):
                break
            group.add_tut(tut)
            clear()
            mainMenu()
            if checkInp(group, "Another Tutorial? (yes Or no) ", 'yes', 'no'):
                break
            if inp == "yes":
                clear()
                mainMenu()
                tut = Tutorial()
                if createTut(tut, group):
                    break
                group.add_tut(tut)

        clear()
        mainMenu()
        if checkInp(group, "Have Lab? (yes Or no) ", 'yes', 'no'):
            break
        if inp == "yes":
            clear()
            mainMenu()
            lab = Lab()
            if createLab(lab, group):
                break
            group.add_lab(lab)
            clear()
            mainMenu()
            if checkInp(group, "Another Lab? (yes Or no) ", 'yes', 'no'):
                break
            if inp == 'yes':
                clear()
                mainMenu()
                lab = Lab()
                if createLab(lab, group):
                    break
                group.add_lab(lab)
        groups.append(group)


def writeFile():
    empty = ",,,,,,,"
    f = open('D:/python/django/Database-Filler/Database.csv', 'w')
    f.write("id,TERM_NUM,NUM,LEC_INST_NAME,LEC_CRS_NAME,LEC_PLACE,LEC_TYPE,LEC_DAY,LEC_FROM,LEC_TO,LEC_PER_TYPE,"
            "TUT1_INST_NAME,"
            "TUT1_CRS_NAME,TUT1_PLACE,TUT1_TYPE,TUT1_DAY,TUT1_FROM,TUT1_TO,TUT1_PER_TYPE,TUT2_INST_NAME,TUT2_CRS_NAME,"
            "TUT2_PLACE,TUT2_TYPE,TUT2_DAY,TUT2_FROM,TUT2_TO,TUT2_PER_TYPE,LAB1_INST_NAME,LAB1_CRS_NAME,LAB1_PLACE,"
            "LAB1_TYPE,LAB1_DAY,LAB1_FROM,LAB1_TO,LAB1_PER_TYPE,LAB2_INST_NAME,LAB2_CRS_NAME,LAB2_PLACE,LAB2_TYPE,"
            "LAB2_DAY,LAB2_FROM,LAB2_TO,LAB2_PER_TYPE\n")
    for i in range(len(groups)):
        f.write('{},{},{},'.format(i + 1, groups[i].number, groups[i].courseTerm))
        f.write('{},{},{},{},{},{},{},{},'.format(groups[i].lecture.instName, groups[i].lecture.courseName,
                                                  groups[i].lecture.place, groups[i].lecture.type,
                                                  groups[i].lecture.time.day, groups[i].lecture.time.fr,
                                                  groups[i].lecture.time.to, groups[i].lecture.periodType))
        if len(groups[i].tutorials) == 0:
            f.write(empty + ",")
            f.write(empty + ",")
        elif len(groups[i].tutorials) == 1:
            f.write(
                '{},{},{},{},{},{},{},{},'.format(groups[i].tutorials[0].instName, groups[i].tutorials[0].courseName,
                                                  groups[i].tutorials[0].place, groups[i].tutorials[0].type,
                                                  groups[i].tutorials[0].time.day, groups[i].tutorials[0].time.fr,
                                                  groups[i].tutorials[0].time.to, groups[i].tutorials[0].periodType))
            f.write(empty + ",")
        else:
            for j in range(2):
                f.write('{},{},{},{},{},{},{},{},'.format(groups[i].tutorials[j].instName,
                                                          groups[i].tutorials[j].courseName,
                                                          groups[i].tutorials[j].place, groups[i].tutorials[0].type,
                                                          groups[i].tutorials[j].time.day,
                                                          groups[i].tutorials[j].time.fr,
                                                          groups[i].tutorials[j].time.to,
                                                          groups[i].tutorials[j].periodType))
        if len(groups[i].labs) == 0:
            f.write(empty + ",")
            f.write(empty + "\n")
        elif len(groups[i].labs) == 1:
            f.write(
                '{},{},{},{},{},{},{},{},'.format(groups[i].labs[0].instName, groups[i].labs[0].courseName,
                                                  groups[i].labs[0].place, groups[i].labs[0].type,
                                                  groups[i].labs[0].time.day, groups[i].labs[0].time.fr,
                                                  groups[i].labs[0].time.to, groups[i].labs[0].periodType))
            f.write(empty + "\n")
        else:
            for j in range(2):
                if j == 0:
                    end = ","
                else:
                    end = "\n"
                f.write('{},{},{},{},{},{},{},{}{}'.format(groups[i].labs[j].instName,
                                                           groups[i].labs[j].courseName,
                                                           groups[i].labs[j].place, groups[i].labs[0].type,
                                                           groups[i].labs[j].time.day,
                                                           groups[i].labs[j].time.fr,
                                                           groups[i].labs[j].time.to,
                                                           groups[i].labs[j].periodType, end))

    f.close()


if __name__ == '__main__':
    print("بسم الله الرحمن الرحيم")
    print("Welcome to Database Filler Application. Let's start the journey")
    filling()
    writeFile()
    print("Information saved to the file successfully")
    print("Congratulations")
