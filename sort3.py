class Student:
	def _init_(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age
	def _repr_(self):
		return repr((self.name, self.grade, self.age))



def ss():
    students = ['dave', 'john', 'jane']
    newgrades = {'john': 'F', 'jane': 'A', 'dave': 'C'}
    sorted(students, key=newgrades.__getitem__)


def sort():

    data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
    standard_way = sorted(data, key=itemgetter(0), reverse=True)
    double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
    assert standard_way == double_reversed
    standard_way


    Student.__lt__ = lambda self, other: self.age < other.age
    sorted(student_objects)