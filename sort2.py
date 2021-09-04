# 정렬의 핵심은 안정성이 보장이 된다는 것이다. 즉 원래의 순서가 유지가 되며 정렬이 된다는것이

'''

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
sorted(data, key=itemgetter(0)

'''

# grade 속성을 내림차순으로 하고 age를 오름차순으로 정렬을 한다면 먼저 age 정렬을 수행한 다음에 그 다음 grade 를 수행한다

'''

s = sorted(student_objects, key=attrgetter('age'))     
sorted(s, key=attrgetter('grade'), reverse=True)       

'''

def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs

multisort(list(student_objects), (('grade', True), ('age', False)))

# 파이썬에서 사용중인 팀 소트는 빠른속도와 안정성으로 정렬할수 있다
