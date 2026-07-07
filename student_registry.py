class Student:
    student_count = 0
    
    def __init__(self, name, age=17, grade="11th"):
        Student.student_count += 1
        self.student_id = Student.student_count
        
        #Assign via the properties (not_name directly) to enforce validation upon creation
        
        self.name = name
        self.age = age
        self.grade = grade
        
        # Age property
        @property
        def name(self):
            return self._name
        
        
        @name.setter
        def name(self, value):
            # check:string, 3+ chars, alphanumeric (no spaces/special chars), and title case
            if isinstance(value, str) and len(value) >= 3 and value.isalnum() and value.title():
                self._name = value
            else:
                raise ValueError(f"Invalid name '{value}': Must be 3+ chars, no spaces or special chars, and Title Case.")
            
        #age property
        @property
        def age(self):
            return self._age
        
        @age.setter
        def age(self, value):
            # check if int type, > 11 and < 18
            if isinstance(value, int) and 11 < value < 18:
                self._age = value
            else:
                raise ValueError(f"Invalid age '{value}': Must be an integer between 12 and 18")
        
        #grade property
        @property
        def grade(self):
            return self._grade
        
        @grade.setter
        def grade(self, value):
            valid_grades = ["9th", "10th", "11th", "12th"]
            if isinstance(value, str) and value in valid_grades:
                self._grade = value
            else:
                raise ValueError(f"Invalid grade '{value}': Must be formatted as 9th, 10th, 11th, or 12th.")
        
        # Methods
        def __str__(self):
            return f"Student {self.student_id}: Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
        
        def advance(self, years_advanced=1):
            #Extract integer from the grade
            current_grade_num = int(self.grade.replace("th", ""))
            new_grade_num = current_grade_num + years_advanced
            return f"{self.name} has advanced to the {new_grade_num}th grade"
        
        def study(self, subject):
            return f"{self.name} is studying {subject}"

student_1 = Student("Keith", 16, "10th")

student_2 = Student("Eli", 13, "9th")

student_3 = Student("Joanna", 17, "11th")

print(student_1.name)
print(student_2.age)
print(student_3.grade)

print(f"Getter - Name: {student_1.name}")
print(f"Getter - Age: {student_2.age}")
print(f"Getter - Grade: {student_3.grade}")



        