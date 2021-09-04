# 파이썬은 액세스 함수를 더 쉽고 빠르게 만드는 편리 함수를 제공합니다.
# operator 모듈에는 itemgetter(), attrgetter() 및 methodcaller() 함수가 있습니다.




'''from operator import itemgetter, attrgetter

sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]'''

# -------------------------------------------------------------

'''sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]'''

