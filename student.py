from oxford import format_list

class Student:
    def __init__(self, first_name, last_name, slack_handle, cohort_id):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort_id = cohort_id
        self.assignments = list()

    def add_assignment(self, exercise):
        self.assignments.append(exercise)

    def show_assignments(self):
        # print()
        # print(f'{self.first_name} has the following assignments:')
        # for assignment in self.assignments:
        #     print(f'{assignment.name} ({assignment.language})')
        assignment_array = []
        for assignment in self.assignments:
            assignment_array.append(assignment.name)
        formatted_list_string = format_list(assignment_array)
        print(f'{self.first_name} is working on {formatted_list_string}')
    