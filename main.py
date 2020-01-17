'''
Once you have defined all of your custom types, go to main.py, import the classes you need, and implement the following logic.

Create 4, or more, exercises.
Create 3, or more, cohorts.
Create 4, or more, students and assign them to one of the cohorts.
Create 3, or more, instructors and assign them to one of the cohorts.
Have each instructor assign 2 exercises to each of the students.
'''
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

exercise_one = Exercise("Intro", "Python")
exercise_two = Exercise("Lists", "Python")
exercise_three = Exercise("Sets", "Python")
exercise_four = Exercise("Dictionaries", "Python")

cohort_38 = Cohort("C38")
cohort_35 = Cohort("C35")
cohort_36 = Cohort("C36")

ryan_b = Student("Ryan", "Bishop", "rdb", cohort_36)
bito_m = Student("Bito", "Mann", "bito", cohort_38)
shirish_s = Student("Shirish", "Shrestha", "Shirish Shrestha", cohort_35)
ryan_c = Student("Ryan", "Cunningham", "Ryan H. Cunningham", cohort_36)

joe_shep = Instructor("Joe", "Shepherd", "joeshep", "Board game guru", cohort_36)
jisie = Instructor("Jisie", "David", "Jisie David", "Keeping Joe in line", cohort_36)
jenna = Instructor("Andy", "Collins", "acollins", "Comedy King", cohort_38)

joe_shep.assign_exercise(ryan_b, exercise_one)
joe_shep.assign_exercise(ryan_b, exercise_two)
jisie.assign_exercise(bito_m, exercise_one)
jisie.assign_exercise(bito_m, exercise_three)
jenna.assign_exercise(shirish_s, exercise_two)
jenna.assign_exercise(shirish_s, exercise_four)
joe_shep.assign_exercise(ryan_c, exercise_four)
joe_shep.assign_exercise(ryan_c, exercise_two)

students = [ryan_b, ryan_c, shirish_s, bito_m]
exercises = [exercise_one, exercise_two, exercise_three, exercise_four]

for student in students:
    student.show_assignments()