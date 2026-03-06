#Class Setup

class Housing_Data:
    def __init__ (self,
                  school:str,
                  population:dict,
                  students:dict,
                  student_housing:dict,
                  averages:dict,
                  homeless:dict):
        self.school = school
        self.population = population
        self.students = students
        self.student_housing = student_housing
        self.averages = averages
        self.homeless = homeless

    def __repr__(self)->str:
        return "Housing_Data({},{},{},{},{},{})".format(
            self.school,
            self.population,
            self.students,
            self.student_housing,
            self.averages,
            self.homeless)


    def __equal__(self,other)->bool:
        return ((self == other) or
                (type(self)==type(other) and
                 self.school==other.school and
                 self.population==other.population and
                 self.students==other.students and
                 self.student_housing==other.student_housing and
                 self.averages==other.averages and
                 self.homeless==other.homeless))

