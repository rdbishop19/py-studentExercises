from student import Student
from NSSPerson import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle, specialty, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.add_assignment(exercise)