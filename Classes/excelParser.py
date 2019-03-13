import os

import xlrd

from Classes.Lab import Lab
from Classes.Lecture import Lecture
from Classes.SchGroup import SchGroup
from Classes.Tutorial import Tutorial
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tables_path = os.path.join(base_dir, 'tables_excel')
excel_path = os.path.join(tables_path, 'CCE 4th&6th term-Spring 2019 -5-2-2019-converted.xlsx')


wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)

groups = []
course_name = ''
group_number = ''
term_number = ''
day = ''
fr = ''
to = ''


def set_group_number(cell_text):
    global group_number
    if '1' in cell_text:
        group_number = 1
    elif '2' in cell_text:
        group_number = 2
    elif '3' in cell_text:
        group_number = 3
    elif '4' in cell_text:
        group_number = 4
    elif '5' in cell_text:
        group_number = 5
    elif '6' in cell_text:
        group_number = 6
    return


def set_term_number(cell_text):
    global term_number
    if cell_text.startswith('1'):
        term_number = 1
    elif cell_text.startswith('2'):
        term_number = 2
    elif cell_text.startswith('3'):
        term_number = 3
    elif cell_text.startswith('4'):
        term_number = 4
    elif cell_text.startswith('5'):
        term_number = 5
    elif cell_text.startswith('6'):
        term_number = 6
    elif cell_text.startswith('7'):
        term_number = 7
    elif cell_text.startswith('8'):
        term_number = 8
    elif cell_text.startswith('9'):
        term_number = 9
    elif cell_text.startswith('10'):
        term_number = 10
    elif cell_text.startswith('Hu'):
        term_number = 11
    return


def set_day(cell_text):
    global day
    if cell_text.startswith("Sa"):
        day = 0
    elif cell_text.startswith("Su"):
        day = 1
    elif cell_text.startswith("Mo"):
        day = 2
    elif cell_text.startswith("Tu"):
        day = 3
    elif cell_text.startswith("Wed"):
        day = 4
    elif cell_text.startswith("Th"):
        day = 5
    return


def set_from_to(cell_text):
    global fr, to
    if cell_text.startswith("1-") or cell_text.startswith("1 -"):
        fr = 0
        to = 1
    elif cell_text.startswith("3-") or cell_text.startswith("3 -"):
        fr = 2
        to = 3
    elif cell_text.startswith("5-")or cell_text.startswith("5 -"):
        fr = 4
        to = 5
    elif cell_text.startswith("7-")or cell_text.startswith("7 -"):
        fr = 6
        to = 7
    elif cell_text.startswith("9-")or cell_text.startswith("9 -"):
        fr = 8
        to = 9
    elif cell_text.startswith("11-")or cell_text.startswith("11 -"):
        fr = 10
        to = 11
    return


def set_course_name(name):
    if name.startswith("Digital LogicI") or name.startswith("Digital Logic Circuits I"):
        return "Digital Logic Circuits 1"
    elif name.startswith("Programming II"):
        return "Programming 2"
    elif name.startswith("Data Structures") or name.startswith("Data Structure I"):
        return "Data Structures 1"
    elif name.startswith("Circuits II ") or name.startswith("Electrical Circuits II"):
        return "Electrical Circuits 2"
    elif name.startswith("Math (IV) I") or name.startswith("Math (IV)"):
        return "Math 4"


def check_course_name(group_courses):
    global course_name
    if course_name not in group_courses:
        group_courses[course_name] = SchGroup(True)
        group_courses[course_name].number = group_number
        group_courses[course_name].courseTerm = term_number
    return group_courses[course_name]


def check_cell_case(left_up, left_down, right_up, right_down, row=None):
    if left_up != '' and left_down == '' and right_up == '' and right_down == '' and row != sheet.nrows:
        return 1
    elif left_up != '' and left_down != '' and right_up == '' and right_down == '':
        return 2
    elif left_up != '' and left_down != '' and right_up != '' and right_down != '':
        return 3
    elif left_up == '' and left_down == '' and right_up != '' and right_down != '':
        return 4
    else:
        return 5


def create_lab(group, lab_type, right=False):
    global course_name, group_number, day, fr, to
    lab = Lab()
    lab.courseName = course_name
    lab.groupNum = group_number
    lab.instName = 'Unknown'
    lab.periodType = 'Lab'
    lab.place = 'Lab'
    lab.type = lab_type
    lab.time.day = day
    lab.time.fr = fr
    lab.time.to = fr
    if right:
        lab.time.fr = to
        lab.time.to = to
    group.add_lab(lab)
    if lab_type == 2:
        lab = Lab()
        lab.courseName = course_name
        lab.groupNum = group_number
        lab.instName = 'Unknown'
        lab.periodType = 'Lab'
        lab.place = 'Lab'
        lab.type = lab_type
        lab.time.day = day
        lab.time.fr = to
        lab.time.to = to
        group.add_lab(lab)


def create_tutorial(group, place, tut_type, right=False):
    global course_name, group_number, day, fr, to
    tut = Tutorial()
    tut.courseName = course_name
    tut.groupNum = group_number
    tut.instName = 'Unknown'
    tut.periodType = 'Tut'
    tut.place = place
    tut.type = tut_type
    tut.time.day = day
    tut.time.fr = fr
    tut.time.to = fr
    if right:
        tut.time.fr = to
        tut.time.to = to
    group.add_tut(tut)
    if tut_type == 2:
        tut = Tutorial()
        tut.courseName = course_name
        tut.groupNum = group_number
        tut.instName = 'Unknown'
        tut.periodType = 'Tut'
        tut.place = place
        tut.type = tut_type
        tut.time.day = day
        tut.time.fr = to
        tut.time.to = to
        group.add_tut(tut)


def check_lecture_completion_or_extension(row, col, case=1):
    global course_name
    previous = sheet.cell_value(row - 2, col)
    next_cell = sheet.cell_value(row + 2, col)
    if 'lec' in previous.lower():
        crs_name = set_course_name(previous.split('-')[0])
        if crs_name.startswith(course_name):
            return 1
    if case == 2:
        next_cell = sheet.cell_value(row + 1, col)
    if 'lec' in next_cell.lower():
        crs_name = set_course_name(next_cell.split('-')[0])
        if crs_name.startswith(course_name):
            return 2
    return 3


def check_place(cell_text):
    cell_text_content = cell_text.split('-')
    if 'Place' in cell_text_content[-1]:
        if ':' in cell_text_content[-1]:
            place = cell_text_content[-1].split(':')[-1]
        else:
            place = cell_text_content[-1][cell_text_content[-1].find('Place') + 5:]
    else:
        place = cell_text_content[-1]
    if place.isdigit():
        place = 'Class ' + place
    return place.strip()


def add_lecture_extension(group, place):
    group.lecExPlace = place
    group.lecExDay = day
    group.lecExFrom = fr
    group.lecExTo = to


def add_lecture(group, row, col, case=False):
    global course_name, group_number, day, fr, to
    main_lecture = sheet.cell_value(row, col)
    lecture = group.lecture
    lecture.instName = main_lecture[main_lecture.find('Dr'):]
    lecture.place = check_place(sheet.cell_value(row + 1, col))
    lecture.courseName = course_name
    lecture.groupNum = group_number
    lecture.type = 1
    lecture.periodType = 'Lecture'
    lecture.time.day = day
    if case:
        lecture.time.fr = fr
        lecture.time.to = to
    else:
        lecture.time.fr = to
        set_from_to(sheet.cell_value(row, 1))
        lecture.time.to = to


def write_file():
    file_path = os.path.join(base_dir, 'ExcelParser.csv')
    empty = ",,,,,,,"
    f = open(file_path, 'w')
    for group in groups:
        f.write('{},{},{},'.format(group.courseTerm, group.creditHours, group.number))
        f.write('{},{},{},{},{},{},{},{},{},{},{},{},'.format(group.lecture.instName, group.lecture.courseName,
                                                              group.lecture.place, group.lecture.type,
                                                              group.lecture.time.day, group.lecture.time.fr,
                                                              group.lecture.time.to, group.lecExPlace, group.lecExDay,
                                                              group.lecExFrom, group.lecExTo,
                                                              group.lecture.periodType))
        if len(group.tutorials) == 0:
            f.write(empty + ",")
            f.write(empty + ",")
        elif len(group.tutorials) == 1:
            f.write(
                '{},{},{},{},{},{},{},{},'.format(group.tutorials[0].instName, group.tutorials[0].courseName,
                                                  group.tutorials[0].place, group.tutorials[0].type,
                                                  group.tutorials[0].time.day, group.tutorials[0].time.fr,
                                                  group.tutorials[0].time.to, group.tutorials[0].periodType))
            f.write(empty + ",")
        else:
            for j in range(2):
                f.write('{},{},{},{},{},{},{},{},'.format(group.tutorials[j].instName,
                                                          group.tutorials[j].courseName,
                                                          group.tutorials[j].place, group.tutorials[0].type,
                                                          group.tutorials[j].time.day,
                                                          group.tutorials[j].time.fr,
                                                          group.tutorials[j].time.to,
                                                          group.tutorials[j].periodType))
        if len(group.labs) == 0:
            f.write(empty + ",")
            f.write(empty + "\n")
        elif len(group.labs) == 1:
            f.write(
                '{},{},{},{},{},{},{},{},'.format(group.labs[0].instName, group.labs[0].courseName,
                                                  group.labs[0].place, group.labs[0].type,
                                                  group.labs[0].time.day, group.labs[0].time.fr,
                                                  group.labs[0].time.to, group.labs[0].periodType))
            f.write(empty + "\n")
        else:
            for j in range(2):
                if j == 0:
                    end = ","
                else:
                    end = "\n"
                f.write('{},{},{},{},{},{},{},{}{}'.format(group.labs[j].instName,
                                                           group.labs[j].courseName,
                                                           group.labs[j].place, group.labs[0].type,
                                                           group.labs[j].time.day,
                                                           group.labs[j].time.fr,
                                                           group.labs[j].time.to,
                                                           group.labs[j].periodType, end))
    f.close()


def extract_table():
    global group_number, term_number, course_name, day, fr, to
    col = 3
    group_courses = {}  # courses in the same group (vertically) in the table
    while col < sheet.ncols:
        set_group_number(sheet.cell_value(2, col))
        set_term_number(sheet.cell_value(1, col))
        row = 4
        while row < sheet.nrows:
            left_up = sheet.cell_value(row, col)
            right_up = sheet.cell_value(row, col + 1)
            left_down = None
            right_down = None
            if row != sheet.nrows - 1:
                left_down = sheet.cell_value(row + 1, col)
                right_down = sheet.cell_value(row + 1, col + 1)
            case = check_cell_case(left_up, left_down, right_up, right_down, row)
            set_day(sheet.cell_value(row, 0))
            if case == 5:
                row += 1
                continue
            set_from_to(sheet.cell_value(row, 1))
            if case == 4:
                course_name = right_up.split('-')[0]
            else:
                course_name = left_up.split('-')[0]
            course_name = set_course_name(course_name)
            group = check_course_name(group_courses)
            if check_cell_case(left_up, left_down, right_up, right_down) == 1:
                if 'lab' in left_up.lower():
                    create_lab(group, 2)
                elif 'tut' in left_up.lower():
                    place = check_place(left_up)
                    create_tutorial(group, place, 2)
                elif 'lec' in left_up.lower():
                    if check_lecture_completion_or_extension(row, col) == 1:
                        group.lecture.time.to = fr
                    elif check_lecture_completion_or_extension(row, col) == 2:
                        row += 2
                        add_lecture(group, row, col)
                    elif check_lecture_completion_or_extension(row, col) == 3:
                        place = check_place(left_up)
                        add_lecture_extension(group, place)
            elif check_cell_case(left_up, left_down, right_up, right_down) == 2:
                if 'lec' not in left_up.lower() and 'lec' not in left_down.lower():
                    if 'tut' in left_up.lower():
                        if 'place' in left_down.lower() and 'tut' not in left_down.lower() \
                                and 'lab' not in left_down.lower():
                            place = check_place(left_down)
                            create_tutorial(group, place, 1)
                            row += 2
                            continue
                        else:
                            place = check_place(left_up)
                            create_tutorial(group, place, 2)
                    elif 'lab' in left_up.lower():
                        if 'place' in left_down.lower() and 'tut' not in left_down.lower() \
                                and 'lab' not in left_down.lower():
                            create_lab(group, 1)
                            row += 2
                            continue
                        else:
                            create_lab(group, 2)
                    course_name = left_down.split('-')[0]
                    course_name = set_course_name(course_name)
                    group = check_course_name(group_courses)
                    if 'tut' in left_down.lower():
                        place = check_place(left_down)
                        create_tutorial(group, place, 2)
                    elif 'lab' in left_down.lower():
                        create_lab(group, 2)
                elif 'lec' in left_up.lower() and 'lec' not in left_down.lower():
                    if left_down.startswith('Place'):
                        add_lecture(group, row, col, True)
                    elif check_lecture_completion_or_extension(row, col) == 1:
                        group.lecture.time.to = fr
                    elif check_lecture_completion_or_extension(row, col) == 3:
                        place = check_place(left_up)
                        add_lecture_extension(group, place)
                    if 'tut' in left_down.lower():
                        place = check_place(left_down)
                        create_tutorial(group, place, 2)
                    elif 'lab' in left_down.lower():
                        create_lab(group, 2)
                elif 'lec' not in left_up.lower() and 'lec' in left_down.lower():
                    if 'tut' in left_up.lower():
                        place = check_place(left_up)
                        create_tutorial(group, place, 2)
                    elif 'lab' in left_up.lower():
                        create_lab(group, 2)
                    if check_lecture_completion_or_extension(row + 1, col, 2) == 2:
                        row += 2
                        add_lecture(group, row, col)
                    elif check_lecture_completion_or_extension(row + 1, col, 2) == 3:
                        place = check_place(left_down)
                        add_lecture_extension(group, place)
                elif 'lec' in left_up.lower() and 'lec' in left_down.lower():
                    if check_lecture_completion_or_extension(row, col) == 1:
                        group.lecture.time.to = fr
                    elif check_lecture_completion_or_extension(row, col) == 3:
                        place = check_place(left_up)
                        add_lecture_extension(group, place)
                    if check_lecture_completion_or_extension(row + 1, col, 2) == 2:
                        row += 2
                        add_lecture(group, row, col)
                    elif check_lecture_completion_or_extension(row + 1, col, 2) == 3:
                        place = check_place(left_down)
                        add_lecture_extension(group, place)
            elif check_cell_case(left_up, left_down, right_up, right_down) == 3:
                if 'tut' in left_up.lower():
                    place = check_place(left_down)
                    create_tutorial(group, place, 1)
                elif 'lab' in left_up.lower():
                    create_lab(group, 1)
                course_name = right_up.split('-')[0]
                course_name = set_course_name(course_name)
                group = check_course_name(group_courses)
                if 'tut' in right_up.lower():
                    place = check_place(right_down)
                    create_tutorial(group, place, 1, True)
                elif 'lab' in right_up.lower():
                    create_lab(group, 1, True)
            elif check_cell_case(left_up, left_down, right_up, right_down) == 4:
                if 'tut' in right_up.lower():
                    place = check_place(right_down)
                    create_tutorial(group, place, 1, True)
                elif 'lab' in right_up.lower():
                    create_lab(group, 1, True)
            row += 1
            set_day(sheet.cell_value(row, 0))
            row += 1
        col += 2
        for group in group_courses.values():
            groups.append(group)
        group_courses.clear()
        write_file()


if __name__ == '__main__':
    extract_table()
    # write_file()
    print("Information saved in the file successfully")
    print("Parsing Done")
