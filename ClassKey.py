class Student:
	def _init_(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age
	def _repr_(self):
		return repr((self.name, self.grade, self.age))

student_obj = [
	Student('hyunwoo', 'a', 15),
	Student('James', 'b', 10),
	Student('ami', 'c', 5),
]

sorted(student_obj, key=lambda stydent: stydent.age)