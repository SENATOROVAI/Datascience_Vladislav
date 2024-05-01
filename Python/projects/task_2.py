"""My task_2."""


class Programmer:
    """My task of programming."""

    price = {"Junior": 10, "Middle": 15, "Senior": 20}

    def __init__(self, name, grade):
        """first initialization."""

        self.name = name
        self.grade = grade
        self.work_time = 0
        self.all_time = 0
        self.base_salary = Programmer.price[self.grade]
        self.final_salary = 0

    def work(self, time):
        """time working."""

        self.work_time = time
        self.all_time += time

    def rise(self):
        """rise price."""

        if self.grade == "Junior":
            self.grade = "Middle"
            self.base_salary = Programmer.price[self.grade]
        elif self.grade == "Middle":
            self.grade = "Senior"
            self.base_salary = Programmer.price[self.grade]
        elif self.grade == "Senior":
            self.base_salary += 1

    def info(self):
        """info about worker."""

        self.final_salary += self.base_salary * self.work_time
        return f"{self.name} {self.all_time}ч. {self.final_salary}тгр."


programmer = Programmer("Васильев Иван", "Junior")
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
