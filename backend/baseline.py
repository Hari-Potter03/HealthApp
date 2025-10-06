class Baseline:
    def __init__(self, name, age, sex, height, weight, goal, activity_level):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.goal = goal
        self.activity_level = activity_level

    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    

