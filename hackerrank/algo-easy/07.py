# gradingStudents

def gradingStudents(grades):
    for grade in range(grades):
        grade = int(input())
        if grade < 38: 
            print(grade)
        else:
            old_grade = grade
            while grade %5 != 0:
                grade += 1
            if (grade-old_grade) < 3:
                print(grade)
            else:
                print(old_grade)



grades = int(input())
gradingStudents(grades)