class Course:

    def __init__(self):
        pass
        
    @classmethod
    def get_course_cost(self, course_name):
        self.course_cost = {
            "DIPLOMA" : 2500,
            "DEGREE" : 5000,
            "CERTIFICATION" : 3000,
        }
        return self.course_cost[course_name]