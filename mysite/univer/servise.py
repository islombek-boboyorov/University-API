from django.db import connection
from contextlib import closing
from collections import OrderedDict


def get_university(univ_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_university where id = %s""", [univ_id])
        univ = dict_fetchone(cursor)
    return univ


def get_universitys():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_university""")
        univ = dict_fetchall(cursor)
    return univ


def get_faculty(fac_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_faculty.*, univer_university.id as univer_id, univer_university.name as univer_name
                 from univer_faculty left join univer_university on
                  univer_faculty.university_id=univer_university.id where univer_faculty.id = %s""", [fac_id])
        fac = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', fac['id']),
                ('name', fac['name']),
                ('university', OrderedDict(
                    [
                        ('id', fac['univer_id']),
                        ('name', fac['univer_name']),
                    ]
                )),
            ]
        )


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_faculty.*, univer_university.id as univer_id, univer_university.name as univer_name
         from univer_faculty left join univer_university on
          univer_faculty.university_id=univer_university.id""")
        facs = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', fac['id']),
                ('name', fac['name']),
                ('university', OrderedDict(
                    [
                        ('id', fac['univer_id']),
                        ('name', fac['univer_name']),
                    ]
                )),
            ]
        ) for fac in facs]


def get_chair(car_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_chair.*, univer_faculty.id as faculty_id, univer_faculty.name as faculty_name
        from univer_chair left join univer_faculty on univer_chair.faculty_id=univer_faculty.id
        where univer_chair.id = %s""", [car_id])
        char = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', char['id']),
                ('name', char['name']),
                ('faculty', OrderedDict(
                    [
                        ('id', char['faculty_id']),
                        ('name', char['faculty_name'])
                    ]
                )),
            ]
        )


def get_chairs():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_chair.*, univer_faculty.id as faculty_id, univer_faculty.name as faculty_name
           from univer_chair left join univer_faculty on univer_chair.faculty_id=univer_faculty.id""")
        chairs = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', chair['id']),
                ('name', chair['name']),
                ('faculty', OrderedDict(
                    [
                        ('id', chair['faculty_id']),
                        ('name', chair['faculty_name']),
                    ]
                )),
            ]
        ) for chair in chairs ]


def get_group(group_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_group.*, univer_chair.id as chair_id, univer_chair.name as chair_name,
         univer_faculty.id as faculty_id, univer_faculty.name as faculty_name, univer_university.id as univ_id, 
         univer_university.name as univ_name from univer_group left join univer_chair 
         on univer_group.chair_id=univer_chair.id left join univer_faculty on univer_group.faculty_id=univer_faculty.id
         left join univer_university on univer_group.university_id=univer_university.id 
         where univer_group.id = %s""", [group_id])
        group = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', group['id']),
                ('number', group['number']),
                ('teacher_name', group['teacher_name']),
                ('pupil_count', group['pupil_count']),
                ('chair', OrderedDict(
                    [
                        ('id', group['chair_id']),
                        ('name', group['chair_name']),
                        ('faculty', OrderedDict(
                            [
                                ('id', group['faculty_id']),
                                ('name', group['faculty_name']),
                                ('university', OrderedDict(
                                    [
                                        ('id', group['univ_id']),
                                        ('name', group['univ_name']),
                                    ]
                                )),
                            ]
                        )),
                    ]
                )),
            ]
        )


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_group.*, univer_chair.id as chair_id, univer_chair.name as chair_name,
         univer_faculty.id as faculty_id, univer_faculty.name as faculty_name, univer_university.id as univ_id,
          univer_university.name as univ_name from univer_group left join univer_chair
          on univer_chair.id=univer_group.chair_id left join univer_faculty on univer_group.faculty_id=univer_faculty.id
          left join univer_university on univer_group.university_id=univer_university.id""")
        groups = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', group['id']),
                ('number', group['number']),
                ('teacher_name', group['teacher_name']),
                ('pupil_count', group['pupil_count']),
                ('chair', OrderedDict(
                    [
                        ('id', group['chair_id']),
                        ('name', group['chair_name']),
                        ('faculty', OrderedDict(
                            [
                                ('id', group['faculty_id']),
                                ('name', group['faculty_name']),
                                ('university', OrderedDict(
                                    [
                                        ('id', group['univ_id']),
                                        ('name', group['univ_name']),
                                    ]
                                )),
                            ]
                        )),
                    ]
                )),
            ]
        ) for group in groups]


def get_teacher(teach_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_teacher.*, univer_chair.id as chair_id, univer_chair.name as chair_name,
        univer_faculty.id as faculty_id, univer_faculty.name as faculty_name, univer_university.id as univ_id,
        univer_university.name as univ_name from univer_teacher left join univer_chair on
        univer_teacher.chair_id=univer_chair.id left join univer_faculty on 
        univer_teacher.faculty_id=univer_faculty.id left join univer_university on
        univer_teacher.university_id=univer_university.id where univer_teacher.id = %s""", [teach_id])
        teacher = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', teacher['id']),
                ('name', teacher['name']),
                ('subject', teacher['subject']),
                ('university', OrderedDict(
                    [
                        ('id', teacher['univ_id']),
                        ('name', teacher['univ_name']),
                    ]
                )),
                ('faculty', OrderedDict(
                    [
                        ('id', teacher['faculty_id']),
                        ('name', teacher['faculty_name']),
                        ('university', OrderedDict(
                            [
                                ('id', teacher['univ_id']),
                                ('name', teacher['univ_name']),
                            ]
                        )),
                    ]
                )),
                ('chair', OrderedDict(
                    [
                        ('id', teacher['chair_id']),
                        ('name', teacher['chair_name']),
                        ('faculty', OrderedDict(
                            [
                                ('id', teacher['faculty_id']),
                                ('name', teacher['faculty_name']),
                                ('university', OrderedDict(
                                    [
                                        ('id', teacher['univ_id']),
                                        ('name', teacher['univ_name']),
                                    ]
                                )),
                            ]
                        )),
                    ]
                )),
            ]
        )


def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_teacher.*, univer_chair.id as chair_id, univer_chair.name as chair_name,
        univer_faculty.id as faculty_id, univer_faculty.name as faculty_name, univer_university.id as univ_id,
        univer_university.name as univ_name from univer_teacher left join univer_chair on
        univer_teacher.chair_id=univer_chair.id left join univer_faculty on 
        univer_teacher.faculty_id=univer_faculty.id left join univer_university on
        univer_teacher.university_id=univer_university.id """)
        teachers = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', teacher['id']),
                ('name', teacher['name']),
                ('subject', teacher['subject']),
                ('university', OrderedDict(
                    [
                        ('id', teacher['univ_id']),
                        ('name', teacher['univ_name']),
                    ]
                )),
                ('faculty', OrderedDict(
                    [
                        ('id', teacher['faculty_id']),
                        ('name', teacher['faculty_name']),
                        ('university', OrderedDict(
                            [
                                ('id', teacher['univ_id']),
                                ('name', teacher['univ_name']),
                            ]
                        )),
                    ]
                )),
                ('chair', OrderedDict(
                    [
                        ('id', teacher['chair_id']),
                        ('name', teacher['chair_name']),
                        ('faculty', OrderedDict(
                            [
                                ('id', teacher['faculty_id']),
                                ('name', teacher['faculty_name']),
                                ('university', OrderedDict(
                                    [
                                        ('id', teacher['univ_id']),
                                        ('name', teacher['univ_name']),
                                    ]
                                )),
                            ]
                        )),
                    ]
                )),
            ]
        ) for teacher in teachers]


def get_student(std_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_student.*, univer_chair.id as chair_id, univer_chair.name as chair_name,
        univer_faculty.id as faculty_id, univer_faculty.name as faculty_name, univer_university.id as univ_id,
        univer_university.name as univ_name, univer_group.id as group_id, univer_group.number as group_number,
         univer_group.teacher_name as group_t_name, univer_group.pupil_count as group_s_count from univer_student 
         left join univer_chair on univer_student.chair_id=univer_chair.id left join univer_faculty on 
        univer_student.faculty_id=univer_faculty.id left join univer_university on 
        univer_student.university_id=univer_university.id left join univer_group on 
        univer_group.id=univer_student.group_id where univer_student.id = %s""", [std_id])
        std = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', std['id']),
                ('name',std['name']),
                ('university', OrderedDict(
                    [
                        ('id', std['univ_id']),
                        ('name', std['univ_name']),
                    ]
                )),
                ('faculty', OrderedDict(
                    [
                        ('id', std['faculty_id']),
                        ('name', std['faculty_name']),
                        ('university', OrderedDict(
                            [
                                ('id', std['univ-id']),
                                ('name', std['univ_name']),
                            ]
                        )),
                    ]
                )),
                ('chair', OrderedDict(
                    [
                        ('id', std['chair_id']),
                        ('name', std['chair_name']),
                        ('faculty', OrderedDict(
                            [
                                ('id', std['faculty_id']),
                                ('name', std['faculty_name']),
                                ('university', OrderedDict(
                                    [
                                        ('id', std['univ_id']),
                                        ('name', std['univ_name']),
                                    ]
                                )),
                            ]
                        )),
                    ]
                )),
                ('group', OrderedDict(
                    [
                        ('id', std['group_id']),
                        ('number', std['group_number']),
                        ('teacher_name', std['group_t_name']),
                        ('pupil_count', std['group_s_count']),
                        ('chair', OrderedDict(
                            [
                                ('id', std['chair_id']),
                                ('name', std['chair_name']),
                                ('faculty', OrderedDict(
                                    [
                                        ('id', std['faculty_id']),
                                        ('name', std['faculty_name']),
                                        ('university', OrderedDict(
                                            [
                                                ('id', std['univ_id']),
                                                ('name', std['univ_name']),
                                            ]
                                        )),
                                    ]
                                )),
                            ]
                        )),
                    ]
                ))
            ]
        )


def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select univer_student.*, univer_chair.id as chair_id, univer_chair.name as chair_name,
        univer_faculty.id as faculty_id, univer_faculty.name as faculty_name, univer_university.id as univ_id,
        univer_university.name as univ_name, univer_group.id as group_id, univer_group.number as group_number,
         univer_group.teacher_name as group_t_name, univer_group.pupil_count as group_s_count from univer_student 
         left join univer_chair on univer_student.chair_id=univer_chair.id left join univer_faculty on 
        univer_student.faculty_id=univer_faculty.id left join univer_university on 
        univer_student.university_id=univer_university.id left join univer_group on 
        univer_group.id=univer_student.group_id """)
        students = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', std['id']),
                ('name',std['name']),
                ('university', OrderedDict(
                    [
                        ('id', std['univ_id']),
                        ('name', std['univ_name']),
                    ]
                )),
                ('faculty', OrderedDict(
                    [
                        ('id', std['faculty_id']),
                        ('name', std['faculty_name']),
                        ('university', OrderedDict(
                            [
                                ('id', std['univ_id']),
                                ('name', std['univ_name']),
                            ]
                        )),
                    ]
                )),
                ('chair', OrderedDict(
                    [
                        ('id', std['chair_id']),
                        ('name', std['chair_name']),
                        ('faculty', OrderedDict(
                            [
                                ('id', std['faculty_id']),
                                ('name', std['faculty_name']),
                                ('university', OrderedDict(
                                    [
                                        ('id', std['univ_id']),
                                        ('name', std['univ_name']),
                                    ]
                                )),
                            ]
                        )),
                    ]
                )),
                ('group', OrderedDict(
                    [
                        ('id', std['group_id']),
                        ('number', std['group_number']),
                        ('teacher_name', std['group_t_name']),
                        ('pupil_count', std['group_s_count']),
                        ('chair', OrderedDict(
                            [
                                ('id', std['chair_id']),
                                ('name', std['chair_name']),
                                ('faculty', OrderedDict(
                                    [
                                        ('id', std['faculty_id']),
                                        ('name', std['faculty_name']),
                                        ('university', OrderedDict(
                                            [
                                                ('id', std['univ_id']),
                                                ('name', std['univ_name']),
                                            ]
                                        )),
                                    ]
                                )),
                            ]
                        )),
                    ]
                ))
            ]
        ) for std in students]


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row))
            for row in cursor.fetchall()]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
