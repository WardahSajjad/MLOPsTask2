class StudentsInMLOps:
    def __init__(self):
        self.total_students = 0

    def enrollStudents(self, num):
        self.total_students += num

    def dropStudents(self, num):
        if num > self.total_students:
            print("Error: Cannot drop more students than enrolled.")
        else:
            self.total_students -= num

    def getTotalStrength(self):
        return self.total_students

    def getClassName(self):
        return "StudentsInMLOps"
