class Person:
  def __init__(self, name, age, habit):
    self.name = name
    self.age = age
    self.habit = habit
  def __str__(self):
    return f"name is {self.name}"