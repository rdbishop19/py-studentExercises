from student import Student

class Instructor:
    def __init__(self, first_name, last_name, slack_handle, specialty, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.specialty = specialty
        self.cohort = cohort

    def assign_exercise(self, student, exercise):
        student.add_assignment(exercise)