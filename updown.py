# list.sort()와 sorted()는 모두 불리언 값을 갖는 reverse 매개 변수로 쓰인다

# sorted(student_tuples, key=itemgetter(2), reverse=True)
'''[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

sorted(student_objects, key=attrgetter('age'), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]'''