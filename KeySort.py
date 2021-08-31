'''
    Key함수
'''

'''
sorted("Hello World hello world".split(), key=str.lower)
['Hello', 'hello', 'World', 'world']
대소문자를 구분한다
'''

'''
test_tup = [
    ('hw', 'a', 15),
	('lw', 'b', 10),
	('wh', 'c', 5),
]

sorted(test_tup, key=lambda test_tup: test_tup[2])

복잡한 객체도 정리할수 있다
'''
