'''

장식 정렬 복원 작업을 할 것이다.

1. 초기 리스트는 정렬 순서를 제어하는 새로운값으로 생성된

2. 정렬

3. 리스트 생성

'''


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

decorated = [(student.grade, i, student) for i, student in enumerate(student_obj)]
decorated.sort()
[student for grade, i, student in decorated]