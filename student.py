class Student:
    def __init__(self, first_name, last_name, slack_handle, cohort_id):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort_id = cohort_id
        self.assignments = list()

    def add_assignment(self, exercise):
        self.assigngments.append(exercise)

    